import multiprocessing

from langchain_community.chat_models import ChatLlamaCpp

llm = ChatLlamaCpp(
    temperature=0.1,
    model_path="./src/guide/Llama-3-ELYZA-JP-8B-q4_k_m.gguf",
    # n_ctx=10000,
    # n_gpu_layers=0,
    # n_batch=300,  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
    # max_tokens=512,
    n_threads=multiprocessing.cpu_count() - 1,
    repeat_penalty=1.5,
    # top_p=0.5,
    verbose=True,
)


def think_response_msg(request_msg):
    messages = [
        (
            "system",
            "あなたは国語の先生です。送られてきた文章に対して、適切な返答をしてください。なお、返事は日本語でお願いします。",
        ),
        ("human", request_msg),
    ]

    return llm.invoke(messages).content
