#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchPartAgreeInfo(object):

    def __init__(self):
        self._audit_info = None
        self._audit_operator = None
        self._audit_reason = None
        self._audit_type = None

    @property
    def audit_info(self):
        return self._audit_info

    @audit_info.setter
    def audit_info(self, value):
        self._audit_info = value
    @property
    def audit_operator(self):
        return self._audit_operator

    @audit_operator.setter
    def audit_operator(self, value):
        self._audit_operator = value
    @property
    def audit_reason(self):
        return self._audit_reason

    @audit_reason.setter
    def audit_reason(self, value):
        self._audit_reason = value
    @property
    def audit_type(self):
        return self._audit_type

    @audit_type.setter
    def audit_type(self, value):
        self._audit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_info:
            if hasattr(self.audit_info, 'to_alipay_dict'):
                params['audit_info'] = self.audit_info.to_alipay_dict()
            else:
                params['audit_info'] = self.audit_info
        if self.audit_operator:
            if hasattr(self.audit_operator, 'to_alipay_dict'):
                params['audit_operator'] = self.audit_operator.to_alipay_dict()
            else:
                params['audit_operator'] = self.audit_operator
        if self.audit_reason:
            if hasattr(self.audit_reason, 'to_alipay_dict'):
                params['audit_reason'] = self.audit_reason.to_alipay_dict()
            else:
                params['audit_reason'] = self.audit_reason
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
        o = SearchPartAgreeInfo()
        if 'audit_info' in d:
            o.audit_info = d['audit_info']
        if 'audit_operator' in d:
            o.audit_operator = d['audit_operator']
        if 'audit_reason' in d:
            o.audit_reason = d['audit_reason']
        if 'audit_type' in d:
            o.audit_type = d['audit_type']
        return o


