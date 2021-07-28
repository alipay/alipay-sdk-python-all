#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppPluginInfo(object):

    def __init__(self):
        self._package_url = None
        self._plugin_id = None
        self._require_version = None

    @property
    def package_url(self):
        return self._package_url

    @package_url.setter
    def package_url(self, value):
        self._package_url = value
    @property
    def plugin_id(self):
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, value):
        self._plugin_id = value
    @property
    def require_version(self):
        return self._require_version

    @require_version.setter
    def require_version(self, value):
        self._require_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.package_url:
            if hasattr(self.package_url, 'to_alipay_dict'):
                params['package_url'] = self.package_url.to_alipay_dict()
            else:
                params['package_url'] = self.package_url
        if self.plugin_id:
            if hasattr(self.plugin_id, 'to_alipay_dict'):
                params['plugin_id'] = self.plugin_id.to_alipay_dict()
            else:
                params['plugin_id'] = self.plugin_id
        if self.require_version:
            if hasattr(self.require_version, 'to_alipay_dict'):
                params['require_version'] = self.require_version.to_alipay_dict()
            else:
                params['require_version'] = self.require_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppPluginInfo()
        if 'package_url' in d:
            o.package_url = d['package_url']
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'require_version' in d:
            o.require_version = d['require_version']
        return o


