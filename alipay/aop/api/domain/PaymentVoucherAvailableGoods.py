#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentVoucherAvailableGoods(object):

    def __init__(self):
        self._goods_description = None
        self._goods_ids = None
        self._goods_name = None

    @property
    def goods_description(self):
        return self._goods_description

    @goods_description.setter
    def goods_description(self, value):
        self._goods_description = value
    @property
    def goods_ids(self):
        return self._goods_ids

    @goods_ids.setter
    def goods_ids(self, value):
        if isinstance(value, list):
            self._goods_ids = list()
            for i in value:
                self._goods_ids.append(i)
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_description:
            if hasattr(self.goods_description, 'to_alipay_dict'):
                params['goods_description'] = self.goods_description.to_alipay_dict()
            else:
                params['goods_description'] = self.goods_description
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
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentVoucherAvailableGoods()
        if 'goods_description' in d:
            o.goods_description = d['goods_description']
        if 'goods_ids' in d:
            o.goods_ids = d['goods_ids']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        return o


