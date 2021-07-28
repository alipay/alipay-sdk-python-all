#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GFAOpenAPIAcceptanceResult(object):

    def __init__(self):
        self._acceptance_id = None
        self._need_retry = None
        self._out_business_no = None
        self._result_code = None
        self._result_message = None
        self._service_type = None
        self._solution_id = None
        self._sub_out_business_no = None

    @property
    def acceptance_id(self):
        return self._acceptance_id

    @acceptance_id.setter
    def acceptance_id(self, value):
        self._acceptance_id = value
    @property
    def need_retry(self):
        return self._need_retry

    @need_retry.setter
    def need_retry(self, value):
        self._need_retry = value
    @property
    def out_business_no(self):
        return self._out_business_no

    @out_business_no.setter
    def out_business_no(self, value):
        self._out_business_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value
    @property
    def sub_out_business_no(self):
        return self._sub_out_business_no

    @sub_out_business_no.setter
    def sub_out_business_no(self, value):
        self._sub_out_business_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.acceptance_id:
            if hasattr(self.acceptance_id, 'to_alipay_dict'):
                params['acceptance_id'] = self.acceptance_id.to_alipay_dict()
            else:
                params['acceptance_id'] = self.acceptance_id
        if self.need_retry:
            if hasattr(self.need_retry, 'to_alipay_dict'):
                params['need_retry'] = self.need_retry.to_alipay_dict()
            else:
                params['need_retry'] = self.need_retry
        if self.out_business_no:
            if hasattr(self.out_business_no, 'to_alipay_dict'):
                params['out_business_no'] = self.out_business_no.to_alipay_dict()
            else:
                params['out_business_no'] = self.out_business_no
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_message:
            if hasattr(self.result_message, 'to_alipay_dict'):
                params['result_message'] = self.result_message.to_alipay_dict()
            else:
                params['result_message'] = self.result_message
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        if self.sub_out_business_no:
            if hasattr(self.sub_out_business_no, 'to_alipay_dict'):
                params['sub_out_business_no'] = self.sub_out_business_no.to_alipay_dict()
            else:
                params['sub_out_business_no'] = self.sub_out_business_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIAcceptanceResult()
        if 'acceptance_id' in d:
            o.acceptance_id = d['acceptance_id']
        if 'need_retry' in d:
            o.need_retry = d['need_retry']
        if 'out_business_no' in d:
            o.out_business_no = d['out_business_no']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_message' in d:
            o.result_message = d['result_message']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        if 'sub_out_business_no' in d:
            o.sub_out_business_no = d['sub_out_business_no']
        return o


