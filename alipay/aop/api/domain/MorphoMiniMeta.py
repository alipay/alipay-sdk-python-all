#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MorphoMiniMeta(object):

    def __init__(self):
        self._app_name = None
        self._builded_version = None
        self._logo = None
        self._mini_app_id = None
        self._online_version = None
        self._status = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def builded_version(self):
        return self._builded_version

    @builded_version.setter
    def builded_version(self, value):
        self._builded_version = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def online_version(self):
        return self._online_version

    @online_version.setter
    def online_version(self, value):
        self._online_version = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.builded_version:
            if hasattr(self.builded_version, 'to_alipay_dict'):
                params['builded_version'] = self.builded_version.to_alipay_dict()
            else:
                params['builded_version'] = self.builded_version
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.online_version:
            if hasattr(self.online_version, 'to_alipay_dict'):
                params['online_version'] = self.online_version.to_alipay_dict()
            else:
                params['online_version'] = self.online_version
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
        o = MorphoMiniMeta()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'builded_version' in d:
            o.builded_version = d['builded_version']
        if 'logo' in d:
            o.logo = d['logo']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'online_version' in d:
            o.online_version = d['online_version']
        if 'status' in d:
            o.status = d['status']
        return o


