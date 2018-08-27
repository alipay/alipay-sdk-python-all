#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignResultValue(object):

    def __init__(self):
        self._effect_biz_value = None

    @property
    def effect_biz_value(self):
        return self._effect_biz_value

    @effect_biz_value.setter
    def effect_biz_value(self, value):
        self._effect_biz_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.effect_biz_value:
            if hasattr(self.effect_biz_value, 'to_alipay_dict'):
                params['effect_biz_value'] = self.effect_biz_value.to_alipay_dict()
            else:
                params['effect_biz_value'] = self.effect_biz_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignResultValue()
        if 'effect_biz_value' in d:
            o.effect_biz_value = d['effect_biz_value']
        return o


