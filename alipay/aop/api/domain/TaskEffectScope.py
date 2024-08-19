#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskEffectScope(object):

    def __init__(self):
        self._scope_id = None
        self._subject_list = None
        self._subject_type = None

    @property
    def scope_id(self):
        return self._scope_id

    @scope_id.setter
    def scope_id(self, value):
        self._scope_id = value
    @property
    def subject_list(self):
        return self._subject_list

    @subject_list.setter
    def subject_list(self, value):
        if isinstance(value, list):
            self._subject_list = list()
            for i in value:
                self._subject_list.append(i)
    @property
    def subject_type(self):
        return self._subject_type

    @subject_type.setter
    def subject_type(self, value):
        self._subject_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.scope_id:
            if hasattr(self.scope_id, 'to_alipay_dict'):
                params['scope_id'] = self.scope_id.to_alipay_dict()
            else:
                params['scope_id'] = self.scope_id
        if self.subject_list:
            if isinstance(self.subject_list, list):
                for i in range(0, len(self.subject_list)):
                    element = self.subject_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subject_list[i] = element.to_alipay_dict()
            if hasattr(self.subject_list, 'to_alipay_dict'):
                params['subject_list'] = self.subject_list.to_alipay_dict()
            else:
                params['subject_list'] = self.subject_list
        if self.subject_type:
            if hasattr(self.subject_type, 'to_alipay_dict'):
                params['subject_type'] = self.subject_type.to_alipay_dict()
            else:
                params['subject_type'] = self.subject_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskEffectScope()
        if 'scope_id' in d:
            o.scope_id = d['scope_id']
        if 'subject_list' in d:
            o.subject_list = d['subject_list']
        if 'subject_type' in d:
            o.subject_type = d['subject_type']
        return o


