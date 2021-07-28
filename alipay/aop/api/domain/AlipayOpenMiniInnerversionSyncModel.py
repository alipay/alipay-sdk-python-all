#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerversionSyncModel(object):

    def __init__(self):
        self._app_origin = None
        self._app_version = None
        self._bundle_id = None
        self._dev_id = None
        self._mini_app_id = None
        self._sync_type = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.dev_id:
            if hasattr(self.dev_id, 'to_alipay_dict'):
                params['dev_id'] = self.dev_id.to_alipay_dict()
            else:
                params['dev_id'] = self.dev_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionSyncModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        return o


