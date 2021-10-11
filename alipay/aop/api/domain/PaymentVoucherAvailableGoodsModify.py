#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentVoucherAvailableGoodsModify(object):

    def __init__(self):
        self._goods_ids = None

    @property
    def goods_ids(self):
        return self._goods_ids

    @goods_ids.setter
    def goods_ids(self, value):
        if isinstance(value, list):
            self._goods_ids = list()
            for i in value:
                self._goods_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.goods_ids:
            if isinstance(self.goods_ids, list):
                for i in range(0, len(self.goods_ids)):
                    element = self.goods_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_ids[i] = element.to_alipay_dict()
            if hasattr(self.goods_ids, 'to_alipay_dict'):
                params['goods_ids'] = self.goods_ids.to_alipay_dict()
            else:
                params['goods_ids'] = self.goods_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentVoucherAvailableGoodsModify()
        if 'goods_ids' in d:
            o.goods_ids = d['goods_ids']
        return o


