#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SendEquityOrderResult(object):

    def __init__(self):
        self._equity_id = None
        self._equity_type = None
        self._order_id = None
        self._order_result_code = None
        self._order_result_msg = None
        self._order_status = None
        self._order_time = None

    @property
    def equity_id(self):
        return self._equity_id

    @equity_id.setter
    def equity_id(self, value):
        self._equity_id = value
    @property
    def equity_type(self):
        return self._equity_type

    @equity_type.setter
    def equity_type(self, value):
        self._equity_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_result_code(self):
        return self._order_result_code

    @order_result_code.setter
    def order_result_code(self, value):
        self._order_result_code = value
    @property
    def order_result_msg(self):
        return self._order_result_msg

    @order_result_msg.setter
    def order_result_msg(self, value):
        self._order_result_msg = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.equity_id:
            if hasattr(self.equity_id, 'to_alipay_dict'):
                params['equity_id'] = self.equity_id.to_alipay_dict()
            else:
                params['equity_id'] = self.equity_id
        if self.equity_type:
            if hasattr(self.equity_type, 'to_alipay_dict'):
                params['equity_type'] = self.equity_type.to_alipay_dict()
            else:
                params['equity_type'] = self.equity_type
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_result_code:
            if hasattr(self.order_result_code, 'to_alipay_dict'):
                params['order_result_code'] = self.order_result_code.to_alipay_dict()
            else:
                params['order_result_code'] = self.order_result_code
        if self.order_result_msg:
            if hasattr(self.order_result_msg, 'to_alipay_dict'):
                params['order_result_msg'] = self.order_result_msg.to_alipay_dict()
            else:
                params['order_result_msg'] = self.order_result_msg
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SendEquityOrderResult()
        if 'equity_id' in d:
            o.equity_id = d['equity_id']
        if 'equity_type' in d:
            o.equity_type = d['equity_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_result_code' in d:
            o.order_result_code = d['order_result_code']
        if 'order_result_msg' in d:
            o.order_result_msg = d['order_result_msg']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_time' in d:
            o.order_time = d['order_time']
        return o


