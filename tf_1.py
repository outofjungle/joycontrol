import asyncio
from aioconsole import ainput
from joycontrol.controller_state import ControllerState, button_push

async def run(controller_state: ControllerState):
    stick = controller_state.l_stick_state
    stick.set_center()
    centerH = stick.get_h()
    centerV = stick.get_v()

    # user_input = asyncio.ensure_future(
    #     ainput(prompt='Running plugin... Press <enter> to stop.')
    # )

    async def orient():
        stick.set_v(centerV + 0x400)
        await asyncio.sleep(1)
        stick.set_v(centerV - 0x400)
        await asyncio.sleep(0.99)
        stick.set_center()

    async def press_a():
        await button_push(controller_state, 'a')
        await asyncio.sleep(0.3)

    async def move_right():
        stick.set_v(centerV + 0x400)
        await asyncio.sleep(1)
        stick.set_v(centerV - 0x400)
        await asyncio.sleep(0.99)
        stick.set_center()

    await orient()
    await press_a()
    await orient()

    # await user_input