#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundUserinfoCheckModel(object):

    def __init__(self):
        self._biz_scene = None
        self._encrypted_user_info = None
        self._open_id = None
        self._product_code = None
        self._salt = None
        self._user_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def encrypted_user_info(self):
        return self._encrypted_user_info

    @encrypted_user_info.setter
    def encrypted_user_info(self, value):
        self._encrypted_user_info = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def salt(self):
        return self._salt

    @salt.setter
    def salt(self, value):
        self._salt = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.encrypted_user_info:
            if hasattr(self.encrypted_user_info, 'to_alipay_dict'):
                params['encrypted_user_info'] = self.encrypted_user_info.to_alipay_dict()
            else:
                params['encrypted_user_info'] = self.encrypted_user_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.salt:
            if hasattr(self.salt, 'to_alipay_dict'):
                params['salt'] = self.salt.to_alipay_dict()
            else:
                params['salt'] = self.salt
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
        o = AlipayFundUserinfoCheckModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'encrypted_user_info' in d:
            o.encrypted_user_info = d['encrypted_user_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'salt' in d:
            o.salt = d['salt']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


