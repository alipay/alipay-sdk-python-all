#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanCollateralValuationSyncModel(object):

    def __init__(self):
        self._apply_no = None
        self._eval_time = None
        self._ext_info = None
        self._out_request_no = None
        self._rejected_code = None
        self._rejected_reason = None
        self._request_id = None
        self._value = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def eval_time(self):
        return self._eval_time

    @eval_time.setter
    def eval_time(self, value):
        self._eval_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def rejected_code(self):
        return self._rejected_code

    @rejected_code.setter
    def rejected_code(self, value):
        self._rejected_code = value
    @property
    def rejected_reason(self):
        return self._rejected_reason

    @rejected_reason.setter
    def rejected_reason(self, value):
        self._rejected_reason = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.eval_time:
            if hasattr(self.eval_time, 'to_alipay_dict'):
                params['eval_time'] = self.eval_time.to_alipay_dict()
            else:
                params['eval_time'] = self.eval_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.rejected_code:
            if hasattr(self.rejected_code, 'to_alipay_dict'):
                params['rejected_code'] = self.rejected_code.to_alipay_dict()
            else:
                params['rejected_code'] = self.rejected_code
        if self.rejected_reason:
            if hasattr(self.rejected_reason, 'to_alipay_dict'):
                params['rejected_reason'] = self.rejected_reason.to_alipay_dict()
            else:
                params['rejected_reason'] = self.rejected_reason
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanCollateralValuationSyncModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'eval_time' in d:
            o.eval_time = d['eval_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'rejected_code' in d:
            o.rejected_code = d['rejected_code']
        if 'rejected_reason' in d:
            o.rejected_reason = d['rejected_reason']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'value' in d:
            o.value = d['value']
        return o


