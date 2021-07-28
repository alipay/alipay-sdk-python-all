#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsAccountStatusDTO(object):

    def __init__(self):
        self._audit_desc = None
        self._logistics_code = None
        self._logistics_name = None
        self._status = None

    @property
    def audit_desc(self):
        return self._audit_desc

    @audit_desc.setter
    def audit_desc(self, value):
        self._audit_desc = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def logistics_name(self):
        return self._logistics_name

    @logistics_name.setter
    def logistics_name(self, value):
        self._logistics_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_desc:
            if hasattr(self.audit_desc, 'to_alipay_dict'):
                params['audit_desc'] = self.audit_desc.to_alipay_dict()
            else:
                params['audit_desc'] = self.audit_desc
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.logistics_name:
            if hasattr(self.logistics_name, 'to_alipay_dict'):
                params['logistics_name'] = self.logistics_name.to_alipay_dict()
            else:
                params['logistics_name'] = self.logistics_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsAccountStatusDTO()
        if 'audit_desc' in d:
            o.audit_desc = d['audit_desc']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_name' in d:
            o.logistics_name = d['logistics_name']
        if 'status' in d:
            o.status = d['status']
        return o


