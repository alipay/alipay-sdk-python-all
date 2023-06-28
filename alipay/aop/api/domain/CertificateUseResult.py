#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertificateInstanceAmountInfo import CertificateInstanceAmountInfo


class CertificateUseResult(object):

    def __init__(self):
        self._amount_info = None
        self._code = None
        self._encrypted_code = None
        self._msg = None
        self._result = None
        self._use_order_no = None

    @property
    def amount_info(self):
        return self._amount_info

    @amount_info.setter
    def amount_info(self, value):
        if isinstance(value, CertificateInstanceAmountInfo):
            self._amount_info = value
        else:
            self._amount_info = CertificateInstanceAmountInfo.from_alipay_dict(value)
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def encrypted_code(self):
        return self._encrypted_code

    @encrypted_code.setter
    def encrypted_code(self, value):
        self._encrypted_code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def use_order_no(self):
        return self._use_order_no

    @use_order_no.setter
    def use_order_no(self, value):
        self._use_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_info:
            if hasattr(self.amount_info, 'to_alipay_dict'):
                params['amount_info'] = self.amount_info.to_alipay_dict()
            else:
                params['amount_info'] = self.amount_info
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.encrypted_code:
            if hasattr(self.encrypted_code, 'to_alipay_dict'):
                params['encrypted_code'] = self.encrypted_code.to_alipay_dict()
            else:
                params['encrypted_code'] = self.encrypted_code
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.use_order_no:
            if hasattr(self.use_order_no, 'to_alipay_dict'):
                params['use_order_no'] = self.use_order_no.to_alipay_dict()
            else:
                params['use_order_no'] = self.use_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateUseResult()
        if 'amount_info' in d:
            o.amount_info = d['amount_info']
        if 'code' in d:
            o.code = d['code']
        if 'encrypted_code' in d:
            o.encrypted_code = d['encrypted_code']
        if 'msg' in d:
            o.msg = d['msg']
        if 'result' in d:
            o.result = d['result']
        if 'use_order_no' in d:
            o.use_order_no = d['use_order_no']
        return o


