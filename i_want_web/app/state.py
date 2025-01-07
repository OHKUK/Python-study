# state.py
import reflex as rx

class State(rx.State):
    ticker: str = "AAPL"
    price: str = "$150"

@rx.page()
def index():
    return rx.center(
        rx.vstack(
            rx.heading(State.ticker, size="3"),
            rx.text(
                f"Current Price: {State.price}",
                font_size="md",
            ),
            rx.text("Change: 4%", color="green"),
        ),
    )

app = rx.App()