#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniMarketMultibundleConsultModel(object):

    def __init__(self):
        self._bundle_id = None
        self._mini_app_id = None
        self._scenes = None
        self._user_id = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def scenes(self):
        return self._scenes

    @scenes.setter
    def scenes(self, value):
        self._scenes = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.scenes:
            if hasattr(self.scenes, 'to_alipay_dict'):
                params['scenes'] = self.scenes.to_alipay_dict()
            else:
                params['scenes'] = self.scenes
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMarketMultibundleConsultModel()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'scenes' in d:
            o.scenes = d['scenes']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


