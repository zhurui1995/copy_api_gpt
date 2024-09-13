# Copy API GPT

A Python script that uses the system clipboard as a communication medium to simulate OpenAI's ChatGPT API calls. This tool allows you to interact with a language model via the clipboard, suitable for environments where direct API access is not possible.

## Features

- Simulates OpenAI's ChatGPT API client.
- Uses the system clipboard to send and receive messages.
- Provides middleware for LLM (Large Language Model) calls via the clipboard.

## Requirements

- Python 3.x
- `clipboard` module (install via):

  ```bash
  pip install clipboard
  ```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

2. **Install the required Python packages**:

   ```bash
   pip install clipboard
   ```

## Usage

Run the script directly:

```bash
python copy_api_gpt.py
```

By default, the script will:

- Send the user message "Tell me a joke" to the simulated API.
- Wait for a response via the clipboard.
- Print the response content.

## How It Works

The script performs the following steps:

1. **Copy the prompt to the clipboard**: The user prompt and system prompt (if any) are combined and copied to the clipboard.

2. **Wait for a response**: The script continuously checks the clipboard for changes. When a change is detected (indicating that a response has been placed in the clipboard), it retrieves the response.

3. **Simulate the API client**: The `MyOpenaiClient` class simulates the behavior of OpenAI's API client, allowing you to use the same method calls as the actual API (`chat.completions.create`).

## Customization

You can modify the script to change prompts or add additional features:

- **Change the prompt**: Modify the `messages` variable in the `__main__` section.

  ```python
  messages = [{"role": "user", "content": "Enter your custom prompt here"}]
  ```

- **Add a system prompt**: Include a system prompt by modifying the `system_prompt` parameter in the `my_llm_call` function.

## Example

Here's how to modify the script to ask a different question:

```python
if __name__ == '__main__':
    messages = [{"role": "user", "content": "Please explain the basic principles of quantum mechanics."}]
    client_ = MyOpenaiClient()
    response = client_.chat.completions.create(
        model="random",
        messages=messages)
    res = response.choices[0].message.content
    print(res)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to OpenAI for the inspiration from their GPT models and API.
- Utilized the `clipboard` Python module for clipboard interactions.

## Contact

For questions or suggestions, please open an issue .

---
# Copy API GPT

一个使用系统剪贴板作为通信媒介来模拟 OpenAI ChatGPT API 调用的 Python 脚本。该工具允许您通过剪贴板与语言模型进行交互，适用于无法直接访问 API 的环境。

## 功能

- 模拟 OpenAI 的 ChatGPT API 客户端。
- 使用系统剪贴板发送和接收消息。
- 提供通过剪贴板进行 LLM 调用的中间件。

## 需求

- Python 3.x
- `clipboard` 模块（可通过以下命令安装）：

  ```bash
  pip install clipboard
  ```

## 安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

2. 安装所需的 Python 包：

   ```bash
   pip install clipboard
   ```

## 使用方法

直接运行脚本：

```bash
python copy_api_gpt.py
```

默认情况下，脚本将：

- 向模拟的 API 发送用户消息“讲个笑话”。
- 通过剪贴板等待响应。
- 打印响应内容。

## 工作原理

脚本执行以下步骤：

1. **将提示信息复制到剪贴板**：用户提示和系统提示（如果有）被组合并复制到剪贴板。

2. **等待响应**：脚本持续检查剪贴板的变化。当检测到变化（表示响应已被放置在剪贴板中）时，检索响应。

3. **模拟 API 客户端**：`MyOpenaiClient` 类模拟 OpenAI 的 API 客户端的行为，允许您使用与实际 API 相同的方法调用（`chat.completions.create`）。

## 自定义

您可以修改脚本以更改提示或添加其他功能：

- **更改提示**：修改 `__main__` 部分中的 `messages` 变量。

  ```python
  messages = [{"role": "user", "content": "在此处输入您的自定义提示"}]
  ```

- **添加系统提示**：可以通过修改 `my_llm_call` 函数中的 `system_prompt` 参数来包含系统提示。

## 示例

以下是如何修改脚本以提出不同的问题：

```python
if __name__ == '__main__':
    messages = [{"role": "user", "content": "请解释量子力学的基本原理。"}]
    client_ = MyOpenaiClient()
    response = client_.chat.completions.create(
        model="random",
        messages=messages)
    res = response.choices[0].message.content
    print(res)
```

## 许可证

此项目基于 MIT 许可证 - 有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 致谢

- 感谢 OpenAI 的 GPT 模型和 API 的启发。
- 使用了 `clipboard` Python 模块进行剪贴板交互。

## 联系方式

如有疑问或建议，请提交 Issue。
