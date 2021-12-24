#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AcquireOrder import AcquireOrder
from alipay.aop.api.domain.FundOrder import FundOrder


class AnttechBlockchainDefinSaasPaymentCreateModel(object):

    def __init__(self):
        self._acquire_order = None
        self._fund_mode = None
        self._fund_order = None
        self._order_type = None
        self._out_request_id = None
        self._platform_member_id = None

    @property
    def acquire_order(self):
        return self._acquire_order

    @acquire_order.setter
    def acquire_order(self, value):
        if isinstance(value, AcquireOrder):
            self._acquire_order = value
        else:
            self._acquire_order = AcquireOrder.from_alipay_dict(value)
    @property
    def fund_mode(self):
        return self._fund_mode

    @fund_mode.setter
    def fund_mode(self, value):
        self._fund_mode = value
    @property
    def fund_order(self):
        return self._fund_order

    @fund_order.setter
    def fund_order(self, value):
        if isinstance(value, FundOrder):
            self._fund_order = value
        else:
            self._fund_order = FundOrder.from_alipay_dict(value)
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.acquire_order:
            if hasattr(self.acquire_order, 'to_alipay_dict'):
                params['acquire_order'] = self.acquire_order.to_alipay_dict()
            else:
                params['acquire_order'] = self.acquire_order
        if self.fund_mode:
            if hasattr(self.fund_mode, 'to_alipay_dict'):
                params['fund_mode'] = self.fund_mode.to_alipay_dict()
            else:
                params['fund_mode'] = self.fund_mode
        if self.fund_order:
            if hasattr(self.fund_order, 'to_alipay_dict'):
                params['fund_order'] = self.fund_order.to_alipay_dict()
            else:
                params['fund_order'] = self.fund_order
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_request_id:
            if hasattr(self.out_request_id, 'to_alipay_dict'):
                params['out_request_id'] = self.out_request_id.to_alipay_dict()
            else:
                params['out_request_id'] = self.out_request_id
        if self.platform_member_id:
            if hasattr(self.platform_member_id, 'to_alipay_dict'):
                params['platform_member_id'] = self.platform_member_id.to_alipay_dict()
            else:
                params['platform_member_id'] = self.platform_member_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinSaasPaymentCreateModel()
        if 'acquire_order' in d:
            o.acquire_order = d['acquire_order']
        if 'fund_mode' in d:
            o.fund_mode = d['fund_mode']
        if 'fund_order' in d:
            o.fund_order = d['fund_order']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_request_id' in d:
            o.out_request_id = d['out_request_id']
        if 'platform_member_id' in d:
            o.platform_member_id = d['platform_member_id']
        return o


