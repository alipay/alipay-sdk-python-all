#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseIdeConfigGetModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._key_expire_time = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def key_expire_time(self):
        return self._key_expire_time

    @key_expire_time.setter
    def key_expire_time(self, value):
        self._key_expire_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.key_expire_time:
            if hasattr(self.key_expire_time, 'to_alipay_dict'):
                params['key_expire_time'] = self.key_expire_time.to_alipay_dict()
            else:
                params['key_expire_time'] = self.key_expire_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseIdeConfigGetModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'key_expire_time' in d:
            o.key_expire_time = d['key_expire_time']
        return o


