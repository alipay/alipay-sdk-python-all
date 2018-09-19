#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsClaimAttachment(object):

    def __init__(self):
        self._description = None
        self._name = None
        self._path = None
        self._reason = None
        self._status = None
        self._type = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsClaimAttachment()
        if 'description' in d:
            o.description = d['description']
        if 'name' in d:
            o.name = d['name']
        if 'path' in d:
            o.path = d['path']
        if 'reason' in d:
            o.reason = d['reason']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        return o


