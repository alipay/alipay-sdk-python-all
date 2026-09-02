#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportChargerIdlefeeCreateModel(object):

    def __init__(self):
        self._billing_rule = None
        self._charge_order_no = None
        self._open_id = None
        self._out_order_no = None
        self._start_time = None
        self._user_id = None

    @property
    def billing_rule(self):
        return self._billing_rule

    @billing_rule.setter
    def billing_rule(self, value):
        self._billing_rule = value
    @property
    def charge_order_no(self):
        return self._charge_order_no

    @charge_order_no.setter
    def charge_order_no(self, value):
        self._charge_order_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.billing_rule:
            if hasattr(self.billing_rule, 'to_alipay_dict'):
                params['billing_rule'] = self.billing_rule.to_alipay_dict()
            else:
                params['billing_rule'] = self.billing_rule
        if self.charge_order_no:
            if hasattr(self.charge_order_no, 'to_alipay_dict'):
                params['charge_order_no'] = self.charge_order_no.to_alipay_dict()
            else:
                params['charge_order_no'] = self.charge_order_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportChargerIdlefeeCreateModel()
        if 'billing_rule' in d:
            o.billing_rule = d['billing_rule']
        if 'charge_order_no' in d:
            o.charge_order_no = d['charge_order_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


