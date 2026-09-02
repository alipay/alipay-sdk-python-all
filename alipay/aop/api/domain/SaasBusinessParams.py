#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaasBusinessParams(object):

    def __init__(self):
        self._campus_card = None

    @property
    def campus_card(self):
        return self._campus_card

    @campus_card.setter
    def campus_card(self, value):
        self._campus_card = value


    def to_alipay_dict(self):
        params = dict()
        if self.campus_card:
            if hasattr(self.campus_card, 'to_alipay_dict'):
                params['campus_card'] = self.campus_card.to_alipay_dict()
            else:
                params['campus_card'] = self.campus_card
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaasBusinessParams()
        if 'campus_card' in d:
            o.campus_card = d['campus_card']
        return o


