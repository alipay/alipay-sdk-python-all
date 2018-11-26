#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosPaymodesortModifyModel(object):

    def __init__(self):
        self._pay_names = None
        self._shop_id = None

    @property
    def pay_names(self):
        return self._pay_names

    @pay_names.setter
    def pay_names(self, value):
        if isinstance(value, list):
            self._pay_names = list()
            for i in value:
                self._pay_names.append(i)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_names:
            if isinstance(self.pay_names, list):
                for i in range(0, len(self.pay_names)):
                    element = self.pay_names[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_names[i] = element.to_alipay_dict()
            if hasattr(self.pay_names, 'to_alipay_dict'):
                params['pay_names'] = self.pay_names.to_alipay_dict()
            else:
                params['pay_names'] = self.pay_names
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosPaymodesortModifyModel()
        if 'pay_names' in d:
            o.pay_names = d['pay_names']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


