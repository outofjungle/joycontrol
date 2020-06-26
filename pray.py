import asyncio
from aioconsole import ainput
from joycontrol.controller_state import ControllerState, button_push
from datetime import datetime, timedelta

async def run(controller_state: ControllerState):
    user_input = asyncio.ensure_future(
        ainput(prompt='Running plugin... Press <enter> to stop.')
    )

    async def press_a():
        await button_push(controller_state, 'a')
        await asyncio.sleep(0.3)

    now = datetime.now()
    stop_at = now.replace(hour=4, minute=50, second=0, microsecond=0)
    if stop_at < now:
        stop_at = stop_at + timedelta(days=1)

    while not user_input.done():
        await press_a()
        now = datetime.now()
        if stop_at < now:
            break

    await user_input
