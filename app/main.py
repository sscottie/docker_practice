# -*- coding: utf-8 -*-

from sanic.server import AsyncioServer, logger
from sanic.response import text
from sanic import Sanic
import typing as t
import asyncio
import os

app = Sanic("LoadBalancedApp")
APP_NAME = os.getenv("APP_NAME")


@app.route("/")
async def root(request):
    return text(body=f"Hi there! I am a {APP_NAME} instance.")


@app.route("/ping")
async def ping(request):
    return text(body="OK")


def serve() -> t.Awaitable[AsyncioServer]:
    logger.info("Starting")
    return app.create_server(host="127.0.0.1", port=8080, return_asyncio_server=True)


async def main():
    server = await serve()
    if APP_NAME == "fallback":
        await server.serve_forever()
    elif APP_NAME == "main":
        while True:
            await asyncio.sleep(5)
            logger.info("Stopping")
            await server.close()
            await asyncio.sleep(5)
            server = await serve()
    else:
        raise ValueError("APP_NAME variable may be set to 'main' or 'fallback' only")

if __name__ == "__main__":
    asyncio.run(main())