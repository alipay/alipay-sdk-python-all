#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarVoucherInfo(object):

    def __init__(self):
        self._amount = None
        self._merchant_contribute = None
        self._name = None
        self._other_contribute = None
        self._template_id = None
        self._voucher_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def merchant_contribute(self):
        return self._merchant_contribute

    @merchant_contribute.setter
    def merchant_contribute(self, value):
        self._merchant_contribute = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def other_contribute(self):
        return self._other_contribute

    @other_contribute.setter
    def other_contribute(self, value):
        self._other_contribute = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.merchant_contribute:
            if hasattr(self.merchant_contribute, 'to_alipay_dict'):
                params['merchant_contribute'] = self.merchant_contribute.to_alipay_dict()
            else:
                params['merchant_contribute'] = self.merchant_contribute
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.other_contribute:
            if hasattr(self.other_contribute, 'to_alipay_dict'):
                params['other_contribute'] = self.other_contribute.to_alipay_dict()
            else:
                params['other_contribute'] = self.other_contribute
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarVoucherInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'merchant_contribute' in d:
            o.merchant_contribute = d['merchant_contribute']
        if 'name' in d:
            o.name = d['name']
        if 'other_contribute' in d:
            o.other_contribute = d['other_contribute']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


