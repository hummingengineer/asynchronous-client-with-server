import aiohttp
import asyncio

async def asynchronous_request(url: str, method: str, params: dict = None, json: dict = None):
    async with aiohttp.request(url=url, method=method, params=params, json=json) as res:
        if res.status == 200:
            print(await res.json())
        else:
            print(await res.text())

if __name__ == '__main__':
    protocol = 'your_protocol'
    domain = 'your_domain'
    port = 'your_port'
    path = 'your_path'
    req_url = f'{protocol}://{domain}:{port}/{path}'

    http_request_method = 'your_http_request_method'

    payload = {
        'title': 'Lorem',
        'content': 'ipsum dolor sit amet'
    }

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asynchronous_request(url=req_url, method=http_request_method, json=payload))
