#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanContractInfoQueryModel(object):

    def __init__(self):
        self._apply_receipt_no = None
        self._contract_type = None
        self._out_biz_no = None
        self._out_request_no = None

    @property
    def apply_receipt_no(self):
        return self._apply_receipt_no

    @apply_receipt_no.setter
    def apply_receipt_no(self, value):
        self._apply_receipt_no = value
    @property
    def contract_type(self):
        return self._contract_type

    @contract_type.setter
    def contract_type(self, value):
        self._contract_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.apply_receipt_no:
            if hasattr(self.apply_receipt_no, 'to_alipay_dict'):
                params['apply_receipt_no'] = self.apply_receipt_no.to_alipay_dict()
            else:
                params['apply_receipt_no'] = self.apply_receipt_no
        if self.contract_type:
            if hasattr(self.contract_type, 'to_alipay_dict'):
                params['contract_type'] = self.contract_type.to_alipay_dict()
            else:
                params['contract_type'] = self.contract_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanContractInfoQueryModel()
        if 'apply_receipt_no' in d:
            o.apply_receipt_no = d['apply_receipt_no']
        if 'contract_type' in d:
            o.contract_type = d['contract_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


