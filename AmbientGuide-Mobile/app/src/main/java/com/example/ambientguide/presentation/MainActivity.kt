package com.example.ambientguide.presentation

import android.content.Context
import android.content.SharedPreferences
import android.os.Bundle
import android.os.PowerManager
import android.os.Vibrator
import android.os.VibrationEffect
import android.speech.tts.TextToSpeech
import android.util.Log
import android.view.WindowManager
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.Image
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Devices
import androidx.compose.ui.tooling.preview.Preview
import com.example.ambientguide.presentation.theme.AmbientGuideTheme
import java.net.DatagramPacket
import java.net.DatagramSocket
import java.util.*
import com.example.ambientguide.R
import java.net.InetAddress
import java.net.SocketTimeoutException

class MainActivity : ComponentActivity(), TextToSpeech.OnInitListener {
    private var ip_address: InetAddress? = null
    private lateinit var vibrator: Vibrator
    private lateinit var wakeLock: PowerManager.WakeLock
    private lateinit var sharedPreferences: SharedPreferences
    private var voiceMessagesEnabled by mutableStateOf(true)
    private lateinit var tts: TextToSpeech
    private var number by mutableStateOf(0)
    private var i = 2
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Creating wake lock
        wakeLock = (getSystemService(Context.POWER_SERVICE) as PowerManager).run {
            newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "MyApp::MyWakelockTag").apply {
                acquire()
            }
        }

        sharedPreferences = getSharedPreferences("MyPrefs", Context.MODE_PRIVATE)

        setContent {
            setTheme(android.R.style.Theme_DeviceDefault)

            vibrator = getSystemService(Context.VIBRATOR_SERVICE) as Vibrator

            tts = TextToSpeech(this@MainActivity, this@MainActivity)

            // Setting up WearApp composable
            WearApp(greetingName = "Android", startVibration = ::startVibration, tts = tts, voiceMessagesEnabled = voiceMessagesEnabled, toggleVoiceMessagesEnabled = ::toggleVoiceMessagesEnabled)
        }

        Thread {
            try {
                receiveUDPPacket()
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }.start()
    }

    // Dodanie funkcji wysyłającej broadcast
    private fun sendBroadcastInfo() {
        val message = "2137"
        val socket = DatagramSocket()
        socket.broadcast = true // Ustawienie socketu na broadcast

        val broadcastAddress = InetAddress.getByName("255.255.255.255") // Adres broadcastowy
        val data = message.toByteArray()

        val packet = DatagramPacket(data, data.size, broadcastAddress, 2137)

        // Pętla do ponownego wysyłania pakietu, dopóki nie otrzymasz pakietu zwrotnego
        var connected = false
        while (!connected) {
            try {
                socket.send(packet)
                socket.soTimeout = 5000 // Ustawienie timeout'u na 5 sekund dla oczekiwania na odpowiedź
                val responseBuffer = ByteArray(1024)
                val responsePacket = DatagramPacket(responseBuffer, responseBuffer.size)
                socket.receive(responsePacket)
                // Jeśli otrzymaliśmy odpowiedź, ustaw flagę na true i wyjdź z pętli
                connected = true
                ip_address = responsePacket.address
                i = 0
                Log.d("UDP", "Otrzymano pakiet zwrotny od: ${responsePacket.address}")
                // Informowanie użytkownika za pomocą TTS
                tts.speak("Połączenie nawiązane", TextToSpeech.QUEUE_FLUSH, null, null)
            } catch (e: SocketTimeoutException) {
                Log.e("UDP", "Timeout - Brak odpowiedzi, ponowne wysyłanie...")
                // Jeśli timeout, ponownie wyślij pakiet
            } catch (e: Exception) {
                Log.e("UDP", "Błąd podczas odbierania pakietu zwrotnego: ${e.message}")
                // Obsłuż inne wyjątki, jeśli są
            }
        }
        Log.d("UDP", "Połączenie nawiązane.")
    }

    private fun checkConnection() {
        val socket = DatagramSocket()
        socket.broadcast = true // Ustawienie socketu na broadcast

        val broadcastAddress = InetAddress.getByName("255.255.255.255") // Adres broadcastowy
        val message = "AmbientGuide_Check_Connect" // Zmiana wiadomości na AmbientGuide_Check_Connect
        val data = message.toByteArray()

        val packet = DatagramPacket(data, data.size, broadcastAddress, 2137)

        try {
            socket.send(packet)
            socket.soTimeout = 2500 // Ustawienie timeout'u na 5 sekund dla oczekiwania na odpowiedź

            val responseBuffer = ByteArray(1024)
            val responsePacket = DatagramPacket(responseBuffer, responseBuffer.size)
            socket.receive(responsePacket)
            if (responsePacket.address == ip_address) {
                Log.d("UDP", "${responsePacket.address}")
            }
            // Sprawdzenie czy otrzymana wiadomość zwrotna jest taka sama jak wysłana
            val responseMessage = String(responsePacket.data, 0, responsePacket.length)
            if (responseMessage == message) {
                // Jeśli otrzymaliśmy odpowiedź z oczekiwaną wiadomością, oznacza to, że połączenie jest aktywne
                Log.d("UDP", "Połączenie jest aktywne.")
            } else {
                // W przeciwnym razie oznacza to, że połączenie zostało przerwane
                Log.e("UDP", "Otrzymano nieprawidłową odpowiedź: $responseMessage. Połączenie zostało przerwane.")
                // Tutaj można dodać kod reakcji na przerwanie połączenia
            if (i != 0) {
                i = 0
            }}
        } catch (e: SocketTimeoutException) {
            // Jeśli timeout, oznacza to, że połączenie zostało przerwane
            Log.e("UDP", "Połączenie zostało przerwane.")
            if (i >= 1){
                tts.speak("Utracono połączenie", TextToSpeech.QUEUE_FLUSH, null, null)
                ip_address = null
            }
            i++
            // Tutaj można dodać kod reakcji na przerwanie połączenia
        } catch (e: Exception) {
            Log.e("UDP", "Błąd podczas sprawdzania połączenia: ${e.message}")
            // Obsłuż inne wyjątki, jeśli są
        } finally {
            socket.close()
        }
    }

    override fun onResume() {
        super.onResume()
        updateKeepScreenOnFlag()
        // Wysłanie broadcastu po wznowieniu aplikacji
        Thread {
            while (true){
                if (ip_address == null) {
                    sendBroadcastInfo()
                }
                else {
                    Thread.sleep(1000)
                    checkConnection()
                }
            }

        }.start()

    }

    private fun updateKeepScreenOnFlag() {
        window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
    }

    override fun onDestroy() {
        wakeLock.release()
        tts.stop()
        tts.shutdown()

        super.onDestroy()
    }

    override fun onInit(status: Int) {
        if (status == TextToSpeech.SUCCESS) {
            val result = tts.setLanguage(Locale.getDefault())
            if (result == TextToSpeech.LANG_MISSING_DATA || result == TextToSpeech.LANG_NOT_SUPPORTED) {
                Log.e("TTS", "This Language is not supported")
            }
        } else {
            Log.e("TTS", "Initialization Failed!")
        }
    }

    private fun startVibration() {
        val pattern = when (number) {
            0 -> longArrayOf(0, 1000)
            1 -> longArrayOf(0, 400, 200, 400)
            2 -> longArrayOf(0, 200, 200, 200, 200, 200)
            else -> longArrayOf(0, 1000, 500)
        }
        vibrator.vibrate(VibrationEffect.createWaveform(pattern, -1))
    }

    private fun receiveUDPPacket() {
        val socket = DatagramSocket(2137)
        val buffer = ByteArray(1024)
        val packet = DatagramPacket(buffer, buffer.size)

        while (true) {
            socket.receive(packet)
            val receivedData = String(packet.data, packet.offset, packet.length)
            val parts = receivedData.split("|")
            if (parts.size == 2) {
                runOnUiThread {
                    val message = parts[0]
                    number = parts[1].toInt()
                    val side = when (number) {
                        0 -> "Na przeciwko"
                        1 -> "Lewa"
                        2 -> "Prawa"
                        else -> "Błąd"
                    }
                    startVibration()
                    // Use voiceMessagesEnabled from MainActivity
                    if (voiceMessagesEnabled) {
                        tts.speak(message.plus(side), TextToSpeech.QUEUE_FLUSH, null, null)
                    }
                }
            }
        }
    }

    // Nowa funkcja do wyłączania komunikatów głosowych
    private fun toggleVoiceMessagesEnabled() {
        voiceMessagesEnabled = !voiceMessagesEnabled
    }
}

