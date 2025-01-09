"""
asyncio를 이용한 비동기 최종코드
"""
import asyncio
import reflex as rx


class State(rx.State):
    color_a:str = "Red"
    color_b:str = "Green"
    color_c:str = "Blue"

    @rx.event
    async def change_a(self):
        await asyncio.sleep(1)
        if self.color_a == "Red":
            self.color_a = "Magenta"
        else:
            self.color_a = "Red"

    @rx.event
    async def change_b(self):
        await asyncio.sleep(1)
        if self.color_b == "Green":
            self.color_b = "Brown"
        else:
            self.color_b = "Green"

    @rx.event
    async def change_c(self):
        await asyncio.sleep(1)
        if self.color_c == "Blue":
            self.color_c = "Black"
        else:
            self.color_c = "Blue"

    @rx.event
    async def change_all(self):
        await asyncio.gather(
            self.change_a(),
            self.change_b(),
            self.change_c(),
        )

@rx.page("/")
def index():
    return rx.vstack(
        rx.hstack(
            rx.text("A", color=State.color_a),
            rx.text("B", color=State.color_b),
            rx.text("C", color=State.color_c),
        ),
        rx.button("Change", on_click=State.change_all)
    )


app = rx.App()
