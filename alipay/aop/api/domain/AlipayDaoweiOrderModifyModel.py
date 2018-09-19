#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDaoweiOrderModifyModel(object):

    def __init__(self):
        self._address = None
        self._gmt_start = None
        self._memo = None
        self._modify_type = None
        self._order_no = None
        self._origin_amount = None
        self._real_amount = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def modify_type(self):
        return self._modify_type

    @modify_type.setter
    def modify_type(self, value):
        self._modify_type = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        self._origin_amount = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.modify_type:
            if hasattr(self.modify_type, 'to_alipay_dict'):
                params['modify_type'] = self.modify_type.to_alipay_dict()
            else:
                params['modify_type'] = self.modify_type
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.origin_amount:
            if hasattr(self.origin_amount, 'to_alipay_dict'):
                params['origin_amount'] = self.origin_amount.to_alipay_dict()
            else:
                params['origin_amount'] = self.origin_amount
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDaoweiOrderModifyModel()
        if 'address' in d:
            o.address = d['address']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'memo' in d:
            o.memo = d['memo']
        if 'modify_type' in d:
            o.modify_type = d['modify_type']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'origin_amount' in d:
            o.origin_amount = d['origin_amount']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        return o


