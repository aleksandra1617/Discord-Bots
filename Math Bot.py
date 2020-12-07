# TODO: Print instructions for the bot, EXAMPLE: when msg is ->help

import random
from discord.ext import commands

first, second, result = 0, 0, 0


def gen_question():
    global first, second, result
    min_num = 3
    max_num = 100

    first = random.randint(min_num, max_num)
    second = random.randint(min_num, max_num)

    question = "What is %d + %d?" % (first, second)
    result = first + second
    return question


def apply_behaviour():
    # SPECIFY CLIENT
    bot = commands.Bot(command_prefix="->")  # Initialise client

    # COMMAND ON READY (WHEN CONNECTED TO DISCORD)
    @bot.event
    async def on_ready():
        print('Logged in as', bot.user.name)
        print(bot.user.name, " is online and connected to Discord")
        print('------')

    # COMMAND ON MESSAGE (WHEN A PARTICULAR MESSAGE IS HEARD)
    @bot.event
    async def on_message(msg):
        global result

        if msg.content.lower() == "->help":
            msg_to_send = "Commands: [->? (get question), ->=(see answer), ->help, ->'your answer here' (enter answer)]"
            await bot.send_message(msg.channel, msg_to_send)

        elif msg.content.upper() == "->?":
            msg_to_send = gen_question()
            await bot.send_message(msg.channel, msg_to_send)

        elif msg.content.upper() == "->=":
            await bot.send_message(msg.channel, "The answer is %s" % str(result))

        elif msg.content.upper().startswith("->"):  # Needs to be the last 'if' because it will always trigger

            # Find the entered value
            if msg.content[2:].isdigit():

                # Check if the entered value equals the result
                if msg.content[2:] == str(result):
                    await bot.send_message(msg.channel, "Correct, good job.")
                else:
                    await bot.send_message(msg.channel, "Incorrect, try again.")
            else:
                await bot.send_message(msg.channel, "Please enter a number.")

    # Run the bot using it's unique token (login info of the bot)
    bot.run(Token)


apply_behaviour()
