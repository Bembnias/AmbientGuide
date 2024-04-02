FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libopencv-core-dev \
    libopencv-imgproc-dev \
    libopencv-video-dev \
    libopencv-videoio-dev \
    libopencv-highgui-dev \
    libopencv-imgcodecs-dev \
    libopencv-objdetect-dev \
    libopencv-features2d-dev \
    libopencv-calib3d-dev \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN useradd -m docker && chown -R docker:docker /app
USER docker

CMD ["python", "main.py"]
