# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
from bs4 import BeautifulSoup as soup
import re
from bacalaureat_edu_ro.items import EvaluareEduRoItem
import base64


county_map = {
    1: "ALBA",
    # 2: "ARGES",
    # 3: "ARAD",
    # 5: "BACAU",
    # 6: "BIHOR",
    # 7: "BISTRITA-NASAUD",
    # 8: "BRAILA",
    # 10: "BRASOV",
    # 9: "BOTOSANI",
    # 11: "BUZAU",
    # 12: "CLUJ",
    # 13: "CALARASI",
    # 14: "CARAS-SEVERIN",
    # 15: "CONSTANTA",
    # 16: "COVASNA",
    # 17: "DAMBOVITA",
    # 18: "DOLJ",
    # 19: "GORJ",
    # 20: "GALATI",
    # 21: "GIURGIU",
    # 22: "HUNEDOARA",
    # 23: "HARGHITA",
    # 25: "IALOMITA",
    # 26: "IASI",
    # 27: "MEHEDINTI",
    # 28: "MARAMURES",
    # 29: "MURES",
    # 30: "NEAMT",
    # 31: "OLT",
    # 32: "PRAHOVA",
    # 33: "SIBIU",
    # 34: "SALAJ",
    # 35: "SATU-MARE",
    # 36: "SUCEAVA",
    # 37: "TULCEA",
    # 38: "TIMIS",
    # 39: "TELEORMAN",
    # 40: "VALCEA",
    # 41: "VRANCEA",
    # 42: "VASLUI",
    # 24: "ILFOV",
    # 4: "BUCURESTI",
}

county_map_acro = {
    "AB": "ALBA",
    # "AG": "ARGES",
    # "AR": "ARAD",
    # "BC": "BACAU",
    # "BH": "BIHOR",
    # "BN": "BISTRITA-NASAUD",
    # "BR": "BRAILA",
    # "BV": "BRASOV",
    # "BT": "BOTOSANI",
    # "BZ": "BUZAU",
    # "CJ": "CLUJ",
    # "CL": "CALARASI",
    # "CS": "CARAS-SEVERIN",
    # "CT": "CONSTANTA",
    # "CV": "COVASNA",
    # "DB": "DAMBOVITA",
    # "DJ": "DOLJ",
    # "GJ": "GORJ",
    # "GL": "GALATI",
    # "GR": "GIURGIU",
    # "HD": "HUNEDOARA",
    # "HR": "HARGHITA",
    # "IL": "IALOMITA",
    # "IS": "IASI",
    # "MH": "MEHEDINTI",
    # "MM": "MARAMURES",
    # "MS": "MURES",
    # "NT": "NEAMT",
    # "OT": "OLT",
    # "PH": "PRAHOVA",
    # "SB": "SIBIU",
    # "SJ": "SALAJ",
    # "SM": "SATU-MARE",
    # "SV": "SUCEAVA",
    # "TL": "TULCEA",
    # "TM": "TIMIS",
    # "TR": "TELEORMAN",
    # "VL": "VALCEA",
    # "VN": "VRANCEA",
    # "VS": "VASLUI",
    # "IF": "ILFOV",
    # "B": "BUCURESTI"
}

class EvaluareSpider(scrapy.Spider):
    name = 'evaluare'
    allowed_domains = ['evaluare.edu.ro']
    start_urls = []

    def __init__(self, year=None):
        if year:
            self.year = int(year)
        else:
            self.year = datetime.now().year



    def start_requests(self):

        if self.year == 2017:
            for county_i, county_name in county_map.items():
                url = 'http://evaluare.edu.ro/Evaluare/CandFromJudAlfa.aspx?Jud={}&PageN=1'.format(county_i)
                yield scrapy.Request(
                    url=url,
                    callback=self.parse,
                    meta={'county': county_name, 'county_i': county_i, 'current_page': 1})
        else:

            for county_i, county_name in county_map_acro.items():
                url = 'http://static.evaluare.edu.ro/{}/rapoarte/j/{}/cand/a/page_1.html'.format(self.year, county_i)
                yield scrapy.Request(
                    url=url,
                    callback=self.parse,
                    meta={'county': county_name, 'county_i': county_i, 'current_page': 1})

    def parse(self, response):
        root = soup(response.body, 'html.parser')
        print('--------')
        print(response.url)
        county_i = response.meta['county_i']
        county = response.meta['county']
        current_page = response.meta['current_page']

        tabel = root.find('table', {'class': 'mainTable'})
        stop_crawl = True if len(tabel.find_all('tr')) == 2 else False


        for elev in tabel.find_all('tr')[2:]:
            td_elev = elev.find_all('td')
            item = EvaluareEduRoItem()
            item['an'] = self.year
            item['judet'] = county
            item['nume'] = td_elev[1].text
            item['url'] = response.url
            item['pozitia_pe_tara'] = td_elev[2].text
            item['unitate_de_invatamant'] = td_elev[3].text
            item['lb_romana_nota'] = td_elev[4].text
            item['lb_romana_contestatie'] = td_elev[5].text
            item['lb_romana_final'] = td_elev[6].text
            item['matematica_nota'] = td_elev[7].text
            item['matematica_contestatie'] = td_elev[8].text
            item['matematica_final'] = td_elev[9].text
            item['lb_materna'] = td_elev[10].text
            item['lb_materna_nota'] = td_elev[11].text
            item['lb_materna_contestatie'] = td_elev[12].text
            item['lb_materna_final'] = td_elev[13].text
            item['media'] = td_elev[14].text
            # yield item
        if self.year == 20017:
            if not stop_crawl:
                next_page = root.find('input', attrs={'title': 'Pagina următoare'})
                next_url = 'http://evaluare.edu.ro/Evaluare/CandFromJudAlfa.aspx?Jud={}&PageN={}'.format(county_i, current_page+1)
                # if current_page < 5:
                # yield scrapy.Request(
                #     url=next_url,
                #     callback=self.parse,
                #     meta={'county': county, 'county_i': county_i, 'current_page': current_page+1})
        else:
            first_script = root.find('script').text
            regex = r".*noOfPages=(\d+)"
            no_of_pages = int(re.findall(regex, first_script)[0])
            if current_page < no_of_pages:
                next_url = 'http://static.evaluare.edu.ro/{}/rapoarte/j/{}/cand/a/page_{}.html'.format(self.year, county_i, current_page)
                # yield scrapy.Request(
                #     url=next_url,
                #     callback=self.parse,
                #     meta={'county': county, 'county_i': county_i, 'current_page': current_page})


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
