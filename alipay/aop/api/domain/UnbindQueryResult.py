#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnbindQueryResult(object):

    def __init__(self):
        self._cancel_bind_result = None
        self._request_no = None
        self._trade_no = None

    @property
    def cancel_bind_result(self):
        return self._cancel_bind_result

    @cancel_bind_result.setter
    def cancel_bind_result(self, value):
        self._cancel_bind_result = value
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
        if self.cancel_bind_result:
            if hasattr(self.cancel_bind_result, 'to_alipay_dict'):
                params['cancel_bind_result'] = self.cancel_bind_result.to_alipay_dict()
            else:
                params['cancel_bind_result'] = self.cancel_bind_result
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
        o = UnbindQueryResult()
        if 'cancel_bind_result' in d:
            o.cancel_bind_result = d['cancel_bind_result']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


