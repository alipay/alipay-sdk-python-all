#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanRepayApplyModel(object):

    def __init__(self):
        self._back_url = None
        self._loan_out_biz_no_list = None
        self._out_biz_no = None
        self._out_request_no = None
        self._repay_amt = None
        self._repay_type = None

    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def loan_out_biz_no_list(self):
        return self._loan_out_biz_no_list

    @loan_out_biz_no_list.setter
    def loan_out_biz_no_list(self, value):
        if isinstance(value, list):
            self._loan_out_biz_no_list = list()
            for i in value:
                self._loan_out_biz_no_list.append(i)
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
    def repay_amt(self):
        return self._repay_amt

    @repay_amt.setter
    def repay_amt(self, value):
        self._repay_amt = value
    @property
    def repay_type(self):
        return self._repay_type

    @repay_type.setter
    def repay_type(self, value):
        self._repay_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.loan_out_biz_no_list:
            if isinstance(self.loan_out_biz_no_list, list):
                for i in range(0, len(self.loan_out_biz_no_list)):
                    element = self.loan_out_biz_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.loan_out_biz_no_list[i] = element.to_alipay_dict()
            if hasattr(self.loan_out_biz_no_list, 'to_alipay_dict'):
                params['loan_out_biz_no_list'] = self.loan_out_biz_no_list.to_alipay_dict()
            else:
                params['loan_out_biz_no_list'] = self.loan_out_biz_no_list
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
        if self.repay_amt:
            if hasattr(self.repay_amt, 'to_alipay_dict'):
                params['repay_amt'] = self.repay_amt.to_alipay_dict()
            else:
                params['repay_amt'] = self.repay_amt
        if self.repay_type:
            if hasattr(self.repay_type, 'to_alipay_dict'):
                params['repay_type'] = self.repay_type.to_alipay_dict()
            else:
                params['repay_type'] = self.repay_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanRepayApplyModel()
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'loan_out_biz_no_list' in d:
            o.loan_out_biz_no_list = d['loan_out_biz_no_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'repay_amt' in d:
            o.repay_amt = d['repay_amt']
        if 'repay_type' in d:
            o.repay_type = d['repay_type']
        return o


