#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBusinessFrontpluginRequestIdentifyModel(object):

    def __init__(self):
        self._operator_id = None
        self._operator_master_id = None
        self._operator_type = None
        self._params = None
        self._plugin_id = None
        self._service_id = None

    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_master_id(self):
        return self._operator_master_id

    @operator_master_id.setter
    def operator_master_id(self, value):
        self._operator_master_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def plugin_id(self):
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, value):
        self._plugin_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_master_id:
            if hasattr(self.operator_master_id, 'to_alipay_dict'):
                params['operator_master_id'] = self.operator_master_id.to_alipay_dict()
            else:
                params['operator_master_id'] = self.operator_master_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.plugin_id:
            if hasattr(self.plugin_id, 'to_alipay_dict'):
                params['plugin_id'] = self.plugin_id.to_alipay_dict()
            else:
                params['plugin_id'] = self.plugin_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessFrontpluginRequestIdentifyModel()
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_master_id' in d:
            o.operator_master_id = d['operator_master_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'params' in d:
            o.params = d['params']
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        return o


