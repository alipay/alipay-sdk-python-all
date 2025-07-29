#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchWord(object):

    def __init__(self):
        self._bidword = None
        self._match_type = None
        self._price = None

    @property
    def bidword(self):
        return self._bidword

    @bidword.setter
    def bidword(self, value):
        self._bidword = value
    @property
    def match_type(self):
        return self._match_type

    @match_type.setter
    def match_type(self, value):
        self._match_type = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.bidword:
            if hasattr(self.bidword, 'to_alipay_dict'):
                params['bidword'] = self.bidword.to_alipay_dict()
            else:
                params['bidword'] = self.bidword
        if self.match_type:
            if hasattr(self.match_type, 'to_alipay_dict'):
                params['match_type'] = self.match_type.to_alipay_dict()
            else:
                params['match_type'] = self.match_type
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchWord()
        if 'bidword' in d:
            o.bidword = d['bidword']
        if 'match_type' in d:
            o.match_type = d['match_type']
        if 'price' in d:
            o.price = d['price']
        return o


