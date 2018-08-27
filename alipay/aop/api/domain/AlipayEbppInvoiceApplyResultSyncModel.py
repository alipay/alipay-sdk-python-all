#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceApplyResultSyncModel(object):

    def __init__(self):
        self._apply_id = None
        self._result = None
        self._result_code = None
        self._result_msg = None
        self._tax_apply_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def tax_apply_id(self):
        return self._tax_apply_id

    @tax_apply_id.setter
    def tax_apply_id(self, value):
        self._tax_apply_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_msg:
            if hasattr(self.result_msg, 'to_alipay_dict'):
                params['result_msg'] = self.result_msg.to_alipay_dict()
            else:
                params['result_msg'] = self.result_msg
        if self.tax_apply_id:
            if hasattr(self.tax_apply_id, 'to_alipay_dict'):
                params['tax_apply_id'] = self.tax_apply_id.to_alipay_dict()
            else:
                params['tax_apply_id'] = self.tax_apply_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceApplyResultSyncModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'result' in d:
            o.result = d['result']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        if 'tax_apply_id' in d:
            o.tax_apply_id = d['tax_apply_id']
        return o


