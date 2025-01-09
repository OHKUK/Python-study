import reflex as rx
from time import sleep

class State(rx.State):
    count: int = 1

    @rx.event
    def initialize(self, count: str):
        self.count = abs(int(count if count else 1))
        return State.countdown

    @rx.event
    def countdown(self):
        while self.count > 1:
            sleep(1)
            self.count -= 1
            yield  # 화면의 count 업데이트


@rx.page("/")
def index():
    return rx.vstack(
        rx.badge(State.count),
        rx.input(on_blur=State.initialize),
    )

app = rx.App()
