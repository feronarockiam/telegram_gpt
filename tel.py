import openai
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='5954457249:AAGPuWzfnEBY92lPWbjZUsLkHlmxeg0_7QY')
dp = Dispatcher(bot)

openai.api_key = "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"

@dp.message_handler(commands = ["start","help"])
async def welcome(message: types.Message):
    await message.reply("Hi! I am Scrappy.Ai! Ask me something...")

@dp.message_handler()
async def gpt(message:types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        max_tokens=1024,
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    await message.reply(response.choices[0].text)


if __name__ == "__main__":
    executor.start_polling(dp)