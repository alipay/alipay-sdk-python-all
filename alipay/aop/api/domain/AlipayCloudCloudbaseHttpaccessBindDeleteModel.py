#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseHttpaccessBindDeleteModel(object):

    def __init__(self):
        self._bind_id = None
        self._biz_app_id = None
        self._biz_env_id = None

    @property
    def bind_id(self):
        return self._bind_id

    @bind_id.setter
    def bind_id(self, value):
        self._bind_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.bind_id:
            if hasattr(self.bind_id, 'to_alipay_dict'):
                params['bind_id'] = self.bind_id.to_alipay_dict()
            else:
                params['bind_id'] = self.bind_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseHttpaccessBindDeleteModel()
        if 'bind_id' in d:
            o.bind_id = d['bind_id']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        return o

