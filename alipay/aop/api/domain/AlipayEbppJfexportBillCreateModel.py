#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppJfexportBillCreateModel(object):

    def __init__(self):
        self._amount = None
        self._bill_key = None
        self._biz_type = None
        self._cache_key = None
        self._charge_inst = None
        self._extend_field = None
        self._merchant_order_no = None
        self._sub_biz_type = None
        self._unique_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cache_key(self):
        return self._cache_key

    @cache_key.setter
    def cache_key(self, value):
        self._cache_key = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cache_key:
            if hasattr(self.cache_key, 'to_alipay_dict'):
                params['cache_key'] = self.cache_key.to_alipay_dict()
            else:
                params['cache_key'] = self.cache_key
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppJfexportBillCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cache_key' in d:
            o.cache_key = d['cache_key']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


