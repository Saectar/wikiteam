# -*- coding: utf-8 -*-
"""
This family file was auto-generated by $Id: generate_family_file.py 9734 2011-11-09 22:17:11Z valhallasw $
Configuration parameters:
  url = http://speedydeletion.wikia.com
  name = speedydeletion

Please do not commit this to the SVN repository!
"""

import family

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'wikivoyage-speedydeletion'
        self.langs = {
            'en': u'wikivoyage-speedydeletion.wikia.com',
        }

        self.namespaces[4] = self.namespaces.get(4, {})
        self.namespaces[4]['en'] = [u'Speedy deletion Wiki']
        self.namespaces[5] = self.namespaces.get(5, {})
        self.namespaces[5]['en'] = [u'Speedy deletion Wiki talk']
        self.namespaces[6] = self.namespaces.get(6, {})
        self.namespaces[6]['en'] = [u'Video', u'Image']
        self.namespaces[7] = self.namespaces.get(7, {})
        self.namespaces[7]['en'] = [u'Video talk', u'Image talk']
        self.namespaces[1100] = self.namespaces.get(1100, {})
        self.namespaces[1100]['en'] = [u'RelatedVideos']
        self.namespaces[110] = self.namespaces.get(110, {})
        self.namespaces[110]['en'] = [u'Forum']
        self.namespaces[111] = self.namespaces.get(111, {})
        self.namespaces[111]['en'] = [u'Forum talk']
        self.namespaces[1200] = self.namespaces.get(1200, {})
        self.namespaces[1200]['en'] = [u'Message Wall']
        self.namespaces[1201] = self.namespaces.get(1201, {})
        self.namespaces[1201]['en'] = [u'Thread']
        self.namespaces[1202] = self.namespaces.get(1202, {})
        self.namespaces[1202]['en'] = [u'Message Wall Greeting']
        self.namespaces[500] = self.namespaces.get(500, {})
        self.namespaces[500]['en'] = [u'User blog']
        self.namespaces[501] = self.namespaces.get(501, {})
        self.namespaces[501]['en'] = [u'User blog comment']
        self.namespaces[502] = self.namespaces.get(502, {})
        self.namespaces[502]['en'] = [u'Blog']
        self.namespaces[503] = self.namespaces.get(503, {})
        self.namespaces[503]['en'] = [u'Blog talk']


    def scriptpath(self, code):
        return {
            'en': u'',
        }[code]

    def version(self, code):
        return {
            'en': u'1.16.5',
        }[code]