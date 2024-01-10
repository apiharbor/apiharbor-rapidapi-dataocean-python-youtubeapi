import asyncio
import aiohttp

from urllib.parse import urlencode
from purl import URL

from .schemas.channel_details import ChannelDetails


class YouTubeChannelDetailsApiClient(object):
    def __init__(self, rapid_api_key: str):
        self.rapidapi_host = 'the-better-youtube-channel-details.p.rapidapi.com'
        self.headers = {
            "X-RapidAPI-Key": rapid_api_key,
            "X-RapidAPI-Host": self.rapidapi_host,
        }

    async def get_channel_details(self, urlOrUsername) -> any:
        response = await self.__get_request("/GetChannelDetails", urlencode({'urlOrUsername': urlOrUsername}))
        return ChannelDetails.model_validate(response)

    async def __get_request(self, path: str, query: dict) -> str:
        url = URL(
            host=self.rapidapi_host,
            path=path,
            query=query,
            scheme="https"
        ).as_string()

        session_timeout = aiohttp.ClientTimeout(total=45.0)
        is_ok = False

        while True:
            async with aiohttp.ClientSession(headers=self.headers, timeout=session_timeout) as session:
                async with session.get(url=url) as response:
                    try:
                        json_response = await response.json()  
                        if response.status == 200:  
                            is_ok = True
                    except aiohttp.client.ContentTypeError:
                        continue
                    if is_ok:
                        break
            await asyncio.sleep(0.3)

        return json_response
    