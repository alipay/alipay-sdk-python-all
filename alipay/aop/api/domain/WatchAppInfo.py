#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WatchAppInfo(object):

    def __init__(self):
        self._app_name = None
        self._app_status_code = None
        self._app_status_desc = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_status_code(self):
        return self._app_status_code

    @app_status_code.setter
    def app_status_code(self, value):
        self._app_status_code = value
    @property
    def app_status_desc(self):
        return self._app_status_desc

    @app_status_desc.setter
    def app_status_desc(self, value):
        self._app_status_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_status_code:
            if hasattr(self.app_status_code, 'to_alipay_dict'):
                params['app_status_code'] = self.app_status_code.to_alipay_dict()
            else:
                params['app_status_code'] = self.app_status_code
        if self.app_status_desc:
            if hasattr(self.app_status_desc, 'to_alipay_dict'):
                params['app_status_desc'] = self.app_status_desc.to_alipay_dict()
            else:
                params['app_status_desc'] = self.app_status_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WatchAppInfo()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_status_code' in d:
            o.app_status_code = d['app_status_code']
        if 'app_status_desc' in d:
            o.app_status_desc = d['app_status_desc']
        return o


