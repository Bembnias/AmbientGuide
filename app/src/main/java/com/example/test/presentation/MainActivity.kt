package com.example.wibracje.presentation

import android.content.Context
import android.os.Bundle
import android.os.VibrationEffect
import android.os.Vibrator
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Devices
import androidx.compose.ui.tooling.preview.Preview
import androidx.wear.compose.material.Button
import androidx.wear.compose.material.MaterialTheme
import androidx.wear.compose.material.Text
import androidx.wear.compose.material.TimeText
import com.example.test.presentation.theme.TestTheme


class MainActivity : ComponentActivity() {
    private lateinit var vibrator: Vibrator

    override fun onCreate(savedInstanceState: Bundle?) {
        installSplashScreen()

        super.onCreate(savedInstanceState)

        setTheme(android.R.style.Theme_DeviceDefault)

        vibrator = getSystemService(Context.VIBRATOR_SERVICE) as Vibrator

        setContent {
            WearApp(greetingName = "Android", startVibration = ::startVibration)        }
    }

    fun startVibration() {
        if (vibrator.hasVibrator()) {
            vibrator.vibrate(VibrationEffect.createOneShot(2000, VibrationEffect.DEFAULT_AMPLITUDE))
            Thread.sleep(1000)


        }
    }
}

@Composable
fun WearApp(greetingName: String, startVibration: () -> Unit) {
    TestTheme {
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(MaterialTheme.colors.background),
            contentAlignment = Alignment.Center
        ) {
            TimeText()
            Button(onClick = startVibration) {
                Text("Vibrate")
            }
        }
    }
}

@Preview(device = Devices.WEAR_OS_SMALL_ROUND, showSystemUi = true)
@Composable
fun DefaultPreview() {
    val startVibration: () -> Unit = {}
    WearApp("Preview Android", startVibration)
}