#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppUpdattestBatchqueryModel(object):

    def __init__(self):
        self._campus_card = None
        self._s = None

    @property
    def campus_card(self):
        return self._campus_card

    @campus_card.setter
    def campus_card(self, value):
        self._campus_card = value
    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value


    def to_alipay_dict(self):
        params = dict()
        if self.campus_card:
            if hasattr(self.campus_card, 'to_alipay_dict'):
                params['campus_card'] = self.campus_card.to_alipay_dict()
            else:
                params['campus_card'] = self.campus_card
        if self.s:
            if hasattr(self.s, 'to_alipay_dict'):
                params['s'] = self.s.to_alipay_dict()
            else:
                params['s'] = self.s
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppUpdattestBatchqueryModel()
        if 'campus_card' in d:
            o.campus_card = d['campus_card']
        if 's' in d:
            o.s = d['s']
        return o


