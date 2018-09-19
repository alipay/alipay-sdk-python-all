#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbadvertRoleInfoResponse(object):

    def __init__(self):
        self._role_code = None
        self._status = None

    @property
    def role_code(self):
        return self._role_code

    @role_code.setter
    def role_code(self, value):
        self._role_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.role_code:
            if hasattr(self.role_code, 'to_alipay_dict'):
                params['role_code'] = self.role_code.to_alipay_dict()
            else:
                params['role_code'] = self.role_code
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
        o = KbadvertRoleInfoResponse()
        if 'role_code' in d:
            o.role_code = d['role_code']
        if 'status' in d:
            o.status = d['status']
        return o


