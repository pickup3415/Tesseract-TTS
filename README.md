# Tesseract-TTS

# 소개

# Tesseract OCR

## Tesseract-OCR이란

Tesseract OCR은 아파치 라이선스에 따라 사용할 수 있는 오픈소스 엔진이다.  

-https://github.com/tesseract-ocr/tesseract

위 주소에 기반을 두고 학습 데이터를 기반으로 학습해 작동하는며 레거시 시스템과 LSTM 신경망을 기반으로 한다.  
Tesseract_ocr 파일에는 Windows용 Tesseract와 훈련된 학습데이터가 들어있고 기존의 데이터에  
https://github.com/tesseract-ocr/tessdata 의 학습데이터를 추가하여 정확도를 높였다. 

## 실행 

![OCR1](https://user-images.githubusercontent.com/102271636/170234987-7fc3255c-ef09-4b98-84a1-e22eaa37ee1f.PNG)


## 설정 방법

Tesseract_ocr 파일 다운로드  

아래 두 방식 중 택 1

- 파이썬 라이브러리 설치 경로인 site-packages파일에 pytesseract-0.3.9.dist-info와 pytesseract파일 추가 
- CMD에 "pip install pytesseract"를 입력


# TTS
## TTS란

구글 텍스트 음성 변환(gTTS)는 구글 번역의 텍스트 음성변환 API와 인터페이스하는 파이썬 라이브러리및 CLI도구이다.  
애플리케이션에 화면상의 텍스트를 읽는 기능을 제공한다.  
또한 gTTS 모듈은 전처리기 및 토큰화 특징을 제공하고 쉽게 확장할 수 있게 해준다.

## 설정방법

아래 두 방식중 택 1  

- 파이썬 라이브러리 설치 경로인 site-packages파일에 gtts와 gTTS-2.2.4.dist-info파일을 추가
- CMD에 "pip install gTTS"를 입력

## 실행

![tts1](https://user-images.githubusercontent.com/102271636/170234433-7187197d-3c13-45e0-8317-52aa2da60dc6.PNG)

# License

    The code in this repository is licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

**NOTE**: This software depends on other packages that may be licensed under different open source licenses.

Tesseract uses [Leptonica library](http://leptonica.com/) which essentially
uses a [BSD 2-clause license](http://leptonica.com/about-the-license.html).
