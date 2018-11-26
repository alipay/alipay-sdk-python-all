#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanRepayResultQueryModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._out_request_no = None
        self._repay_receipt_no = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def repay_receipt_no(self):
        return self._repay_receipt_no

    @repay_receipt_no.setter
    def repay_receipt_no(self, value):
        self._repay_receipt_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.repay_receipt_no:
            if hasattr(self.repay_receipt_no, 'to_alipay_dict'):
                params['repay_receipt_no'] = self.repay_receipt_no.to_alipay_dict()
            else:
                params['repay_receipt_no'] = self.repay_receipt_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanRepayResultQueryModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'repay_receipt_no' in d:
            o.repay_receipt_no = d['repay_receipt_no']
        return o


