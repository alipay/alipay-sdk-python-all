#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuditResultInfo(object):

    def __init__(self):
        self._audit_reason = None
        self._audit_result = None
        self._audit_type = None

    @property
    def audit_reason(self):
        return self._audit_reason

    @audit_reason.setter
    def audit_reason(self, value):
        self._audit_reason = value
    @property
    def audit_result(self):
        return self._audit_result

    @audit_result.setter
    def audit_result(self, value):
        self._audit_result = value
    @property
    def audit_type(self):
        return self._audit_type

    @audit_type.setter
    def audit_type(self, value):
        self._audit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_reason:
            if hasattr(self.audit_reason, 'to_alipay_dict'):
                params['audit_reason'] = self.audit_reason.to_alipay_dict()
            else:
                params['audit_reason'] = self.audit_reason
        if self.audit_result:
            if hasattr(self.audit_result, 'to_alipay_dict'):
                params['audit_result'] = self.audit_result.to_alipay_dict()
            else:
                params['audit_result'] = self.audit_result
        if self.audit_type:
            if hasattr(self.audit_type, 'to_alipay_dict'):
                params['audit_type'] = self.audit_type.to_alipay_dict()
            else:
                params['audit_type'] = self.audit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuditResultInfo()
        if 'audit_reason' in d:
            o.audit_reason = d['audit_reason']
        if 'audit_result' in d:
            o.audit_result = d['audit_result']
        if 'audit_type' in d:
            o.audit_type = d['audit_type']
        return o


