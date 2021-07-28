#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PluginBetaItemInfo(object):

    def __init__(self):
        self._app_name = None
        self._beta_status = None
        self._memo = None
        self._mini_app_id = None
        self._plugin_id = None
        self._plugin_version = None
        self._qr_code_url = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def beta_status(self):
        return self._beta_status

    @beta_status.setter
    def beta_status(self, value):
        self._beta_status = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
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
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.beta_status:
            if hasattr(self.beta_status, 'to_alipay_dict'):
                params['beta_status'] = self.beta_status.to_alipay_dict()
            else:
                params['beta_status'] = self.beta_status
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
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
        if self.qr_code_url:
            if hasattr(self.qr_code_url, 'to_alipay_dict'):
                params['qr_code_url'] = self.qr_code_url.to_alipay_dict()
            else:
                params['qr_code_url'] = self.qr_code_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PluginBetaItemInfo()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'beta_status' in d:
            o.beta_status = d['beta_status']
        if 'memo' in d:
            o.memo = d['memo']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'plugin_version' in d:
            o.plugin_version = d['plugin_version']
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        return o


