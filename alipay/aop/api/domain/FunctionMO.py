#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FunctionMO(object):

    def __init__(self):
        self._description = None
        self._function_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._image_name = None
        self._quota_name = None
        self._status = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def image_name(self):
        return self._image_name

    @image_name.setter
    def image_name(self, value):
        self._image_name = value
    @property
    def quota_name(self):
        return self._quota_name

    @quota_name.setter
    def quota_name(self, value):
        self._quota_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.image_name:
            if hasattr(self.image_name, 'to_alipay_dict'):
                params['image_name'] = self.image_name.to_alipay_dict()
            else:
                params['image_name'] = self.image_name
        if self.quota_name:
            if hasattr(self.quota_name, 'to_alipay_dict'):
                params['quota_name'] = self.quota_name.to_alipay_dict()
            else:
                params['quota_name'] = self.quota_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FunctionMO()
        if 'description' in d:
            o.description = d['description']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'image_name' in d:
            o.image_name = d['image_name']
        if 'quota_name' in d:
            o.quota_name = d['quota_name']
        if 'status' in d:
            o.status = d['status']
        return o


