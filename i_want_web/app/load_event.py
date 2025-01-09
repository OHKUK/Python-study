from time import sleep
import reflex as rx

class State(rx.State):
    count: int = 0

    @rx.var
    def data(self):
        sleep(3) #fetching
        return "Hello world"

    @rx.event
    def inc(self):
        self.count += 1

@rx.page()
def index():
    return  rx.vstack(
        rx.text(State.data),
        rx.text("It's a beautiful app!"),
        rx.hstack(
            rx.button("inc", on_click=State.inc),
            rx.text(State.count),
        )
    )


app = rx.App()
