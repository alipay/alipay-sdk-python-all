#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateUsageInfo(object):

    def __init__(self):
        self._app_version = None
        self._mini_app_id = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
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
        o = TemplateUsageInfo()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        return o


