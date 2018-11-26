#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosPaymodeDeleteModel(object):

    def __init__(self):
        self._pay_name = None
        self._shop_id = None
        self._system = None

    @property
    def pay_name(self):
        return self._pay_name

    @pay_name.setter
    def pay_name(self, value):
        self._pay_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, value):
        self._system = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_name:
            if hasattr(self.pay_name, 'to_alipay_dict'):
                params['pay_name'] = self.pay_name.to_alipay_dict()
            else:
                params['pay_name'] = self.pay_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.system:
            if hasattr(self.system, 'to_alipay_dict'):
                params['system'] = self.system.to_alipay_dict()
            else:
                params['system'] = self.system
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosPaymodeDeleteModel()
        if 'pay_name' in d:
            o.pay_name = d['pay_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'system' in d:
            o.system = d['system']
        return o


