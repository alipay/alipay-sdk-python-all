#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailWmsGoodsBatchqueryModel(object):

    def __init__(self):
        self._goods_codes = None

    @property
    def goods_codes(self):
        return self._goods_codes

    @goods_codes.setter
    def goods_codes(self, value):
        if isinstance(value, list):
            self._goods_codes = list()
            for i in value:
                self._goods_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.goods_codes:
            if isinstance(self.goods_codes, list):
                for i in range(0, len(self.goods_codes)):
                    element = self.goods_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_codes[i] = element.to_alipay_dict()
            if hasattr(self.goods_codes, 'to_alipay_dict'):
                params['goods_codes'] = self.goods_codes.to_alipay_dict()
            else:
                params['goods_codes'] = self.goods_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsGoodsBatchqueryModel()
        if 'goods_codes' in d:
            o.goods_codes = d['goods_codes']
        return o


