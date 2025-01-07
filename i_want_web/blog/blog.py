import  reflex as rx
"""
Make it count!
class State(rx.State):
    num = 0

    def 감소(self):
        self.num -= 1

    def 증가(self):
        self.num += 1

def index():
    return rx.container(
        rx.hstack(
            rx.button("감소", on_click=State.감소, color_scheme="ruby"),
            rx.text(State.num, font_size="1.5em"),
            rx.button("증가", on_click=State.증가, color_scheme="grass"),
            spacing="4",
        )
    )


todo


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

todolist에 추가하는 방식
class State(rx.State):
    num: int
    num_list = [3, 2, 1]

    def add_num(self):
        self.num_list.insert(0, self.num)
        # self.num_list.insert(0, self.num_list[0] + 1)

def index():
    return rx.container(
        rx.vstack(
            # rx.input(value=State.num, on_change=State.set_num),
            # rx.button("추가", on_click=State.add_num),
            # rx.foreach(State.num_list, rx.text)
            rx.form(
                rx.input(on_change=State.set_num),
                on_submit = lambda x: State.add_num(),
                reset_on_submit=True
            ),
            rx.foreach(State.num_list, rx.text)
        )
    )

#todolist 완성

class State(rx.State):
    todo: str
    todo_list: list[str]
    todo_list = ["영어공부", "수학공부", "코딩연습"]
    completed: list[bool]
    completed = [False, False, False]
    on_edit:list[bool]
    on_edit = [False, False, False]


    def add_todo(self):
        self.todo_list.insert(0, self.todo)
        self.completed.insert(0, False)
        self.on_edit.insert(0, False)

    def pop_todo(self, idx:int):
        self.todo_list.pop(idx)
        self.completed.pop(idx)
        self.on_edit.pop(idx)

    def update_todo(self, x:dict[str:str]):
        x는 {"0": "new_todo"} 형식의 사전데이터임.
        사전의 키인 "0"을 정수로 바꿔서 인덱스로 활용하고
        사전의 값으로 "할일" 문자열을 업데이트함
        i, val = x.popitem()
        i = int(i)
        self.todo_list[i] = val
        self.on_edit[i] = False

    def toggle(self, idx:int):
        self.completed[idx] = ~self.completed[idx]

    def toggle_edit(self, idx:int):
        self.on_edit[idx] = not self.on_edit[idx]

def render_fn(item,idx):
    return rx.hstack(
        rx.cond(
          State.completed[idx],
            rx.icon("circle-check-big", size=10, on_click=lambda: State.toggle(idx)),
            rx.icon("circle", size=10, on_click=lambda: State.toggle(idx))
        ),
        rx.cond(
            State.completed[idx],
            rx.text(item, style={"text-decoration": "line-through"}),
            rx.cond(
                State.on_edit[idx],
                rx.form(
                    rx.input(default_value=item, autofocus=True, on_change=State.set_todo, name=idx.to_string()),
                    on_submit=State.update_todo,
                    reset_on_submit=True
                ),
                rx.text(item, on_click=lambda: State.toggle_edit(idx)),
            )
        ),
        rx.icon("trash-2", size=10, on_click=lambda: State.pop_todo(idx)),

        align="center"
    )

def index():
    return rx.container(
            rx.form(
                rx.input(on_change=State.set_todo),
                on_submit = lambda x: State.add_todo(),
                reset_on_submit=True
            ),
            rx.foreach(State.todo_list, lambda item,idx: render_fn(item, idx))
    )


app = rx.App()
app.add_page(index)
        
"""
# 동적 라우팅 사용법
class Post(rx.Model, table=True):
    title: str
    content: str
    created_at: str


class State(rx.State):
    post: dict

    def get_post(self):
        with rx.session() as session:
            try:
                post = session.exec(
                    Post.select()
                    .where(Post.id == self.pid)).first().dict()
            except AttributeError as e:
                post = {"error": "해당 포스팅을 찾을 수 없습니다."}
        self.post = post


@rx.page(route="/[pid]", on_load=State.get_post)
def post():
    return rx.cond(
        State.post["error"],
        rx.text(State.post["error"]),
        rx.box(
            rx.heading(State.post["title"], align="center"),
            rx.divider(),
            rx.text(State.post["created_at"], size="1", align="right"),
            rx.text(State.post["content"]),
        )
    )


app = rx.App()