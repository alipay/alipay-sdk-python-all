#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfinspectionSyncModel(object):

    def __init__(self):
        self._biz_source = None
        self._order_code = None
        self._order_price = None
        self._pay_status = None
        self._reserve_code = None
        self._reserve_status = None
        self._reserve_time = None
        self._union_order_code = None

    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def order_code(self):
        return self._order_code

    @order_code.setter
    def order_code(self, value):
        self._order_code = value
    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def reserve_code(self):
        return self._reserve_code

    @reserve_code.setter
    def reserve_code(self, value):
        self._reserve_code = value
    @property
    def reserve_status(self):
        return self._reserve_status

    @reserve_status.setter
    def reserve_status(self, value):
        self._reserve_status = value
    @property
    def reserve_time(self):
        return self._reserve_time

    @reserve_time.setter
    def reserve_time(self, value):
        self._reserve_time = value
    @property
    def union_order_code(self):
        return self._union_order_code

    @union_order_code.setter
    def union_order_code(self, value):
        self._union_order_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.order_code:
            if hasattr(self.order_code, 'to_alipay_dict'):
                params['order_code'] = self.order_code.to_alipay_dict()
            else:
                params['order_code'] = self.order_code
        if self.order_price:
            if hasattr(self.order_price, 'to_alipay_dict'):
                params['order_price'] = self.order_price.to_alipay_dict()
            else:
                params['order_price'] = self.order_price
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.reserve_code:
            if hasattr(self.reserve_code, 'to_alipay_dict'):
                params['reserve_code'] = self.reserve_code.to_alipay_dict()
            else:
                params['reserve_code'] = self.reserve_code
        if self.reserve_status:
            if hasattr(self.reserve_status, 'to_alipay_dict'):
                params['reserve_status'] = self.reserve_status.to_alipay_dict()
            else:
                params['reserve_status'] = self.reserve_status
        if self.reserve_time:
            if hasattr(self.reserve_time, 'to_alipay_dict'):
                params['reserve_time'] = self.reserve_time.to_alipay_dict()
            else:
                params['reserve_time'] = self.reserve_time
        if self.union_order_code:
            if hasattr(self.union_order_code, 'to_alipay_dict'):
                params['union_order_code'] = self.union_order_code.to_alipay_dict()
            else:
                params['union_order_code'] = self.union_order_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfinspectionSyncModel()
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'order_code' in d:
            o.order_code = d['order_code']
        if 'order_price' in d:
            o.order_price = d['order_price']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'reserve_code' in d:
            o.reserve_code = d['reserve_code']
        if 'reserve_status' in d:
            o.reserve_status = d['reserve_status']
        if 'reserve_time' in d:
            o.reserve_time = d['reserve_time']
        if 'union_order_code' in d:
            o.union_order_code = d['union_order_code']
        return o


