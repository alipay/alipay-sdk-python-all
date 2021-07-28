#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishMenuQueryModel(object):

    def __init__(self):
        self._cook_name = None

    @property
    def cook_name(self):
        return self._cook_name

    @cook_name.setter
    def cook_name(self, value):
        self._cook_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cook_name:
            if hasattr(self.cook_name, 'to_alipay_dict'):
                params['cook_name'] = self.cook_name.to_alipay_dict()
            else:
                params['cook_name'] = self.cook_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishMenuQueryModel()
        if 'cook_name' in d:
            o.cook_name = d['cook_name']
        return o


