#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayModeModel(object):

    def __init__(self):
        self._accounting = None
        self._enabled = None
        self._fixed_amount = None
        self._fixed_switch = None
        self._income_ratio = None
        self._pay_code = None
        self._pay_name = None
        self._shop_id = None
        self._sort = None
        self._system = None

    @property
    def accounting(self):
        return self._accounting

    @accounting.setter
    def accounting(self, value):
        self._accounting = value
    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value
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
    def pay_code(self):
        return self._pay_code

    @pay_code.setter
    def pay_code(self, value):
        self._pay_code = value
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
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, value):
        self._system = value


    def to_alipay_dict(self):
        params = dict()
        if self.accounting:
            if hasattr(self.accounting, 'to_alipay_dict'):
                params['accounting'] = self.accounting.to_alipay_dict()
            else:
                params['accounting'] = self.accounting
        if self.enabled:
            if hasattr(self.enabled, 'to_alipay_dict'):
                params['enabled'] = self.enabled.to_alipay_dict()
            else:
                params['enabled'] = self.enabled
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
        if self.pay_code:
            if hasattr(self.pay_code, 'to_alipay_dict'):
                params['pay_code'] = self.pay_code.to_alipay_dict()
            else:
                params['pay_code'] = self.pay_code
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
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
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
        o = PayModeModel()
        if 'accounting' in d:
            o.accounting = d['accounting']
        if 'enabled' in d:
            o.enabled = d['enabled']
        if 'fixed_amount' in d:
            o.fixed_amount = d['fixed_amount']
        if 'fixed_switch' in d:
            o.fixed_switch = d['fixed_switch']
        if 'income_ratio' in d:
            o.income_ratio = d['income_ratio']
        if 'pay_code' in d:
            o.pay_code = d['pay_code']
        if 'pay_name' in d:
            o.pay_name = d['pay_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sort' in d:
            o.sort = d['sort']
        if 'system' in d:
            o.system = d['system']
        return o


