#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEdeductForecastQueryModel(object):

    def __init__(self):
        self._batch_order_amount = None
        self._batch_order_counts = None
        self._biz_type = None
        self._charge_inst = None
        self._chargeoff_inst = None
        self._deduct_date = None
        self._sub_biz_type = None

    @property
    def batch_order_amount(self):
        return self._batch_order_amount

    @batch_order_amount.setter
    def batch_order_amount(self, value):
        self._batch_order_amount = value
    @property
    def batch_order_counts(self):
        return self._batch_order_counts

    @batch_order_counts.setter
    def batch_order_counts(self, value):
        self._batch_order_counts = value
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
    def chargeoff_inst(self):
        return self._chargeoff_inst

    @chargeoff_inst.setter
    def chargeoff_inst(self, value):
        self._chargeoff_inst = value
    @property
    def deduct_date(self):
        return self._deduct_date

    @deduct_date.setter
    def deduct_date(self, value):
        self._deduct_date = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_order_amount:
            if hasattr(self.batch_order_amount, 'to_alipay_dict'):
                params['batch_order_amount'] = self.batch_order_amount.to_alipay_dict()
            else:
                params['batch_order_amount'] = self.batch_order_amount
        if self.batch_order_counts:
            if hasattr(self.batch_order_counts, 'to_alipay_dict'):
                params['batch_order_counts'] = self.batch_order_counts.to_alipay_dict()
            else:
                params['batch_order_counts'] = self.batch_order_counts
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
        if self.chargeoff_inst:
            if hasattr(self.chargeoff_inst, 'to_alipay_dict'):
                params['chargeoff_inst'] = self.chargeoff_inst.to_alipay_dict()
            else:
                params['chargeoff_inst'] = self.chargeoff_inst
        if self.deduct_date:
            if hasattr(self.deduct_date, 'to_alipay_dict'):
                params['deduct_date'] = self.deduct_date.to_alipay_dict()
            else:
                params['deduct_date'] = self.deduct_date
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
        o = AlipayEbppEdeductForecastQueryModel()
        if 'batch_order_amount' in d:
            o.batch_order_amount = d['batch_order_amount']
        if 'batch_order_counts' in d:
            o.batch_order_counts = d['batch_order_counts']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'chargeoff_inst' in d:
            o.chargeoff_inst = d['chargeoff_inst']
        if 'deduct_date' in d:
            o.deduct_date = d['deduct_date']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


