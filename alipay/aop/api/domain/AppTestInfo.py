#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppTestInfo(object):

    def __init__(self):
        self._app_name = None
        self._app_version = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppTestInfo()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_version' in d:
            o.app_version = d['app_version']
        return o


