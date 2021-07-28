#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMultimediaXnnminiVersionCreateModel(object):

    def __init__(self):
        self._biz_id = None
        self._des = None
        self._mini_app_id = None
        self._model_version = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def des(self):
        return self._des

    @des.setter
    def des(self, value):
        self._des = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def model_version(self):
        return self._model_version

    @model_version.setter
    def model_version(self, value):
        self._model_version = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.des:
            if hasattr(self.des, 'to_alipay_dict'):
                params['des'] = self.des.to_alipay_dict()
            else:
                params['des'] = self.des
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.model_version:
            if hasattr(self.model_version, 'to_alipay_dict'):
                params['model_version'] = self.model_version.to_alipay_dict()
            else:
                params['model_version'] = self.model_version
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
        o = AlipayMultimediaXnnminiVersionCreateModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'des' in d:
            o.des = d['des']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'model_version' in d:
            o.model_version = d['model_version']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


