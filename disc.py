# -*- coding: utf-8 -*-
import requests
from lxml import html

class Disc:

    def __init__(self, termo):
        self.termo = termo

    def crawl(self):

        # Page
        page = requests.get("https://www.dac.unicamp.br/portal/busca?q="+self.termo)

        tree = html.fromstring(page.content)
        
        disc = tree.xpath("//h4[@class='ss-result__title']//a/@href")

        if not disc:
            return "error"

        disc_url = None
        for url in disc:
            if url.find("caderno-de-horarios") > 0:
                disc_url = url
                break

        if disc_url == None:
            return "error"

        # Disc
        page_disc = requests.get(disc)

        tree = html.fromstring(page_disc.content)

        cred = tree.xpath("//div[@class='row disciplina']//span[@class='label label-primary']/text()")
        ementa = tree.xpath("//div[@class='row disciplina']//div[class='col-md-6']//p/text()").extract()[1]
        

        return (cred, ementa)


if __name__ == "__main__":
    a = Disc("MC102")
    a.crawl()
