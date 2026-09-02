#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PluginPrivacyFields(object):

    def __init__(self):
        self._code = None
        self._name = None
        self._plugin_name = None
        self._plugin_provider_name = None
        self._purpose = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def plugin_name(self):
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, value):
        self._plugin_name = value
    @property
    def plugin_provider_name(self):
        return self._plugin_provider_name

    @plugin_provider_name.setter
    def plugin_provider_name(self, value):
        self._plugin_provider_name = value
    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, value):
        self._purpose = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.plugin_name:
            if hasattr(self.plugin_name, 'to_alipay_dict'):
                params['plugin_name'] = self.plugin_name.to_alipay_dict()
            else:
                params['plugin_name'] = self.plugin_name
        if self.plugin_provider_name:
            if hasattr(self.plugin_provider_name, 'to_alipay_dict'):
                params['plugin_provider_name'] = self.plugin_provider_name.to_alipay_dict()
            else:
                params['plugin_provider_name'] = self.plugin_provider_name
        if self.purpose:
            if hasattr(self.purpose, 'to_alipay_dict'):
                params['purpose'] = self.purpose.to_alipay_dict()
            else:
                params['purpose'] = self.purpose
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PluginPrivacyFields()
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        if 'plugin_name' in d:
            o.plugin_name = d['plugin_name']
        if 'plugin_provider_name' in d:
            o.plugin_provider_name = d['plugin_provider_name']
        if 'purpose' in d:
            o.purpose = d['purpose']
        return o


