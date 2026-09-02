#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationCreditphoneRoutehubQueryModel(object):

    def __init__(self):
        self._inst_pid = None
        self._order_no = None
        self._query_type = None
        self._request_no = None
        self._trade_no = None

    @property
    def inst_pid(self):
        return self._inst_pid

    @inst_pid.setter
    def inst_pid(self, value):
        self._inst_pid = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_pid:
            if hasattr(self.inst_pid, 'to_alipay_dict'):
                params['inst_pid'] = self.inst_pid.to_alipay_dict()
            else:
                params['inst_pid'] = self.inst_pid
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationCreditphoneRoutehubQueryModel()
        if 'inst_pid' in d:
            o.inst_pid = d['inst_pid']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


