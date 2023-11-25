import asyncio
from snake import tick, running

# Do init here
# Load any assets right now to avoid lag at runtime or network errors.

async def main():
    global running

    while running:

        tick()

        await asyncio.sleep(0)  # Very important, and keep it 0

# This is the program entry point:
asyncio.run(main())