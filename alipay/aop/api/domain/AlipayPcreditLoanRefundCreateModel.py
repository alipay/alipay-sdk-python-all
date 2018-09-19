#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanRefundCreateModel(object):

    def __init__(self):
        self._loan_apply_no = None
        self._out_biz_no = None
        self._repay_amt = None
        self._req_id = None

    @property
    def loan_apply_no(self):
        return self._loan_apply_no

    @loan_apply_no.setter
    def loan_apply_no(self, value):
        self._loan_apply_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def repay_amt(self):
        return self._repay_amt

    @repay_amt.setter
    def repay_amt(self, value):
        self._repay_amt = value
    @property
    def req_id(self):
        return self._req_id

    @req_id.setter
    def req_id(self, value):
        self._req_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.loan_apply_no:
            if hasattr(self.loan_apply_no, 'to_alipay_dict'):
                params['loan_apply_no'] = self.loan_apply_no.to_alipay_dict()
            else:
                params['loan_apply_no'] = self.loan_apply_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.repay_amt:
            if hasattr(self.repay_amt, 'to_alipay_dict'):
                params['repay_amt'] = self.repay_amt.to_alipay_dict()
            else:
                params['repay_amt'] = self.repay_amt
        if self.req_id:
            if hasattr(self.req_id, 'to_alipay_dict'):
                params['req_id'] = self.req_id.to_alipay_dict()
            else:
                params['req_id'] = self.req_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanRefundCreateModel()
        if 'loan_apply_no' in d:
            o.loan_apply_no = d['loan_apply_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'repay_amt' in d:
            o.repay_amt = d['repay_amt']
        if 'req_id' in d:
            o.req_id = d['req_id']
        return o


