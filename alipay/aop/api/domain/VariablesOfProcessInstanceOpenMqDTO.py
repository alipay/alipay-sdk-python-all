#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VariablesOfProcessInstanceOpenMqDTO(object):

    def __init__(self):
        self._app_key = None
        self._create_time = None
        self._group_id = None
        self._name = None
        self._process_instance_id = None
        self._update_time = None
        self._value = None
        self._variable_id = None

    @property
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def process_instance_id(self):
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, value):
        self._process_instance_id = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
    @property
    def variable_id(self):
        return self._variable_id

    @variable_id.setter
    def variable_id(self, value):
        self._variable_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_key:
            if hasattr(self.app_key, 'to_alipay_dict'):
                params['app_key'] = self.app_key.to_alipay_dict()
            else:
                params['app_key'] = self.app_key
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.process_instance_id:
            if hasattr(self.process_instance_id, 'to_alipay_dict'):
                params['process_instance_id'] = self.process_instance_id.to_alipay_dict()
            else:
                params['process_instance_id'] = self.process_instance_id
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        if self.variable_id:
            if hasattr(self.variable_id, 'to_alipay_dict'):
                params['variable_id'] = self.variable_id.to_alipay_dict()
            else:
                params['variable_id'] = self.variable_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VariablesOfProcessInstanceOpenMqDTO()
        if 'app_key' in d:
            o.app_key = d['app_key']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'name' in d:
            o.name = d['name']
        if 'process_instance_id' in d:
            o.process_instance_id = d['process_instance_id']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'value' in d:
            o.value = d['value']
        if 'variable_id' in d:
            o.variable_id = d['variable_id']
        return o


