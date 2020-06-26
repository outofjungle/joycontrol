import asyncio
from aioconsole import ainput
from joycontrol.controller_state import ControllerState, button_push

async def run(controller_state: ControllerState):
    user_input = asyncio.ensure_future(
        ainput(prompt='Running plugin... Press <enter> to stop.')
    )

    async def press_a():
        await button_push(controller_state, 'a', sec=1)
        await asyncio.sleep(0.1)

    while not user_input.done():
        await press_a()

    await user_input