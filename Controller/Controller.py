class Controller(object):

    async def on_message(self, client, message):
        raise NotImplementedError("No implementation of on_message defined")
