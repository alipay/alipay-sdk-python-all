#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CrowdOperationNodeOptionDetail(object):

    def __init__(self):
        self._desc = None
        self._id = None
        self._parent_id = None
        self._parent_value = None
        self._priority = None
        self._text = None
        self._value = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    @property
    def parent_value(self):
        return self._parent_value

    @parent_value.setter
    def parent_value(self, value):
        self._parent_value = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        if self.parent_value:
            if hasattr(self.parent_value, 'to_alipay_dict'):
                params['parent_value'] = self.parent_value.to_alipay_dict()
            else:
                params['parent_value'] = self.parent_value
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdOperationNodeOptionDetail()
        if 'desc' in d:
            o.desc = d['desc']
        if 'id' in d:
            o.id = d['id']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'parent_value' in d:
            o.parent_value = d['parent_value']
        if 'priority' in d:
            o.priority = d['priority']
        if 'text' in d:
            o.text = d['text']
        if 'value' in d:
            o.value = d['value']
        return o


