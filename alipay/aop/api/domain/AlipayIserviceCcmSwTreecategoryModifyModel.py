#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmSwTreecategoryModifyModel(object):

    def __init__(self):
        self._ccs_instance_id = None
        self._description = None
        self._father_id = None
        self._id = None
        self._name = None
        self._tags = None

    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def father_id(self):
        return self._father_id

    @father_id.setter
    def father_id(self, value):
        self._father_id = value
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
        self._tags = value


    def to_alipay_dict(self):
        params = dict()
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.father_id:
            if hasattr(self.father_id, 'to_alipay_dict'):
                params['father_id'] = self.father_id.to_alipay_dict()
            else:
                params['father_id'] = self.father_id
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
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmSwTreecategoryModifyModel()
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'description' in d:
            o.description = d['description']
        if 'father_id' in d:
            o.father_id = d['father_id']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'tags' in d:
            o.tags = d['tags']
        return o


