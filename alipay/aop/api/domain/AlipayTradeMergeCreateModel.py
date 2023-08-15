#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderDetail import OrderDetail


class AlipayTradeMergeCreateModel(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_open_id = None
        self._op_app_id = None
        self._order_details = None
        self._out_merge_no = None
        self._time_expire = None
        self._timeout_express = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def op_app_id(self):
        return self._op_app_id

    @op_app_id.setter
    def op_app_id(self, value):
        self._op_app_id = value
    @property
    def order_details(self):
        return self._order_details

    @order_details.setter
    def order_details(self, value):
        if isinstance(value, list):
            self._order_details = list()
            for i in value:
                if isinstance(i, OrderDetail):
                    self._order_details.append(i)
                else:
                    self._order_details.append(OrderDetail.from_alipay_dict(i))
    @property
    def out_merge_no(self):
        return self._out_merge_no

    @out_merge_no.setter
    def out_merge_no(self, value):
        self._out_merge_no = value
    @property
    def time_expire(self):
        return self._time_expire

    @time_expire.setter
    def time_expire(self, value):
        self._time_expire = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.op_app_id:
            if hasattr(self.op_app_id, 'to_alipay_dict'):
                params['op_app_id'] = self.op_app_id.to_alipay_dict()
            else:
                params['op_app_id'] = self.op_app_id
        if self.order_details:
            if isinstance(self.order_details, list):
                for i in range(0, len(self.order_details)):
                    element = self.order_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_details[i] = element.to_alipay_dict()
            if hasattr(self.order_details, 'to_alipay_dict'):
                params['order_details'] = self.order_details.to_alipay_dict()
            else:
                params['order_details'] = self.order_details
        if self.out_merge_no:
            if hasattr(self.out_merge_no, 'to_alipay_dict'):
                params['out_merge_no'] = self.out_merge_no.to_alipay_dict()
            else:
                params['out_merge_no'] = self.out_merge_no
        if self.time_expire:
            if hasattr(self.time_expire, 'to_alipay_dict'):
                params['time_expire'] = self.time_expire.to_alipay_dict()
            else:
                params['time_expire'] = self.time_expire
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeMergeCreateModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'op_app_id' in d:
            o.op_app_id = d['op_app_id']
        if 'order_details' in d:
            o.order_details = d['order_details']
        if 'out_merge_no' in d:
            o.out_merge_no = d['out_merge_no']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        return o


