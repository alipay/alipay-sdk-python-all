#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundCallbackBizDetail(object):

    def __init__(self):
        self._request_no = None
        self._trade_no = None
        self._transfer_refund_results = None

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
    def transfer_refund_results(self):
        return self._transfer_refund_results

    @transfer_refund_results.setter
    def transfer_refund_results(self, value):
        self._transfer_refund_results = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.transfer_refund_results:
            if hasattr(self.transfer_refund_results, 'to_alipay_dict'):
                params['transfer_refund_results'] = self.transfer_refund_results.to_alipay_dict()
            else:
                params['transfer_refund_results'] = self.transfer_refund_results
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundCallbackBizDetail()
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'transfer_refund_results' in d:
            o.transfer_refund_results = d['transfer_refund_results']
        return o