@Composable
fun WearApp(greetingName: String, startVibration: () -> Unit, tts: TextToSpeech, voiceMessagesEnabled: Boolean, toggleVoiceMessagesEnabled: () -> Unit) {
    // Usunięcie deklaracji voiceMessagesEnabled
    AmbientGuideTheme {
        Box(
            modifier = Modifier.fillMaxSize(),
            contentAlignment = Alignment.Center
        ) {
            Image(
                painter = painterResource(id = R.drawable.logo),
                contentDescription = null,
                modifier = Modifier.fillMaxSize().clickable {
                    // Wywołanie funkcji do wyłączania komunikatów głosowych po kliknięciu
                    toggleVoiceMessagesEnabled()
                    val message = if (!voiceMessagesEnabled) "Komunikaty głosowe włączone" else "Komunikaty głosowe wyłączone"
                    tts.speak(message, TextToSpeech.QUEUE_FLUSH, null, null)
                },
                contentScale = ContentScale.FillBounds
            )
        }
    }
}

@Preview(device = Devices.WEAR_OS_SMALL_ROUND, showSystemUi = true)
@Composable
fun DefaultPreview() {
    val startVibration: () -> Unit = {}
    val context = LocalContext.current
    val tts = TextToSpeech(context, TextToSpeech.OnInitListener { })
    val voiceMessagesEnabled = remember { mutableStateOf(true) } // Initialize voiceMessagesEnabled
    WearApp("Preview Android", startVibration, tts, voiceMessagesEnabled.value) {}
}
