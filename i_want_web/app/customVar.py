import googletrans  # googletrans==4.0.0rc1 버전 설치 필요
import reflex as rx


class Translation(rx.Base):
    """구글 번역 결과를 담는 커스텀 바"""
    original_text: str
    en_text: str
    es_text: str
    ja_text: str


class State(rx.State):
    input_text: str = "안녕하세요"
    cur_tr: Translation = Translation(  # 커스텀 바 초기화
        original_text="",
        en_text="",
        es_text="",
        ja_text="",
    )

    @rx.event
    async def translate(self):
        """번역 이벤트"""
        # Google Translator 인스턴스 생성
        translator = googletrans.Translator()

        # 번역 작업 (await 키워드로 실행)
        en_text = (await translator.translate(self.input_text, dest="en")).text
        es_text = (await translator.translate(self.input_text, dest="es")).text
        ja_text = (await translator.translate(self.input_text, dest="ja")).text

        # 상태 업데이트
        self.cur_tr = Translation(
            original_text=self.input_text,
            en_text=en_text,
            es_text=es_text,
            ja_text=ja_text,
        )

    @rx.event
    async def set_input_text(self, value: str):
        """입력된 텍스트를 업데이트"""
        self.input_text = value


@rx.page("/")
def translation_example():
    return rx.vstack(
        # 사용자 입력
        rx.input(
            on_blur=State.set_input_text,  # 텍스트 입력 후 상태 업데이트
            default_value=State.input_text,
            placeholder="Text to translate...",
        ),
        # 번역 버튼
        rx.button(
            "Translate", on_click=State.translate
        ),
        # 번역 결과 표시
        rx.text("English: " + State.cur_tr.en_text),
        rx.text("Spanish: " + State.cur_tr.es_text),
        rx.text("Japanese: " + State.cur_tr.ja_text),
    )


# 애플리케이션 생성
app = rx.App()
