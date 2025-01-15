from math import lcm
import reflex as rx


class State(rx.State):
    input_value: str  # 사용자 입력이 저장되는 변수
    answer: str  # 계산결과가 저장되는 변수

    @rx.event
    def calc_lcm(self):
        num_list = [int(i) for i in self.input_value.strip().split(" ")]
        result = lcm(*num_list)
        self.answer = f"{result:,}"


@rx.page(on_load=rx.set_focus("user_input"))
def index():
    return rx.vstack(
        rx.heading("최소공배수 계산기"),
        rx.text("띄어쓰기로 구분하여 두 개 이상의 자연수를 입력해주세요."),
        rx.hstack(
            rx.input(
                id="user_input",
                placeholder="입력 후 계산 버튼을 눌러주세요",
                on_change=State.set_input_value.throttle(500),
            ),
            rx.button("계산", on_click=[rx.set_focus("user_input"), State.calc_lcm]),
        ),
        rx.hstack(
            rx.text("최소공배수는 ", as_="span"),
            rx.text(State.answer, as_="span", color_scheme="mint"),
            rx.text("입니다.", as_="span"),
        ),
        align="center",
    )


app = rx.App()
