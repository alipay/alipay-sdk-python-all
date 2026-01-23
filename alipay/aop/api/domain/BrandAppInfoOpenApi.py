#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BrandAppInfoOpenApi(object):

    def __init__(self):
        self._app_id_b = None
        self._app_name = None
        self._app_type = None

    @property
    def app_id_b(self):
        return self._app_id_b

    @app_id_b.setter
    def app_id_b(self, value):
        self._app_id_b = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_id_b:
            if hasattr(self.app_id_b, 'to_alipay_dict'):
                params['app_id_b'] = self.app_id_b.to_alipay_dict()
            else:
                params['app_id_b'] = self.app_id_b
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandAppInfoOpenApi()
        if 'app_id_b' in d:
            o.app_id_b = d['app_id_b']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_type' in d:
            o.app_type = d['app_type']
        return o


