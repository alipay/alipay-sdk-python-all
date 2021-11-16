#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubTaskInfo(object):

    def __init__(self):
        self._execute_result = None
        self._status = None
        self._type = None
        self._type_desc = None

    @property
    def execute_result(self):
        return self._execute_result

    @execute_result.setter
    def execute_result(self, value):
        self._execute_result = value
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
    @property
    def type_desc(self):
        return self._type_desc

    @type_desc.setter
    def type_desc(self, value):
        self._type_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.execute_result:
            if hasattr(self.execute_result, 'to_alipay_dict'):
                params['execute_result'] = self.execute_result.to_alipay_dict()
            else:
                params['execute_result'] = self.execute_result
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
        if self.type_desc:
            if hasattr(self.type_desc, 'to_alipay_dict'):
                params['type_desc'] = self.type_desc.to_alipay_dict()
            else:
                params['type_desc'] = self.type_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubTaskInfo()
        if 'execute_result' in d:
            o.execute_result = d['execute_result']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        if 'type_desc' in d:
            o.type_desc = d['type_desc']
        return o


