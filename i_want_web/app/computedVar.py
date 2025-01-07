# app.py
import reflex as rx
#컴퓨터바
class State(rx.State):
    raw_text: str = "hi"

    @rx.var
    def upper_text(self) -> str:
        return self.raw_text.upper() if self.raw_text else "EMPIY"

@rx.page()
def index():
    return  rx.vstack(
        rx.heading(State.upper_text),
        rx.input(
            on_change=State.set_raw_text,
            placeholder="Type here",
        ),
        align="center",
    )

app = rx.App()