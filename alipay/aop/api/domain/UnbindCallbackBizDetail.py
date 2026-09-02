#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnbindCallbackBizDetail(object):

    def __init__(self):
        self._alipay_order_no = None
        self._request_no = None
        self._trade_no = None
        self._unbind_result = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
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
    @property
    def unbind_result(self):
        return self._unbind_result

    @unbind_result.setter
    def unbind_result(self, value):
        self._unbind_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
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
        if self.unbind_result:
            if hasattr(self.unbind_result, 'to_alipay_dict'):
                params['unbind_result'] = self.unbind_result.to_alipay_dict()
            else:
                params['unbind_result'] = self.unbind_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnbindCallbackBizDetail()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'unbind_result' in d:
            o.unbind_result = d['unbind_result']
        return o


