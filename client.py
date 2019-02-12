#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set filencodding =utf8 :



from urllib.request import urllib3
import bs4


class Clientweb(object):
  """Client web per la web de la eps"""
  def __init__(self):
      super(Clientweb, self). __init__()

  def descarregar_html(self):
      f = urlopen("http://www.eps.udl.cat/cat/")
      html = f.read()
      f.close()
      return html

  def buscar_activitats(self, html):
      arbre = bs4.BeautifulSoup(html)
      activitats = arbre.find_all("div","featured-links-item")
      return activitats

  def run(self):
      htmsl = self.descarregar_html()
      activitats = self.buscar_activitats(html)
      print(html)

if __name__ == "__main__":
  c= Clientweb()
  c.run()
