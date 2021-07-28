#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMultimediaXnnminiBizCreateModel(object):

    def __init__(self):
        self._des = None
        self._mini_app_id = None
        self._name = None
        self._user_id = None

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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = AlipayMultimediaXnnminiBizCreateModel()
        if 'des' in d:
            o.des = d['des']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'name' in d:
            o.name = d['name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


