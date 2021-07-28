#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PluginUseConfigInfo(object):

    def __init__(self):
        self._bundle_id = None
        self._gray_code = None
        self._plugin_develop_version = None
        self._status = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def gray_code(self):
        return self._gray_code

    @gray_code.setter
    def gray_code(self, value):
        self._gray_code = value
    @property
    def plugin_develop_version(self):
        return self._plugin_develop_version

    @plugin_develop_version.setter
    def plugin_develop_version(self, value):
        self._plugin_develop_version = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.gray_code:
            if hasattr(self.gray_code, 'to_alipay_dict'):
                params['gray_code'] = self.gray_code.to_alipay_dict()
            else:
                params['gray_code'] = self.gray_code
        if self.plugin_develop_version:
            if hasattr(self.plugin_develop_version, 'to_alipay_dict'):
                params['plugin_develop_version'] = self.plugin_develop_version.to_alipay_dict()
            else:
                params['plugin_develop_version'] = self.plugin_develop_version
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
        o = PluginUseConfigInfo()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'gray_code' in d:
            o.gray_code = d['gray_code']
        if 'plugin_develop_version' in d:
            o.plugin_develop_version = d['plugin_develop_version']
        if 'status' in d:
            o.status = d['status']
        return o


