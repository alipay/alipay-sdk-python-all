#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalSearchDepartmentQueryModel(object):

    def __init__(self):
        self._channel_code = None
        self._key_type = None
        self._page_key = None
        self._scene_code = None

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def key_type(self):
        return self._key_type

    @key_type.setter
    def key_type(self, value):
        self._key_type = value
    @property
    def page_key(self):
        return self._page_key

    @page_key.setter
    def page_key(self, value):
        self._page_key = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.key_type:
            if hasattr(self.key_type, 'to_alipay_dict'):
                params['key_type'] = self.key_type.to_alipay_dict()
            else:
                params['key_type'] = self.key_type
        if self.page_key:
            if hasattr(self.page_key, 'to_alipay_dict'):
                params['page_key'] = self.page_key.to_alipay_dict()
            else:
                params['page_key'] = self.page_key
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalSearchDepartmentQueryModel()
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'key_type' in d:
            o.key_type = d['key_type']
        if 'page_key' in d:
            o.page_key = d['page_key']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


