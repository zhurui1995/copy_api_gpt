# author: zhu rui
# date: 2024.9.13
import clipboard
import time


def get_string_from_clipboard():
    text = clipboard.paste()  # 从剪贴板获取文本数据
    return text


def middleware_llm_call(query):
    clipboard.copy(query)  # 把需要查询的放到剪切板中
    previous_text = get_string_from_clipboard()

    while True:
        res_ = get_string_from_clipboard()
        if res_ == previous_text:
            print(". ", end="")
            time.sleep(3)
        else:
            print(res_)  # 一般中间结果直接在程序中使用，这里打印方便查看中间结果
            return res_


def copy_to_clipboard(string):
    """ 将需要的字符串或文字复制到剪切板. """
    clipboard.copy(string)


def get_llm_call(prompt=None, system_prompt=None):
    all_prompt = system_prompt + "\n\n" + prompt if system_prompt else prompt
    copy_to_clipboard("")  # 清空剪切板
    res_ = middleware_llm_call(all_prompt)
    copy_to_clipboard(res_)
    return res_


def my_llm_call(prompt, system_prompt=None):
    sys_prompt_arg = system_prompt if system_prompt else ""
    middle_ware_response = get_llm_call(prompt=prompt, system_prompt=sys_prompt_arg)
    return middle_ware_response


class T:
    pass


class Response:
    def __init__(self):
        self.choices = [T(), ]
        self.choices[0].message = T()


class MyOpenaiClient:
    def __init__(self):
        self.chat = T()
        self.chat.completions = T()
        self.__call__ = self._openai_history_call
        self.chat.completions.create = self.__call__

    def _openai_history_call(self, model, messages, temperature=0, max_tokens=4096, n=1, stop=None, seed=0):
        if len(messages):
            prompt = ""
            for message in messages:
                prompt += "角色:" + message["role"] + "\n" + "内容:" + message["content"] + "\n" + "\n"
            res_ = self._openai_call(prompt=prompt)
            response = Response()
            response.choices[0].message.content = res_
            return response
        else:
            print("留个 todo在这里")

    def _openai_call(self, prompt=None, system_prompt=None):
        prompt = prompt if prompt else "没传入prompt，随便问个问题。讲个笑话"

        res_ = my_llm_call(prompt=prompt, system_prompt=system_prompt)
        return res_


if __name__ == '__main__':
    # res = my_llm_call("讲个笑话")
    # print(res)

    messages = [{"role": "user", "content": "讲个笑话"}]
    client_ = MyOpenaiClient()
    response = client_.chat.completions.create(
        model="random",
        messages=messages)
    res = response.choices[0].message.content
    print(res)
