import asyncio
from aioconsole import ainput
from joycontrol.controller_state import ControllerState, button_push

async def run(controller_state: ControllerState):
    stick = controller_state.l_stick_state
    
    user_input = asyncio.ensure_future(
        ainput(prompt='Running plugin... Press <enter> to stop.')
    )

    async def press_a():
        await button_push(controller_state, 'a')
        await asyncio.sleep(0.3)

    speed = 0x100
    stick.set_center()
 
    centerH = stick.get_h()
    centerV = stick.get_v()
    move_path = ((-1, 0), (0, -1), (1, 0), (0, 1))

    while not user_input.done():
        for direction in move_path:
            # move
            stick.set_h(centerH + (speed * direction[0]))
            stick.set_v(centerV + (speed * direction[1]))
            await asyncio.sleep(5)
            stick.set_center()

            # press a
            await press_a()

            if user_input.done():
                break
            else:
                continue

    await user_input