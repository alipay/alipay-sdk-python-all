#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppBasicInfoResponse(object):

    def __init__(self):
        self._open_app_id = None
        self._open_app_name = None
        self._open_app_type = None

    @property
    def open_app_id(self):
        return self._open_app_id

    @open_app_id.setter
    def open_app_id(self, value):
        self._open_app_id = value
    @property
    def open_app_name(self):
        return self._open_app_name

    @open_app_name.setter
    def open_app_name(self, value):
        self._open_app_name = value
    @property
    def open_app_type(self):
        return self._open_app_type

    @open_app_type.setter
    def open_app_type(self, value):
        self._open_app_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_app_id:
            if hasattr(self.open_app_id, 'to_alipay_dict'):
                params['open_app_id'] = self.open_app_id.to_alipay_dict()
            else:
                params['open_app_id'] = self.open_app_id
        if self.open_app_name:
            if hasattr(self.open_app_name, 'to_alipay_dict'):
                params['open_app_name'] = self.open_app_name.to_alipay_dict()
            else:
                params['open_app_name'] = self.open_app_name
        if self.open_app_type:
            if hasattr(self.open_app_type, 'to_alipay_dict'):
                params['open_app_type'] = self.open_app_type.to_alipay_dict()
            else:
                params['open_app_type'] = self.open_app_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppBasicInfoResponse()
        if 'open_app_id' in d:
            o.open_app_id = d['open_app_id']
        if 'open_app_name' in d:
            o.open_app_name = d['open_app_name']
        if 'open_app_type' in d:
            o.open_app_type = d['open_app_type']
        return o


