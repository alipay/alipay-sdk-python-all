#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcEmployeeTitleFailed(object):

    def __init__(self):
        self._employee_id = None
        self._enterprise_id = None
        self._message = None
        self._title_id = None
        self._title_tag = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def title_id(self):
        return self._title_id

    @title_id.setter
    def title_id(self, value):
        self._title_id = value
    @property
    def title_tag(self):
        return self._title_tag

    @title_tag.setter
    def title_tag(self, value):
        self._title_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.title_id:
            if hasattr(self.title_id, 'to_alipay_dict'):
                params['title_id'] = self.title_id.to_alipay_dict()
            else:
                params['title_id'] = self.title_id
        if self.title_tag:
            if hasattr(self.title_tag, 'to_alipay_dict'):
                params['title_tag'] = self.title_tag.to_alipay_dict()
            else:
                params['title_tag'] = self.title_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcEmployeeTitleFailed()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'message' in d:
            o.message = d['message']
        if 'title_id' in d:
            o.title_id = d['title_id']
        if 'title_tag' in d:
            o.title_tag = d['title_tag']
        return o


