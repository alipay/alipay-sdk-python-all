#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AllergyHistory(object):

    def __init__(self):
        self._allergen = None

    @property
    def allergen(self):
        return self._allergen

    @allergen.setter
    def allergen(self, value):
        self._allergen = value


    def to_alipay_dict(self):
        params = dict()
        if self.allergen:
            if hasattr(self.allergen, 'to_alipay_dict'):
                params['allergen'] = self.allergen.to_alipay_dict()
            else:
                params['allergen'] = self.allergen
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AllergyHistory()
        if 'allergen' in d:
            o.allergen = d['allergen']
        return o


