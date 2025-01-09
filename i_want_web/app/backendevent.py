import reflex as rx


class State(rx.State):
    colors: list[str]
    colors = [
        "rgba(245,168,152,0.9)",
        "MediumSeaGreen",
        "#DEADE3",
    ]

    @rx.event
    def change_color(self, color: str, index: int):  # 이벤트핸들러에서는 자료형을 꼭 명시해야 함
        self.colors[index] = color


@rx.page()
def index():
    return rx.hstack(
        rx.input(
            default_value=State.colors[0],
            on_blur=lambda c: State.change_color(c, 0), #c가 없어도 정상으로 작동함
            bg=State.colors[0],
        ),
        rx.input(
            default_value=State.colors[1],
            on_blur=lambda c: State.change_color(c, 1),
            bg=State.colors[1],
        ),
        rx.input(
            default_value=State.colors[2],
            on_blur=lambda c: State.change_color(c, 2),
            bg=State.colors[2],
        ),
    )


app = rx.App()
