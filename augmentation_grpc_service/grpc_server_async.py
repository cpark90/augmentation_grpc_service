import asyncio
import time
from concurrent import futures

from grpc import aio


class GrpcServerAsync(object):
    
    def __init__(self, max_workers=10, listen_addr='[::]:50051'):
        self.server = aio.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        self.server.add_insecure_port(listen_addr)
        self._listen_addr = listen_addr
        self._key = None
    
    async def serve(self) -> None:
        await self.server.start()
        await self.server.wait_for_termination()