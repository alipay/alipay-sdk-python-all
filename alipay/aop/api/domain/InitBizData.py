#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InitBizData(object):

    def __init__(self):
        self._un_valid_prods = None

    @property
    def un_valid_prods(self):
        return self._un_valid_prods

    @un_valid_prods.setter
    def un_valid_prods(self, value):
        self._un_valid_prods = value


    def to_alipay_dict(self):
        params = dict()
        if self.un_valid_prods:
            if hasattr(self.un_valid_prods, 'to_alipay_dict'):
                params['un_valid_prods'] = self.un_valid_prods.to_alipay_dict()
            else:
                params['un_valid_prods'] = self.un_valid_prods
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InitBizData()
        if 'un_valid_prods' in d:
            o.un_valid_prods = d['un_valid_prods']
        return o


