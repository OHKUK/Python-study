"""
#클릭 이벤트
import reflex as rx

class State(rx.State):
    number: int = 0
    @rx.event
    def inc(self):
        self.number += 1

@rx.page()
def index():
    return rx.vstack(
        rx.heading(State.number),
        rx.button("클릭",on_click=State.inc),
        align="center"
    )

app = rx.App()

#슬라이더 이벤트
import reflex as rx


class State(rx.State):
    value: int = 0

    # 이벤트핸들러 정의
    @rx.event
    def update_value(self, slide_val: int):
        self.value = slide_val


@rx.page()
def index():
    return rx.vstack(
        rx.heading(State.value),
        rx.slider(
            default_value=State.value,
            on_change=State.update_value  # 이벤트트리거 정의
        ),
        align="center"
    )

app = rx.App()


import reflex as rx


class State(rx.State):
    value: list
    value = [0]


@rx.page()
def index():
    return rx.vstack(
        rx.heading(State.value[0]),
        rx.slider(
            default_value=State.value,
            on_change=State.set_value
        ),
        align="center"
    )

app = rx.App()
"""