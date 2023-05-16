from prisma import Prisma


class PrismaConnection:
    """Open and close connection to PrismaORM, that connect to database"""

    def __init__(self):
        self.client = Prisma(auto_register=True)
        self.connected = False

    async def connect(self):
        if self.connected:
            return self.client
        await self.client.connect()
        self.connected = True
        return self.client

    async def disconnect(self):
        if not self.connected:
            return self.client
        await self.client.disconnect()
        self.connected = False
        return self.client
