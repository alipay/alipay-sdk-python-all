#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CashSummaryDTO(object):

    def __init__(self):
        self._biz_code = None
        self._biz_document_no = None
        self._pay_fail_amount = None
        self._pay_success_amount = None
        self._related_document_no = None
        self._total_amount = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_document_no(self):
        return self._biz_document_no

    @biz_document_no.setter
    def biz_document_no(self, value):
        self._biz_document_no = value
    @property
    def pay_fail_amount(self):
        return self._pay_fail_amount

    @pay_fail_amount.setter
    def pay_fail_amount(self, value):
        self._pay_fail_amount = value
    @property
    def pay_success_amount(self):
        return self._pay_success_amount

    @pay_success_amount.setter
    def pay_success_amount(self, value):
        self._pay_success_amount = value
    @property
    def related_document_no(self):
        return self._related_document_no

    @related_document_no.setter
    def related_document_no(self, value):
        self._related_document_no = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_document_no:
            if hasattr(self.biz_document_no, 'to_alipay_dict'):
                params['biz_document_no'] = self.biz_document_no.to_alipay_dict()
            else:
                params['biz_document_no'] = self.biz_document_no
        if self.pay_fail_amount:
            if hasattr(self.pay_fail_amount, 'to_alipay_dict'):
                params['pay_fail_amount'] = self.pay_fail_amount.to_alipay_dict()
            else:
                params['pay_fail_amount'] = self.pay_fail_amount
        if self.pay_success_amount:
            if hasattr(self.pay_success_amount, 'to_alipay_dict'):
                params['pay_success_amount'] = self.pay_success_amount.to_alipay_dict()
            else:
                params['pay_success_amount'] = self.pay_success_amount
        if self.related_document_no:
            if hasattr(self.related_document_no, 'to_alipay_dict'):
                params['related_document_no'] = self.related_document_no.to_alipay_dict()
            else:
                params['related_document_no'] = self.related_document_no
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CashSummaryDTO()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_document_no' in d:
            o.biz_document_no = d['biz_document_no']
        if 'pay_fail_amount' in d:
            o.pay_fail_amount = d['pay_fail_amount']
        if 'pay_success_amount' in d:
            o.pay_success_amount = d['pay_success_amount']
        if 'related_document_no' in d:
            o.related_document_no = d['related_document_no']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


