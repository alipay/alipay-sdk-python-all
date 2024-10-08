#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceExtInfo(object):

    def __init__(self):
        self._promo_text = None

    @property
    def promo_text(self):
        return self._promo_text

    @promo_text.setter
    def promo_text(self, value):
        self._promo_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.promo_text:
            if hasattr(self.promo_text, 'to_alipay_dict'):
                params['promo_text'] = self.promo_text.to_alipay_dict()
            else:
                params['promo_text'] = self.promo_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceExtInfo()
        if 'promo_text' in d:
            o.promo_text = d['promo_text']
        return o


