#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdFacepayVerifyModel(object):

    def __init__(self):
        self._check_code = None
        self._face_image = None
        self._ftoken = None
        self._store_id = None
        self._user_auth_id = None
        self._user_auth_type = None

    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def face_image(self):
        return self._face_image

    @face_image.setter
    def face_image(self, value):
        self._face_image = value
    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def user_auth_id(self):
        return self._user_auth_id

    @user_auth_id.setter
    def user_auth_id(self, value):
        self._user_auth_id = value
    @property
    def user_auth_type(self):
        return self._user_auth_type

    @user_auth_type.setter
    def user_auth_type(self, value):
        self._user_auth_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.face_image:
            if hasattr(self.face_image, 'to_alipay_dict'):
                params['face_image'] = self.face_image.to_alipay_dict()
            else:
                params['face_image'] = self.face_image
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.user_auth_id:
            if hasattr(self.user_auth_id, 'to_alipay_dict'):
                params['user_auth_id'] = self.user_auth_id.to_alipay_dict()
            else:
                params['user_auth_id'] = self.user_auth_id
        if self.user_auth_type:
            if hasattr(self.user_auth_type, 'to_alipay_dict'):
                params['user_auth_type'] = self.user_auth_type.to_alipay_dict()
            else:
                params['user_auth_type'] = self.user_auth_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdFacepayVerifyModel()
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'face_image' in d:
            o.face_image = d['face_image']
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'user_auth_id' in d:
            o.user_auth_id = d['user_auth_id']
        if 'user_auth_type' in d:
            o.user_auth_type = d['user_auth_type']
        return o


