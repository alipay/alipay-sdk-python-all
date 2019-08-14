#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerversionOnlineModel(object):

    def __init__(self):
        self._app_offline_version = None
        self._app_online_version = None
        self._app_origin = None
        self._bundle_id = None
        self._inst_code = None
        self._mini_app_id = None

    @property
    def app_offline_version(self):
        return self._app_offline_version

    @app_offline_version.setter
    def app_offline_version(self, value):
        self._app_offline_version = value
    @property
    def app_online_version(self):
        return self._app_online_version

    @app_online_version.setter
    def app_online_version(self, value):
        self._app_online_version = value
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
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_offline_version:
            if hasattr(self.app_offline_version, 'to_alipay_dict'):
                params['app_offline_version'] = self.app_offline_version.to_alipay_dict()
            else:
                params['app_offline_version'] = self.app_offline_version
        if self.app_online_version:
            if hasattr(self.app_online_version, 'to_alipay_dict'):
                params['app_online_version'] = self.app_online_version.to_alipay_dict()
            else:
                params['app_online_version'] = self.app_online_version
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
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionOnlineModel()
        if 'app_offline_version' in d:
            o.app_offline_version = d['app_offline_version']
        if 'app_online_version' in d:
            o.app_online_version = d['app_online_version']
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        return o


