#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepaymentDetailDto(object):

    def __init__(self):
        self._biz_order_id = None
        self._out_order_id = None
        self._period = None
        self._repayment_interest_price = None
        self._repayment_principal_price = None
        self._repayment_time = None
        self._repayment_total_price = None
        self._stage = None
        self._type = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def repayment_interest_price(self):
        return self._repayment_interest_price

    @repayment_interest_price.setter
    def repayment_interest_price(self, value):
        self._repayment_interest_price = value
    @property
    def repayment_principal_price(self):
        return self._repayment_principal_price

    @repayment_principal_price.setter
    def repayment_principal_price(self, value):
        self._repayment_principal_price = value
    @property
    def repayment_time(self):
        return self._repayment_time

    @repayment_time.setter
    def repayment_time(self, value):
        self._repayment_time = value
    @property
    def repayment_total_price(self):
        return self._repayment_total_price

    @repayment_total_price.setter
    def repayment_total_price(self, value):
        self._repayment_total_price = value
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.repayment_interest_price:
            if hasattr(self.repayment_interest_price, 'to_alipay_dict'):
                params['repayment_interest_price'] = self.repayment_interest_price.to_alipay_dict()
            else:
                params['repayment_interest_price'] = self.repayment_interest_price
        if self.repayment_principal_price:
            if hasattr(self.repayment_principal_price, 'to_alipay_dict'):
                params['repayment_principal_price'] = self.repayment_principal_price.to_alipay_dict()
            else:
                params['repayment_principal_price'] = self.repayment_principal_price
        if self.repayment_time:
            if hasattr(self.repayment_time, 'to_alipay_dict'):
                params['repayment_time'] = self.repayment_time.to_alipay_dict()
            else:
                params['repayment_time'] = self.repayment_time
        if self.repayment_total_price:
            if hasattr(self.repayment_total_price, 'to_alipay_dict'):
                params['repayment_total_price'] = self.repayment_total_price.to_alipay_dict()
            else:
                params['repayment_total_price'] = self.repayment_total_price
        if self.stage:
            if hasattr(self.stage, 'to_alipay_dict'):
                params['stage'] = self.stage.to_alipay_dict()
            else:
                params['stage'] = self.stage
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
        o = RepaymentDetailDto()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'period' in d:
            o.period = d['period']
        if 'repayment_interest_price' in d:
            o.repayment_interest_price = d['repayment_interest_price']
        if 'repayment_principal_price' in d:
            o.repayment_principal_price = d['repayment_principal_price']
        if 'repayment_time' in d:
            o.repayment_time = d['repayment_time']
        if 'repayment_total_price' in d:
            o.repayment_total_price = d['repayment_total_price']
        if 'stage' in d:
            o.stage = d['stage']
        if 'type' in d:
            o.type = d['type']
        return o


