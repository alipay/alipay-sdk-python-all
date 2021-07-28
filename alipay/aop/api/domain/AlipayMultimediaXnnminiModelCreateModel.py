#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMultimediaXnnminiModelCreateModel(object):

    def __init__(self):
        self._biz_id = None
        self._des = None
        self._license = None
        self._mini_app_id = None
        self._name = None
        self._ori_url = None
        self._type = None
        self._user_id = None
        self._version_id = None

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
    def license(self):
        return self._license

    @license.setter
    def license(self, value):
        self._license = value
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
    def ori_url(self):
        return self._ori_url

    @ori_url.setter
    def ori_url(self, value):
        self._ori_url = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def version_id(self):
        return self._version_id

    @version_id.setter
    def version_id(self, value):
        self._version_id = value


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
        if self.license:
            if hasattr(self.license, 'to_alipay_dict'):
                params['license'] = self.license.to_alipay_dict()
            else:
                params['license'] = self.license
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
        if self.ori_url:
            if hasattr(self.ori_url, 'to_alipay_dict'):
                params['ori_url'] = self.ori_url.to_alipay_dict()
            else:
                params['ori_url'] = self.ori_url
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.version_id:
            if hasattr(self.version_id, 'to_alipay_dict'):
                params['version_id'] = self.version_id.to_alipay_dict()
            else:
                params['version_id'] = self.version_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMultimediaXnnminiModelCreateModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'des' in d:
            o.des = d['des']
        if 'license' in d:
            o.license = d['license']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'name' in d:
            o.name = d['name']
        if 'ori_url' in d:
            o.ori_url = d['ori_url']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'version_id' in d:
            o.version_id = d['version_id']
        return o


