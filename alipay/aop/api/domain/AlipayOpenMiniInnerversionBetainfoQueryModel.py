#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerversionBetainfoQueryModel(object):

    def __init__(self):
        self._app_origin = None
        self._bundle_id = None
        self._plugin_id = None
        self._plugin_version = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
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
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
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
        o = AlipayOpenMiniInnerversionBetainfoQueryModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'plugin_version' in d:
            o.plugin_version = d['plugin_version']
        return o


