import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        for name,url,w,h in [("region","/cote-d-azur/",1280,0),("iti","/cote-d-azur/3-jours/",1280,0),("mobest","/cote-d-azur/massif-de-l-esterel/",390,0)]:
            pg=await b.new_page(viewport={"width":w,"height":900})
            errs=[]; pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
            await pg.goto("http://localhost:8765"+url); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"/tmp/{name}.png",full_page=True)
            print(name,errs)
        await b.close()
asyncio.run(main())
