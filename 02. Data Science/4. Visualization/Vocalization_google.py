from gtts import gTTS

default_str = """
안녕하세요. 홍길동입니다.. 스마트홈네트워크를 구동시키겠습니다.
오늘의 추천 뉴스를 알려드리겠습니다.
오늘도 버닝썬관련 뉴스가 화제입니다.
처음에는 단순하게 보였지만 뒤에 가려진 것들이 드러나면서 점차 사건은
게이트화되어 가고 있습니다."""
emotion_str = "안녕하세요. 안녕하세요? 안녕하세요! 안녕하세요.. 젠장. 젠장? 젠장!"

def speaker(a) :
    tts = gTTS(text=a, lang='ko')
    tts.save("test.mp3")

    open("test.mp3")

speaker(default_str)
# speaker(emotion_str)