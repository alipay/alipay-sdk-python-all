#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromotePageProperty import PromotePageProperty


class PromotePageDetail(object):

    def __init__(self):
        self._gmt_create = None
        self._id = None
        self._name = None
        self._property_list = None
        self._type = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
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
    def property_list(self):
        return self._property_list

    @property_list.setter
    def property_list(self, value):
        if isinstance(value, list):
            self._property_list = list()
            for i in value:
                if isinstance(i, PromotePageProperty):
                    self._property_list.append(i)
                else:
                    self._property_list.append(PromotePageProperty.from_alipay_dict(i))
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
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
        if self.property_list:
            if isinstance(self.property_list, list):
                for i in range(0, len(self.property_list)):
                    element = self.property_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_list[i] = element.to_alipay_dict()
            if hasattr(self.property_list, 'to_alipay_dict'):
                params['property_list'] = self.property_list.to_alipay_dict()
            else:
                params['property_list'] = self.property_list
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
        o = PromotePageDetail()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'property_list' in d:
            o.property_list = d['property_list']
        if 'type' in d:
            o.type = d['type']
        return o


