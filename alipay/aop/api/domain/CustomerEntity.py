#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomerTag import CustomerTag


class CustomerEntity(object):

    def __init__(self):
        self._code = None
        self._desc = None
        self._id = None
        self._name = None
        self._tags = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                if isinstance(i, CustomerTag):
                    self._tags.append(i)
                else:
                    self._tags.append(CustomerTag.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerEntity()
        if 'code' in d:
            o.code = d['code']
        if 'desc' in d:
            o.desc = d['desc']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'tags' in d:
            o.tags = d['tags']
        return o


