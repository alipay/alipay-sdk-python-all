#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompanyOverviewHighLight(object):

    def __init__(self):
        self._high_light_text = None

    @property
    def high_light_text(self):
        return self._high_light_text

    @high_light_text.setter
    def high_light_text(self, value):
        self._high_light_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.high_light_text:
            if hasattr(self.high_light_text, 'to_alipay_dict'):
                params['high_light_text'] = self.high_light_text.to_alipay_dict()
            else:
                params['high_light_text'] = self.high_light_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyOverviewHighLight()
        if 'high_light_text' in d:
            o.high_light_text = d['high_light_text']
        return o


