#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcoMockGroupInfo(object):

    def __init__(self):
        self._app_code = None
        self._description = None
        self._id = None
        self._mock_count = None
        self._name = None
        self._status = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def mock_count(self):
        return self._mock_count

    @mock_count.setter
    def mock_count(self, value):
        self._mock_count = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.mock_count:
            if hasattr(self.mock_count, 'to_alipay_dict'):
                params['mock_count'] = self.mock_count.to_alipay_dict()
            else:
                params['mock_count'] = self.mock_count
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = EcoMockGroupInfo()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'description' in d:
            o.description = d['description']
        if 'id' in d:
            o.id = d['id']
        if 'mock_count' in d:
            o.mock_count = d['mock_count']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        return o


