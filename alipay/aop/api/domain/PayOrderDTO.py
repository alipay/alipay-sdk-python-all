#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayOrderDTO(object):

    def __init__(self):
        self._actual_total_fee = None
        self._in_account_no = None
        self._in_account_open_id = None
        self._in_account_type = None
        self._out_account_no = None
        self._out_account_open_id = None
        self._out_account_type = None
        self._pay_flow_id = None
        self._pay_order_id = None
        self._pay_status = None
        self._pay_time = None
        self._pay_type = None
        self._total_fee = None

    @property
    def actual_total_fee(self):
        return self._actual_total_fee

    @actual_total_fee.setter
    def actual_total_fee(self, value):
        self._actual_total_fee = value
    @property
    def in_account_no(self):
        return self._in_account_no

    @in_account_no.setter
    def in_account_no(self, value):
        self._in_account_no = value
    @property
    def in_account_open_id(self):
        return self._in_account_open_id

    @in_account_open_id.setter
    def in_account_open_id(self, value):
        self._in_account_open_id = value
    @property
    def in_account_type(self):
        return self._in_account_type

    @in_account_type.setter
    def in_account_type(self, value):
        self._in_account_type = value
    @property
    def out_account_no(self):
        return self._out_account_no

    @out_account_no.setter
    def out_account_no(self, value):
        self._out_account_no = value
    @property
    def out_account_open_id(self):
        return self._out_account_open_id

    @out_account_open_id.setter
    def out_account_open_id(self, value):
        self._out_account_open_id = value
    @property
    def out_account_type(self):
        return self._out_account_type

    @out_account_type.setter
    def out_account_type(self, value):
        self._out_account_type = value
    @property
    def pay_flow_id(self):
        return self._pay_flow_id

    @pay_flow_id.setter
    def pay_flow_id(self, value):
        self._pay_flow_id = value
    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_total_fee:
            if hasattr(self.actual_total_fee, 'to_alipay_dict'):
                params['actual_total_fee'] = self.actual_total_fee.to_alipay_dict()
            else:
                params['actual_total_fee'] = self.actual_total_fee
        if self.in_account_no:
            if hasattr(self.in_account_no, 'to_alipay_dict'):
                params['in_account_no'] = self.in_account_no.to_alipay_dict()
            else:
                params['in_account_no'] = self.in_account_no
        if self.in_account_open_id:
            if hasattr(self.in_account_open_id, 'to_alipay_dict'):
                params['in_account_open_id'] = self.in_account_open_id.to_alipay_dict()
            else:
                params['in_account_open_id'] = self.in_account_open_id
        if self.in_account_type:
            if hasattr(self.in_account_type, 'to_alipay_dict'):
                params['in_account_type'] = self.in_account_type.to_alipay_dict()
            else:
                params['in_account_type'] = self.in_account_type
        if self.out_account_no:
            if hasattr(self.out_account_no, 'to_alipay_dict'):
                params['out_account_no'] = self.out_account_no.to_alipay_dict()
            else:
                params['out_account_no'] = self.out_account_no
        if self.out_account_open_id:
            if hasattr(self.out_account_open_id, 'to_alipay_dict'):
                params['out_account_open_id'] = self.out_account_open_id.to_alipay_dict()
            else:
                params['out_account_open_id'] = self.out_account_open_id
        if self.out_account_type:
            if hasattr(self.out_account_type, 'to_alipay_dict'):
                params['out_account_type'] = self.out_account_type.to_alipay_dict()
            else:
                params['out_account_type'] = self.out_account_type
        if self.pay_flow_id:
            if hasattr(self.pay_flow_id, 'to_alipay_dict'):
                params['pay_flow_id'] = self.pay_flow_id.to_alipay_dict()
            else:
                params['pay_flow_id'] = self.pay_flow_id
        if self.pay_order_id:
            if hasattr(self.pay_order_id, 'to_alipay_dict'):
                params['pay_order_id'] = self.pay_order_id.to_alipay_dict()
            else:
                params['pay_order_id'] = self.pay_order_id
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.total_fee:
            if hasattr(self.total_fee, 'to_alipay_dict'):
                params['total_fee'] = self.total_fee.to_alipay_dict()
            else:
                params['total_fee'] = self.total_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayOrderDTO()
        if 'actual_total_fee' in d:
            o.actual_total_fee = d['actual_total_fee']
        if 'in_account_no' in d:
            o.in_account_no = d['in_account_no']
        if 'in_account_open_id' in d:
            o.in_account_open_id = d['in_account_open_id']
        if 'in_account_type' in d:
            o.in_account_type = d['in_account_type']
        if 'out_account_no' in d:
            o.out_account_no = d['out_account_no']
        if 'out_account_open_id' in d:
            o.out_account_open_id = d['out_account_open_id']
        if 'out_account_type' in d:
            o.out_account_type = d['out_account_type']
        if 'pay_flow_id' in d:
            o.pay_flow_id = d['pay_flow_id']
        if 'pay_order_id' in d:
            o.pay_order_id = d['pay_order_id']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'total_fee' in d:
            o.total_fee = d['total_fee']
        return o


