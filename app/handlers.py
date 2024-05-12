from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from openai import AsyncOpenAI

router = Router()

client = AsyncOpenAI(api_key='you_chatgpt_token')

def load_context(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            context = file.read()
            print("Context loaded successfully:")
            print(context)
            return context
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None


context_file = "./context.txt"
context = load_context(context_file)

async def generate_answer(user_message):
    if context:
        full_message = f"{context}\n{user_message}"
    else:
        full_message = user_message
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{full_message}",
            }
        ],
        model="gpt-4",
    )
    return chat_completion.choices[0].message.content

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Hello, 你好！')

@router.message()
async def gpt_answer(message: Message):
    answer = await generate_answer(message.text)
    await message.answer(f'{answer}')



