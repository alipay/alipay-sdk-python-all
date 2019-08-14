#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppPluginReference(object):

    def __init__(self):
        self._plugin_id = None
        self._plugin_version = None

    @property
    def plugin_id(self):
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, value):
        self._plugin_id = value
    @property
    def plugin_version(self):
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, value):
        self._plugin_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.plugin_id:
            if hasattr(self.plugin_id, 'to_alipay_dict'):
                params['plugin_id'] = self.plugin_id.to_alipay_dict()
            else:
                params['plugin_id'] = self.plugin_id
        if self.plugin_version:
            if hasattr(self.plugin_version, 'to_alipay_dict'):
                params['plugin_version'] = self.plugin_version.to_alipay_dict()
            else:
                params['plugin_version'] = self.plugin_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppPluginReference()
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'plugin_version' in d:
            o.plugin_version = d['plugin_version']
        return o


