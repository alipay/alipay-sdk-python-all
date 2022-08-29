#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskRobotAuditFeedbackReq(object):

    def __init__(self):
        self._audit_result = None
        self._audit_status = None
        self._request_id = None

    @property
    def audit_result(self):
        return self._audit_result

    @audit_result.setter
    def audit_result(self, value):
        self._audit_result = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_result:
            if hasattr(self.audit_result, 'to_alipay_dict'):
                params['audit_result'] = self.audit_result.to_alipay_dict()
            else:
                params['audit_result'] = self.audit_result
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskRobotAuditFeedbackReq()
        if 'audit_result' in d:
            o.audit_result = d['audit_result']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


