#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class WriteOffProcessDetailResponseOpenApiDTO(object):

    def __init__(self):
        self._bill_no = None
        self._ip_role_id = None
        self._opposite_bill_no = None
        self._opposite_writeoffable_bill_type = None
        self._writeoff_amt = None
        self._writeoffable_bill_type = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def opposite_bill_no(self):
        return self._opposite_bill_no

    @opposite_bill_no.setter
    def opposite_bill_no(self, value):
        self._opposite_bill_no = value
    @property
    def opposite_writeoffable_bill_type(self):
        return self._opposite_writeoffable_bill_type

    @opposite_writeoffable_bill_type.setter
    def opposite_writeoffable_bill_type(self, value):
        self._opposite_writeoffable_bill_type = value
    @property
    def writeoff_amt(self):
        return self._writeoff_amt

    @writeoff_amt.setter
    def writeoff_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._writeoff_amt = value
        else:
            self._writeoff_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def writeoffable_bill_type(self):
        return self._writeoffable_bill_type

    @writeoffable_bill_type.setter
    def writeoffable_bill_type(self, value):
        self._writeoffable_bill_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.opposite_bill_no:
            if hasattr(self.opposite_bill_no, 'to_alipay_dict'):
                params['opposite_bill_no'] = self.opposite_bill_no.to_alipay_dict()
            else:
                params['opposite_bill_no'] = self.opposite_bill_no
        if self.opposite_writeoffable_bill_type:
            if hasattr(self.opposite_writeoffable_bill_type, 'to_alipay_dict'):
                params['opposite_writeoffable_bill_type'] = self.opposite_writeoffable_bill_type.to_alipay_dict()
            else:
                params['opposite_writeoffable_bill_type'] = self.opposite_writeoffable_bill_type
        if self.writeoff_amt:
            if hasattr(self.writeoff_amt, 'to_alipay_dict'):
                params['writeoff_amt'] = self.writeoff_amt.to_alipay_dict()
            else:
                params['writeoff_amt'] = self.writeoff_amt
        if self.writeoffable_bill_type:
            if hasattr(self.writeoffable_bill_type, 'to_alipay_dict'):
                params['writeoffable_bill_type'] = self.writeoffable_bill_type.to_alipay_dict()
            else:
                params['writeoffable_bill_type'] = self.writeoffable_bill_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WriteOffProcessDetailResponseOpenApiDTO()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'opposite_bill_no' in d:
            o.opposite_bill_no = d['opposite_bill_no']
        if 'opposite_writeoffable_bill_type' in d:
            o.opposite_writeoffable_bill_type = d['opposite_writeoffable_bill_type']
        if 'writeoff_amt' in d:
            o.writeoff_amt = d['writeoff_amt']
        if 'writeoffable_bill_type' in d:
            o.writeoffable_bill_type = d['writeoffable_bill_type']
        return o


