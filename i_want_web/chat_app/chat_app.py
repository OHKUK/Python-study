import reflex as rx
from openai import OpenAI, AsyncOpenAI
from reflex import session


class State(rx.State):
    q: str
    qa_list: list[list[str]]

    async def append_qa(self, d):
        self.q = d["q"]
        self.answer = ""
        self.qa_list.append(
            [self.q, self.answer]
        )

        client = AsyncOpenAI()
        session = await client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": self.q,
            }],
            model="gpt-4o-mini",
            stop=None,
            stream=True,
        )
        yield

        async for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    break
                self.answer += item.choices[0].delta.content
                self.qa_list[-1][1] = self.answer
                yield


# 비동기로 변경
#     def append_qa(self, d):
#         self.q = d["q"]
#         self.qa_list.append(
#             [self.q, self.ai_answer(self.q)]
#         )
    def ai_answer(self, q: str):
        client = OpenAI()
        response = client.chat.completions.with_raw_response.create(
            messages=[{
                "role": "user",
                "content": q,
            }],
            model="gpt-4o-mini",
        )

        return response.parse().choices[0].message.content



def qa(qna):
    return rx.box(
        rx.box(qna[0],
               background_color="green",
               text_align="right"),
        rx.box(qna[1],
               background_color="orange",
               text_align="left"),
    )


@rx.page()
def index() -> rx.Component:
    return rx.container(
        rx.foreach(State.qa_list, qa),
        rx.form(
            rx.input(
                placeholder="질문을 입력하세요.",
                name="q"
            ),
            on_submit=State.append_qa,
            reset_on_submit=True
        )
    )


app = rx.App()
