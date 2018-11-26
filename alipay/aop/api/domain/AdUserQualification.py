#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdUserQualification(object):

    def __init__(self):
        self._approver = None
        self._audit_reason = None
        self._audit_status = None
        self._audit_time = None
        self._file_url = None
        self._id = None
        self._qualification_name = None

    @property
    def approver(self):
        return self._approver

    @approver.setter
    def approver(self, value):
        self._approver = value
    @property
    def audit_reason(self):
        return self._audit_reason

    @audit_reason.setter
    def audit_reason(self, value):
        self._audit_reason = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def audit_time(self):
        return self._audit_time

    @audit_time.setter
    def audit_time(self, value):
        self._audit_time = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        if isinstance(value, list):
            self._file_url = list()
            for i in value:
                self._file_url.append(i)
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def qualification_name(self):
        return self._qualification_name

    @qualification_name.setter
    def qualification_name(self, value):
        self._qualification_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.approver:
            if hasattr(self.approver, 'to_alipay_dict'):
                params['approver'] = self.approver.to_alipay_dict()
            else:
                params['approver'] = self.approver
        if self.audit_reason:
            if hasattr(self.audit_reason, 'to_alipay_dict'):
                params['audit_reason'] = self.audit_reason.to_alipay_dict()
            else:
                params['audit_reason'] = self.audit_reason
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.audit_time:
            if hasattr(self.audit_time, 'to_alipay_dict'):
                params['audit_time'] = self.audit_time.to_alipay_dict()
            else:
                params['audit_time'] = self.audit_time
        if self.file_url:
            if isinstance(self.file_url, list):
                for i in range(0, len(self.file_url)):
                    element = self.file_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_url[i] = element.to_alipay_dict()
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.qualification_name:
            if hasattr(self.qualification_name, 'to_alipay_dict'):
                params['qualification_name'] = self.qualification_name.to_alipay_dict()
            else:
                params['qualification_name'] = self.qualification_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdUserQualification()
        if 'approver' in d:
            o.approver = d['approver']
        if 'audit_reason' in d:
            o.audit_reason = d['audit_reason']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'audit_time' in d:
            o.audit_time = d['audit_time']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'id' in d:
            o.id = d['id']
        if 'qualification_name' in d:
            o.qualification_name = d['qualification_name']
        return o


