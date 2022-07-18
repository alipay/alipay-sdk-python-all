#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppPluginReference(object):

    def __init__(self):
        self._lazy = None
        self._plugin_id = None
        self._plugin_lazy = None
        self._plugin_version = None

    @property
    def lazy(self):
        return self._lazy

    @lazy.setter
    def lazy(self, value):
        self._lazy = value
    @property
    def plugin_id(self):
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, value):
        self._plugin_id = value
    @property
    def plugin_lazy(self):
        return self._plugin_lazy

    @plugin_lazy.setter
    def plugin_lazy(self, value):
        self._plugin_lazy = value
    @property
    def plugin_version(self):
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, value):
        self._plugin_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.lazy:
            if hasattr(self.lazy, 'to_alipay_dict'):
                params['lazy'] = self.lazy.to_alipay_dict()
            else:
                params['lazy'] = self.lazy
        if self.plugin_id:
            if hasattr(self.plugin_id, 'to_alipay_dict'):
                params['plugin_id'] = self.plugin_id.to_alipay_dict()
            else:
                params['plugin_id'] = self.plugin_id
        if self.plugin_lazy:
            if hasattr(self.plugin_lazy, 'to_alipay_dict'):
                params['plugin_lazy'] = self.plugin_lazy.to_alipay_dict()
            else:
                params['plugin_lazy'] = self.plugin_lazy
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
        if 'lazy' in d:
            o.lazy = d['lazy']
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'plugin_lazy' in d:
            o.plugin_lazy = d['plugin_lazy']
        if 'plugin_version' in d:
            o.plugin_version = d['plugin_version']
        return o


