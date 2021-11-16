#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerappPluginsyncmodeModifyModel(object):

    def __init__(self):
        self._app_origin = None
        self._mini_app_id = None
        self._plugin_id = None
        self._sync_mode = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
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
    def sync_mode(self):
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, value):
        self._sync_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
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
        if self.sync_mode:
            if hasattr(self.sync_mode, 'to_alipay_dict'):
                params['sync_mode'] = self.sync_mode.to_alipay_dict()
            else:
                params['sync_mode'] = self.sync_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerappPluginsyncmodeModifyModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'sync_mode' in d:
            o.sync_mode = d['sync_mode']
        return o


