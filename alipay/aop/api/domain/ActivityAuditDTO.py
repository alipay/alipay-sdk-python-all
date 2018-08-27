#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityAuditDTO(object):

    def __init__(self):
        self._audit_id = None
        self._audit_status = None
        self._creator_id = None
        self._creator_type = None
        self._operation_time = None
        self._reason = None

    @property
    def audit_id(self):
        return self._audit_id

    @audit_id.setter
    def audit_id(self, value):
        self._audit_id = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def creator_type(self):
        return self._creator_type

    @creator_type.setter
    def creator_type(self, value):
        self._creator_type = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_id:
            if hasattr(self.audit_id, 'to_alipay_dict'):
                params['audit_id'] = self.audit_id.to_alipay_dict()
            else:
                params['audit_id'] = self.audit_id
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.creator_type:
            if hasattr(self.creator_type, 'to_alipay_dict'):
                params['creator_type'] = self.creator_type.to_alipay_dict()
            else:
                params['creator_type'] = self.creator_type
        if self.operation_time:
            if hasattr(self.operation_time, 'to_alipay_dict'):
                params['operation_time'] = self.operation_time.to_alipay_dict()
            else:
                params['operation_time'] = self.operation_time
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityAuditDTO()
        if 'audit_id' in d:
            o.audit_id = d['audit_id']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'creator_type' in d:
            o.creator_type = d['creator_type']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'reason' in d:
            o.reason = d['reason']
        return o


