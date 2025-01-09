import time
import reflex as rx


class State(rx.State):
    count: int = 0

    @rx.event
    def update_one_by_one(self):
        for i in range(100):
            self.count += 1
            time.sleep(0.01)
            yield


@rx.page("/")
def single_update():
    return rx.vstack(
        rx.text(State.count),
        rx.button("Start", on_click=State.update_one_by_one),
        rx.button("Reset", on_click=State.set_count(0))  # <--- 직전 챕터에서 언급했던 partial event 문법입니다.
    )

app = rx.App()
