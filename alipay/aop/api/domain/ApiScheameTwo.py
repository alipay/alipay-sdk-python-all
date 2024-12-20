#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApiScheameTwo(object):

    def __init__(self):
        self._card_name = None

    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApiScheameTwo()
        if 'card_name' in d:
            o.card_name = d['card_name']
        return o


