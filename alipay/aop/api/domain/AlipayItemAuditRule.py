#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayItemAuditRule(object):

    def __init__(self):
        self._audit_type = None
        self._need_audit = None

    @property
    def audit_type(self):
        return self._audit_type

    @audit_type.setter
    def audit_type(self, value):
        self._audit_type = value
    @property
    def need_audit(self):
        return self._need_audit

    @need_audit.setter
    def need_audit(self, value):
        self._need_audit = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_type:
            if hasattr(self.audit_type, 'to_alipay_dict'):
                params['audit_type'] = self.audit_type.to_alipay_dict()
            else:
                params['audit_type'] = self.audit_type
        if self.need_audit:
            if hasattr(self.need_audit, 'to_alipay_dict'):
                params['need_audit'] = self.need_audit.to_alipay_dict()
            else:
                params['need_audit'] = self.need_audit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayItemAuditRule()
        if 'audit_type' in d:
            o.audit_type = d['audit_type']
        if 'need_audit' in d:
            o.need_audit = d['need_audit']
        return o


