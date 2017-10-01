# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class BacalaureatEduRoItem(Item):
    an = Field()
    judet = Field()
    nume = Field()
    url = Field()
    pozitia_pe_judet = Field()
    pozitia_pe_tara = Field()
    unitate_de_invatamant = Field()
    promotie_anterioara = Field()
    forma_invatamant = Field()
    specializare = Field()

    lb_romana_oral = Field()
    lb_romana_scris = Field()
    lb_romana_contestatie = Field()
    lb_romana_final = Field()

    lb_materna = Field()
    lb_materna_oral = Field()
    lb_materna_scris = Field()
    lb_materna_contestatie = Field()
    lb_materna_final = Field()

    lb_moderna = Field()
    lb_moderna_oral = Field()

    disciplina_obligatorie_scris = Field()
    disciplina_obligatorie_scris_nota = Field()
    disciplina_obligatorie_scris_contestatie = Field()
    disciplina_obligatorie_scris_final = Field()

    disciplina_alegere_aria_culiculara = Field()
    disciplina_alegere_aria_culiculara_nota = Field()
    disciplina_alegere_aria_culiculara_contestatie = Field()
    disciplina_alegere_aria_culiculara_final = Field()


    disciplina_alegere_celelalte_arii_culiculare = Field()
    disciplina_alegere_celelalte_arii_culiculare_nota = Field()
    disciplina_alegere_celelalte_arii_culiculare_contestatie = Field()
    disciplina_alegere_celelalte_arii_culiculare_final = Field()

    competente_digitale = Field()

    media = Field()
    rezultat = Field()