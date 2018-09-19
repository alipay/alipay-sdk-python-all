#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiscountInfos(object):

    def __init__(self):
        self._amount = None
        self._ext_infos = None
        self._mdiscount_amount = None
        self._name = None
        self._platform_discount_amount = None
        self._type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def mdiscount_amount(self):
        return self._mdiscount_amount

    @mdiscount_amount.setter
    def mdiscount_amount(self, value):
        self._mdiscount_amount = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def platform_discount_amount(self):
        return self._platform_discount_amount

    @platform_discount_amount.setter
    def platform_discount_amount(self, value):
        self._platform_discount_amount = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.mdiscount_amount:
            if hasattr(self.mdiscount_amount, 'to_alipay_dict'):
                params['mdiscount_amount'] = self.mdiscount_amount.to_alipay_dict()
            else:
                params['mdiscount_amount'] = self.mdiscount_amount
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.platform_discount_amount:
            if hasattr(self.platform_discount_amount, 'to_alipay_dict'):
                params['platform_discount_amount'] = self.platform_discount_amount.to_alipay_dict()
            else:
                params['platform_discount_amount'] = self.platform_discount_amount
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountInfos()
        if 'amount' in d:
            o.amount = d['amount']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'mdiscount_amount' in d:
            o.mdiscount_amount = d['mdiscount_amount']
        if 'name' in d:
            o.name = d['name']
        if 'platform_discount_amount' in d:
            o.platform_discount_amount = d['platform_discount_amount']
        if 'type' in d:
            o.type = d['type']
        return o


