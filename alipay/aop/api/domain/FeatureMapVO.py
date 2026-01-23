#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FeatureMapVO(object):

    def __init__(self):
        self._nutritional_prop = None

    @property
    def nutritional_prop(self):
        return self._nutritional_prop

    @nutritional_prop.setter
    def nutritional_prop(self, value):
        self._nutritional_prop = value


    def to_alipay_dict(self):
        params = dict()
        if self.nutritional_prop:
            if hasattr(self.nutritional_prop, 'to_alipay_dict'):
                params['nutritional_prop'] = self.nutritional_prop.to_alipay_dict()
            else:
                params['nutritional_prop'] = self.nutritional_prop
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FeatureMapVO()
        if 'nutritional_prop' in d:
            o.nutritional_prop = d['nutritional_prop']
        return o


