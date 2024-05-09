#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TagInfo import TagInfo


class ConditionInfo(object):

    def __init__(self):
        self._identity = None
        self._operator = None
        self._priority = None
        self._tag_list = None

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                if isinstance(i, TagInfo):
                    self._tag_list.append(i)
                else:
                    self._tag_list.append(TagInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConditionInfo()
        if 'identity' in d:
            o.identity = d['identity']
        if 'operator' in d:
            o.operator = d['operator']
        if 'priority' in d:
            o.priority = d['priority']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        return o


