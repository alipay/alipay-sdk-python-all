#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardRechargeDetail(object):

    def __init__(self):
        self._order_no = None
        self._recharge_fail_msg = None
        self._recharge_fee = None
        self._recharge_flow = None
        self._recharge_status = None
        self._recharge_time = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def recharge_fail_msg(self):
        return self._recharge_fail_msg

    @recharge_fail_msg.setter
    def recharge_fail_msg(self, value):
        self._recharge_fail_msg = value
    @property
    def recharge_fee(self):
        return self._recharge_fee

    @recharge_fee.setter
    def recharge_fee(self, value):
        self._recharge_fee = value
    @property
    def recharge_flow(self):
        return self._recharge_flow

    @recharge_flow.setter
    def recharge_flow(self, value):
        self._recharge_flow = value
    @property
    def recharge_status(self):
        return self._recharge_status

    @recharge_status.setter
    def recharge_status(self, value):
        self._recharge_status = value
    @property
    def recharge_time(self):
        return self._recharge_time

    @recharge_time.setter
    def recharge_time(self, value):
        self._recharge_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.recharge_fail_msg:
            if hasattr(self.recharge_fail_msg, 'to_alipay_dict'):
                params['recharge_fail_msg'] = self.recharge_fail_msg.to_alipay_dict()
            else:
                params['recharge_fail_msg'] = self.recharge_fail_msg
        if self.recharge_fee:
            if hasattr(self.recharge_fee, 'to_alipay_dict'):
                params['recharge_fee'] = self.recharge_fee.to_alipay_dict()
            else:
                params['recharge_fee'] = self.recharge_fee
        if self.recharge_flow:
            if hasattr(self.recharge_flow, 'to_alipay_dict'):
                params['recharge_flow'] = self.recharge_flow.to_alipay_dict()
            else:
                params['recharge_flow'] = self.recharge_flow
        if self.recharge_status:
            if hasattr(self.recharge_status, 'to_alipay_dict'):
                params['recharge_status'] = self.recharge_status.to_alipay_dict()
            else:
                params['recharge_status'] = self.recharge_status
        if self.recharge_time:
            if hasattr(self.recharge_time, 'to_alipay_dict'):
                params['recharge_time'] = self.recharge_time.to_alipay_dict()
            else:
                params['recharge_time'] = self.recharge_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardRechargeDetail()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'recharge_fail_msg' in d:
            o.recharge_fail_msg = d['recharge_fail_msg']
        if 'recharge_fee' in d:
            o.recharge_fee = d['recharge_fee']
        if 'recharge_flow' in d:
            o.recharge_flow = d['recharge_flow']
        if 'recharge_status' in d:
            o.recharge_status = d['recharge_status']
        if 'recharge_time' in d:
            o.recharge_time = d['recharge_time']
        return o


