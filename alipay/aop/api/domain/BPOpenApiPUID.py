#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BPOpenApiPUID(object):

    def __init__(self):
        self._app_name = None
        self._biz_id = None
        self._biz_type = None
        self._unique_key = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def unique_key(self):
        return self._unique_key

    @unique_key.setter
    def unique_key(self, value):
        self._unique_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.unique_key:
            if hasattr(self.unique_key, 'to_alipay_dict'):
                params['unique_key'] = self.unique_key.to_alipay_dict()
            else:
                params['unique_key'] = self.unique_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BPOpenApiPUID()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'unique_key' in d:
            o.unique_key = d['unique_key']
        return o


