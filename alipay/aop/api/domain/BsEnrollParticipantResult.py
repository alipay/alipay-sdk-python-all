#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BsEnrollParticipantResultDetail import BsEnrollParticipantResultDetail


class BsEnrollParticipantResult(object):

    def __init__(self):
        self._enroll_result = None
        self._enroll_result_detail = None
        self._fail_code = None
        self._fail_reason = None
        self._value = None

    @property
    def enroll_result(self):
        return self._enroll_result

    @enroll_result.setter
    def enroll_result(self, value):
        self._enroll_result = value
    @property
    def enroll_result_detail(self):
        return self._enroll_result_detail

    @enroll_result_detail.setter
    def enroll_result_detail(self, value):
        if isinstance(value, BsEnrollParticipantResultDetail):
            self._enroll_result_detail = value
        else:
            self._enroll_result_detail = BsEnrollParticipantResultDetail.from_alipay_dict(value)
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.enroll_result:
            if hasattr(self.enroll_result, 'to_alipay_dict'):
                params['enroll_result'] = self.enroll_result.to_alipay_dict()
            else:
                params['enroll_result'] = self.enroll_result
        if self.enroll_result_detail:
            if hasattr(self.enroll_result_detail, 'to_alipay_dict'):
                params['enroll_result_detail'] = self.enroll_result_detail.to_alipay_dict()
            else:
                params['enroll_result_detail'] = self.enroll_result_detail
        if self.fail_code:
            if hasattr(self.fail_code, 'to_alipay_dict'):
                params['fail_code'] = self.fail_code.to_alipay_dict()
            else:
                params['fail_code'] = self.fail_code
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
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
        o = BsEnrollParticipantResult()
        if 'enroll_result' in d:
            o.enroll_result = d['enroll_result']
        if 'enroll_result_detail' in d:
            o.enroll_result_detail = d['enroll_result_detail']
        if 'fail_code' in d:
            o.fail_code = d['fail_code']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'value' in d:
            o.value = d['value']
        return o


