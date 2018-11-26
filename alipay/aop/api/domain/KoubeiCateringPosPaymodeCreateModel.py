#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosPaymodeCreateModel(object):

    def __init__(self):
        self._fixed_amount = None
        self._fixed_switch = None
        self._income_ratio = None
        self._pay_name = None
        self._shop_id = None

    @property
    def fixed_amount(self):
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, value):
        self._fixed_amount = value
    @property
    def fixed_switch(self):
        return self._fixed_switch

    @fixed_switch.setter
    def fixed_switch(self, value):
        self._fixed_switch = value
    @property
    def income_ratio(self):
        return self._income_ratio

    @income_ratio.setter
    def income_ratio(self, value):
        self._income_ratio = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.fixed_amount:
            if hasattr(self.fixed_amount, 'to_alipay_dict'):
                params['fixed_amount'] = self.fixed_amount.to_alipay_dict()
            else:
                params['fixed_amount'] = self.fixed_amount
        if self.fixed_switch:
            if hasattr(self.fixed_switch, 'to_alipay_dict'):
                params['fixed_switch'] = self.fixed_switch.to_alipay_dict()
            else:
                params['fixed_switch'] = self.fixed_switch
        if self.income_ratio:
            if hasattr(self.income_ratio, 'to_alipay_dict'):
                params['income_ratio'] = self.income_ratio.to_alipay_dict()
            else:
                params['income_ratio'] = self.income_ratio
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosPaymodeCreateModel()
        if 'fixed_amount' in d:
            o.fixed_amount = d['fixed_amount']
        if 'fixed_switch' in d:
            o.fixed_switch = d['fixed_switch']
        if 'income_ratio' in d:
            o.income_ratio = d['income_ratio']
        if 'pay_name' in d:
            o.pay_name = d['pay_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


