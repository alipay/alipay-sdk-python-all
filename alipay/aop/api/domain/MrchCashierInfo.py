#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MrchCashierInfo(object):

    def __init__(self):
        self._cashier_id = None
        self._cashier_name = None
        self._phone_no = None
        self._shop_id = None

    @property
    def cashier_id(self):
        return self._cashier_id

    @cashier_id.setter
    def cashier_id(self, value):
        self._cashier_id = value
    @property
    def cashier_name(self):
        return self._cashier_name

    @cashier_name.setter
    def cashier_name(self, value):
        self._cashier_name = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cashier_id:
            if hasattr(self.cashier_id, 'to_alipay_dict'):
                params['cashier_id'] = self.cashier_id.to_alipay_dict()
            else:
                params['cashier_id'] = self.cashier_id
        if self.cashier_name:
            if hasattr(self.cashier_name, 'to_alipay_dict'):
                params['cashier_name'] = self.cashier_name.to_alipay_dict()
            else:
                params['cashier_name'] = self.cashier_name
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
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
        o = MrchCashierInfo()
        if 'cashier_id' in d:
            o.cashier_id = d['cashier_id']
        if 'cashier_name' in d:
            o.cashier_name = d['cashier_name']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


