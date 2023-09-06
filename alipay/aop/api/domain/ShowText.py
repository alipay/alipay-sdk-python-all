#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShowText(object):

    def __init__(self):
        self._meal_desc = None

    @property
    def meal_desc(self):
        return self._meal_desc

    @meal_desc.setter
    def meal_desc(self, value):
        self._meal_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.meal_desc:
            if hasattr(self.meal_desc, 'to_alipay_dict'):
                params['meal_desc'] = self.meal_desc.to_alipay_dict()
            else:
                params['meal_desc'] = self.meal_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShowText()
        if 'meal_desc' in d:
            o.meal_desc = d['meal_desc']
        return o


