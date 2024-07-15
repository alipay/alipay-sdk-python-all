#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthResourceContent import AuthResourceContent


class SearchDetailsByInviterResItem(object):

    def __init__(self):
        self._record_id = None
        self._resources = None

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        if isinstance(value, list):
            self._resources = list()
            for i in value:
                if isinstance(i, AuthResourceContent):
                    self._resources.append(i)
                else:
                    self._resources.append(AuthResourceContent.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.resources:
            if isinstance(self.resources, list):
                for i in range(0, len(self.resources)):
                    element = self.resources[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.resources[i] = element.to_alipay_dict()
            if hasattr(self.resources, 'to_alipay_dict'):
                params['resources'] = self.resources.to_alipay_dict()
            else:
                params['resources'] = self.resources
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchDetailsByInviterResItem()
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'resources' in d:
            o.resources = d['resources']
        return o


