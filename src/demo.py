import chainlit as cl


@cl.step
def tool(message: str):
    # ユーザーのメッセージに基づいて応答を生成
    if "こんにちは" in message:
        return "こんにちは！今日はどのようにお手伝いできますか？"
    elif "ありがとう" in message:
        return "どういたしまして！他に何かお手伝いできることはありますか？"
    else:
        return f"あなたのメッセージに応答します: {message}"


@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    """
    ユーザーがUIにメッセージを入力するたびに呼び出される関数。
    ツールからの応答を取得し、それをユーザーに送信します。
    Args:
        message: ユーザーのメッセージ。
    Returns:
        None.
    """

    # ツールを呼び出して応答を取得
    with cl.Step() as step:
        tool_response = tool(message.content)
    
    # ツールからの応答を送信
    await cl.Message(content=tool_response).send()

    # 最終的な回答を送信
    final_response = "会話を続けましょう！他に何か質問がありますか？"
    await cl.Message(content=final_response).send()