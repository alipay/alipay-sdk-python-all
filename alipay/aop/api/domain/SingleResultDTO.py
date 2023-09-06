#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SingleResultDTO(object):

    def __init__(self):
        self._invoice_id = None
        self._result_code = None
        self._result_msg = None
        self._succeeded = None

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
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
    def succeeded(self):
        return self._succeeded

    @succeeded.setter
    def succeeded(self, value):
        self._succeeded = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
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
        if self.succeeded:
            if hasattr(self.succeeded, 'to_alipay_dict'):
                params['succeeded'] = self.succeeded.to_alipay_dict()
            else:
                params['succeeded'] = self.succeeded
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SingleResultDTO()
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        if 'succeeded' in d:
            o.succeeded = d['succeeded']
        return o


