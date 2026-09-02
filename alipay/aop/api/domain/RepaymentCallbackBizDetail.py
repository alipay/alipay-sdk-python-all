#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepaymentCallbackBizDetail(object):

    def __init__(self):
        self._repayment_results = None
        self._trade_no = None

    @property
    def repayment_results(self):
        return self._repayment_results

    @repayment_results.setter
    def repayment_results(self, value):
        self._repayment_results = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.repayment_results:
            if hasattr(self.repayment_results, 'to_alipay_dict'):
                params['repayment_results'] = self.repayment_results.to_alipay_dict()
            else:
                params['repayment_results'] = self.repayment_results
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
        o = RepaymentCallbackBizDetail()
        if 'repayment_results' in d:
            o.repayment_results = d['repayment_results']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


