import asyncio
import reflex as rx


class State(rx.State):
    counter: int = 0
    max_counter: int = 10
    running: bool = False
    _n_tasks: int = 0

    @rx.event(background=True)
    async def my_task(self):
        async with self:
            # The latest state values are always available inside the context
            if self._n_tasks > 0:
                # only allow 1 concurrent task
                return

            # State mutation is only allowed inside context block
            self._n_tasks += 1

        while True:
            async with self:
                # Check for stopping conditions inside context
                if self.counter >= self.max_counter:
                    self.running = False
                if not self.running:
                    self._n_tasks -= 1
                    return

                self.counter += 1

            # Await long operations outside the context to avoid blocking UI
            await asyncio.sleep(0.5)

    @rx.event
    def toggle_running(self):
        self.running = not self.running
        if self.running:
            return State.my_task

    @rx.event
    def clear_counter(self):
        self.counter = 0


@rx.page("/")
def background_task_example():
    return rx.hstack(
        rx.heading(State.counter, " /"),
        rx.input(
            value=State.max_counter,
            on_change=State.set_max_counter,
            width="8em",
        ),
        rx.button(
            rx.cond(~State.running, "Start", "Stop"),
            on_click=State.toggle_running,
        ),
        rx.button(
            "Reset",
            on_click=State.clear_counter,
        ),
    )


app = rx.App()
