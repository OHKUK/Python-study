import reflex as rx

class State(rx.State):
    authenticated: bool = False

    @rx.event
    def login(self):
        self.authenticated = True
        return rx.redirect("/")

    @rx.event
    def check_auth(self):
        # check if user is authenticated
        if not self.authenticated:
            return rx.redirect("/login")

@rx.page("/login")
def login():
    return rx.vstack(
        rx.text("먼저 로그인해주세요."),
        rx.input(placeholder="아이디를 입력하세요"),
        rx.input(placeholder="패스워드를 입력하세요."),
        rx.button("로그인", on_click=State.login)
    )

@rx.page(on_load=State.check_auth)
def index():
    return rx.text("A Beautiful App")

app= rx.App()