# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
from bs4 import BeautifulSoup as soup
import re
from bacalaureat_edu_ro.items import BacalaureatEduRoItem
import base64

class BacalaureatSpider(scrapy.Spider):
    name = 'bacalaureat'
    allowed_domains = ['bacalaureat.edu.ro']
    start_urls = []

    def __init__(self, session=None, year=None, ):
        if year:
            self.year = int(year)
        else:
            self.year = datetime.now().year

        if session:
            self.session = int(session)
        else:
            self.session = 1


    def start_requests(self):
        if self.session == 1:
            url = 'http://static.bacalaureat.edu.ro/{}/rapoarte/rezultate/alfabetic/page_1.html'.format(self.year)
        else:
            url = 'http://static.bacalaureat.edu.ro/{}/rapoarte_sept/rezultate/alfabetic/page_1.html'.format(self.year)
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            meta={'year': self.year})

    def parse(self, response):
        root = soup(response.body, 'html.parser')
        if self.year in [2010, 2011, 2012, 2013, 2014, 2015, 2016]:
            regex = r'^.*ged\(\){return \"(.*)\";}'
            ged = re.findall(regex, root.find('script').text)[0]
            dec_ged = base64.b64decode(s3(ged))
            root = soup(dec_ged, 'html.parser')


        tabel = root.find('table', {'id': 'mainTable'})

        row_1 = True
        for elev in tabel.find_all('tr')[2:]:
            td_elev = elev.find_all('td')
            if row_1:
                item = BacalaureatEduRoItem()
                item['an'] = response.meta['year']
                item['url'] = response.url
                item['pozitia_pe_judet'] = td_elev[2].text.replace('\xa0',' ')
                item['pozitia_pe_tara'] = td_elev[3].text.replace('\xa0',' ')
                item['unitate_de_invatamant'] = td_elev[4].text.replace('\xa0',' ')
                item['judet'] = td_elev[5].text.replace('\xa0',' ')
                item['promotie_anterioara'] = td_elev[6].text.replace('\xa0',' ')
                item['forma_invatamant'] = td_elev[7].text.replace('\xa0',' ')
                item['specializare'] = td_elev[8].text.replace('\xa0',' ')
                item['lb_romana_oral'] = td_elev[9].text.replace('\xa0', ' ')
                item['lb_romana_scris'] = td_elev[10].text.replace('\xa0', ' ')
                item['lb_romana_contestatie'] = td_elev[11].text.replace('\xa0', ' ')
                item['lb_romana_final'] = td_elev[12].text.replace('\xa0', ' ')
                item['lb_materna'] = td_elev[13].text.replace('\xa0', ' ')
                item['lb_moderna'] = td_elev[14].text.replace('\xa0', ' ')
                item['lb_moderna_oral'] = td_elev[15].text.replace('\xa0', ' ')
                item['disciplina_obligatorie_scris'] = td_elev[16].text.replace('\xa0', ' ')
                item['disciplina_alegere_aria_culiculara'] = td_elev[17].text.replace('\xa0', ' ')
                if self.year not in [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]:
                    item['disciplina_alegere_celelalte_arii_culiculare'] = td_elev[18].text.replace('\xa0', ' ')
                    if self.year not in [2009]:
                        item['nume'] = td_elev[1].text.strip().replace('\xa0', ' ')
                        item['media'] = td_elev[19].text.replace('\xa0', ' ')
                        item['rezultat'] = td_elev[20].text.replace('\xa0', ' ')
                    else:
                        script_elev = elev.find('script').text
                        regex = '^.*=\"(.*)\";.*=\"(.*)\";.*=\"(.*)\"\;$'
                        elev_decript = re.findall(regex, script_elev)
                        item['nume'] = elev_decript[0][0].replace('<br>', '')
                        item['media'] = elev_decript[0][1]
                        item['rezultat'] = elev_decript[0][2]

                else:
                    item['competente_digitale'] = td_elev[18].text.replace('\xa0', ' ')

                    script_elev = elev.find('script').text
                    regex = '^.*=\"(.*)\";.*=\"(.*)\";.*=\"(.*)\"\;$'
                    elev_decript = re.findall(regex, script_elev)

                    item['nume'] = elev_decript[0][0].replace('<br>', '')
                    item['media'] = elev_decript[0][1]
                    item['rezultat'] = elev_decript[0][2]
                row_1 = False
            else:
                item['lb_materna_oral'] = td_elev[0].text.replace('\xa0', ' ')
                item['lb_materna_scris'] = td_elev[1].text.replace('\xa0', ' ')
                item['lb_materna_contestatie'] = td_elev[2].text.replace('\xa0', ' ')
                item['lb_materna_final'] = td_elev[3].text.replace('\xa0', ' ')
                item['disciplina_obligatorie_scris_nota'] = td_elev[4].text.replace('\xa0', ' ')
                item['disciplina_obligatorie_scris_contestatie'] = td_elev[5].text.replace('\xa0', ' ')
                item['disciplina_obligatorie_scris_final'] = td_elev[6].text.replace('\xa0', ' ')
                item['disciplina_alegere_aria_culiculara_nota'] = td_elev[7].text.replace('\xa0', ' ')
                item['disciplina_alegere_aria_culiculara_contestatie'] = td_elev[8].text.replace('\xa0', ' ')
                item['disciplina_alegere_aria_culiculara_final'] = td_elev[9].text.replace('\xa0', ' ')
                if self.year not in [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]:
                    item['disciplina_alegere_celelalte_arii_culiculare_nota'] = td_elev[10].text.replace('\xa0', ' ')
                    item['disciplina_alegere_celelalte_arii_culiculare_contestatie'] = td_elev[11].text.replace('\xa0', ' ')
                    item['disciplina_alegere_celelalte_arii_culiculare_final'] = td_elev[12].text.replace('\xa0', ' ')
                row_1 = True
                yield item
        first_script = root.find('script').text
        regex = r".*noOfPages=(\d+)"
        no_of_pages = int(re.findall(regex, first_script)[0])
        regex = '.*page_(\d+)'
        current_page = int(re.findall(regex, response.url)[0])
        if current_page < no_of_pages:
            next_url = '{}/page_{}.html'.format('/'.join(response.url.split('/')[:-1]),current_page+1)
            yield scrapy.Request(
                url=next_url,
                callback=self.parse,
                meta={'year': self.year, 'county': item['judet']})


def str_replace(srch, rplc, sbjct):
    if len(sbjct) == 0:
        return ''

    if len(srch) == 1:
        return sbjct.replace(srch[0], rplc[0])

    lst = sbjct.split(srch[0])
    reslst = []
    for s in lst:
        reslst.append(str_replace(s, srch[1:], rplc[1:]))
    return rplc[0].join(reslst)


def s0(a, b, c):
    a = str_replace(b, '_', a)
    a = str_replace(c, b, a)
    a = str_replace('_', c, a)
    return a


def s1(a, b):
    return s0(a, b.lower(), b.upper())


def s2(a):
    for i in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
        a = s1(a, i)
    return a


def s3(a):
    a = s0(a, "0", "O")
    a = s0(a, "1", "l")
    a = s0(a, "5", "S")
    a = s0(a, "m", "s")
    a = s2(a)

    return a
