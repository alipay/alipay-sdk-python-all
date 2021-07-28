#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppBillkeyUpgradeModel(object):

    def __init__(self):
        self._bill_key = None
        self._biz_type = None
        self._charge_inst = None
        self._new_bill_key = None
        self._operation_type = None
        self._sub_biz_type = None

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
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def new_bill_key(self):
        return self._new_bill_key

    @new_bill_key.setter
    def new_bill_key(self, value):
        self._new_bill_key = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.new_bill_key:
            if hasattr(self.new_bill_key, 'to_alipay_dict'):
                params['new_bill_key'] = self.new_bill_key.to_alipay_dict()
            else:
                params['new_bill_key'] = self.new_bill_key
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppBillkeyUpgradeModel()
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'new_bill_key' in d:
            o.new_bill_key = d['new_bill_key']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


