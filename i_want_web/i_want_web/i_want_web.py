import  reflex as rx

# Make it count!
# class State(rx.State):
#     num = 0
#
#     def 감소(self):
#         self.num -= 1
#
#     def 증가(self):
#         self.num += 1
#
# def index():
#     return rx.container(
#         rx.hstack(
#             rx.button("감소", on_click=State.감소, color_scheme="ruby"),
#             rx.text(State.num, font_size="1.5em"),
#             rx.button("증가", on_click=State.증가, color_scheme="grass"),
#             spacing="4",
#         )
#     )
#

#todo


class State(rx.State):
    todo = ["씻기", "아침먹기", "옷입기", "출근하기"]

def render_fn(item):
    return rx.hstack(
        rx.icon_button("circle_check_big", size="1", bg="tomato"),
        rx.text(item),
    )


def index():
    return rx.container(
        rx.foreach(State.todo, render_fn)
    )

app = rx.App()
app.add_page(index)