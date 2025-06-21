
gemini_api_keys = [ "AIzaSyDSrXRe6IcDVUiEVaNlE-N-BQ487z3tCF0", "AIzaSyBHM_nqSP14jO0fgCdTMXuNUgmTfUAVC0A", "AIzaSyBGu1ISipjjAY2ZdT7fkYvt52nG8y42DDg", "AIzaSyBYFf1fIy0P2YhUeXh-sDoAi_aANGT_Skc", "AIzaSyCTDLanehb7lnBSaBYGhOMA5w_sSn_K4RA", "AIzaSyBa5TqQEETmzwjskEIoLcKEfRnJGw3log8", "AIzaSyAAYpzV61bpOQl7myiFC-JfUGOBtXxzakc", "AIzaSyBHM_nqSP14jO0fgCdTMXuNUgmTfUAVC0A", "AIzaSyDXh9nekfpEw0pi4gFqKzcWbNuolQWzZxc", "AIzaSyDT4snF29dv6g5iCGCb_XyjZFLVApKlrN4", "AIzaSyCmLFuMaEjwQIwrpWtNYPQoSr_MGIY5h2c", "AIzaSyAnNZ3SXF88brmF8YLnpuuADb4N3oAjIBE", "AIzaSyCzMgiUf4vnkU3Uh_fhFLnYJeAsdw2M88w",  ]

import asyncio
import aiohttp

req = 0
res = 0

async def fetch(url, session):
    async with session.get(url) as response:
        global req, res
        req += 1
        print(req, res)
        result = await response.text()
        res += 1
        print(req, res)
        return result

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            await asyncio.sleep(0.5)
            tasks.append(asyncio.create_task(fetch(url, session)))
        return await asyncio.gather(*tasks)

urls = [
    'https://422qp817ae.execute-api.us-east-1.amazonaws.com/fetch?auth=' + x
    for x
    in gemini_api_keys * 3
    # in gemini_api_keys[:1]
]

results = asyncio.run(fetch_all(urls))

print(results)