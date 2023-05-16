#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitFailureInfo(object):

    def __init__(self):
        self._enroll_failure_reason = None

    @property
    def enroll_failure_reason(self):
        return self._enroll_failure_reason

    @enroll_failure_reason.setter
    def enroll_failure_reason(self, value):
        self._enroll_failure_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.enroll_failure_reason:
            if hasattr(self.enroll_failure_reason, 'to_alipay_dict'):
                params['enroll_failure_reason'] = self.enroll_failure_reason.to_alipay_dict()
            else:
                params['enroll_failure_reason'] = self.enroll_failure_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitFailureInfo()
        if 'enroll_failure_reason' in d:
            o.enroll_failure_reason = d['enroll_failure_reason']
        return o


