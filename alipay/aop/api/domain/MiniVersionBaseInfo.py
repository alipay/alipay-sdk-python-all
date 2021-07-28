#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniVersionBaseInfo(object):

    def __init__(self):
        self._app_version = None
        self._build_source = None
        self._bundle_id = None
        self._dev_id = None
        self._gray_strategy = None
        self._mini_app_id = None
        self._status = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def build_source(self):
        return self._build_source

    @build_source.setter
    def build_source(self, value):
        self._build_source = value
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
    def gray_strategy(self):
        return self._gray_strategy

    @gray_strategy.setter
    def gray_strategy(self, value):
        self._gray_strategy = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.build_source:
            if hasattr(self.build_source, 'to_alipay_dict'):
                params['build_source'] = self.build_source.to_alipay_dict()
            else:
                params['build_source'] = self.build_source
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
        if self.gray_strategy:
            if hasattr(self.gray_strategy, 'to_alipay_dict'):
                params['gray_strategy'] = self.gray_strategy.to_alipay_dict()
            else:
                params['gray_strategy'] = self.gray_strategy
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
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
        o = MiniVersionBaseInfo()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'build_source' in d:
            o.build_source = d['build_source']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'gray_strategy' in d:
            o.gray_strategy = d['gray_strategy']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'status' in d:
            o.status = d['status']
        return o


