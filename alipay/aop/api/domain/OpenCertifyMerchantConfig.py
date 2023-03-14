#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenCertifyMerchantConfig(object):

    def __init__(self):
        self._auth_scope = None
        self._auth_type = None
        self._face_reserve_strategy = None
        self._facial_picture_level = None
        self._linked_merchant_app_id = None
        self._linked_merchant_logo_url = None
        self._linked_merchant_name = None
        self._out_put_facial_picture = None
        self._return_url = None

    @property
    def auth_scope(self):
        return self._auth_scope

    @auth_scope.setter
    def auth_scope(self, value):
        self._auth_scope = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def face_reserve_strategy(self):
        return self._face_reserve_strategy

    @face_reserve_strategy.setter
    def face_reserve_strategy(self, value):
        self._face_reserve_strategy = value
    @property
    def facial_picture_level(self):
        return self._facial_picture_level

    @facial_picture_level.setter
    def facial_picture_level(self, value):
        self._facial_picture_level = value
    @property
    def linked_merchant_app_id(self):
        return self._linked_merchant_app_id

    @linked_merchant_app_id.setter
    def linked_merchant_app_id(self, value):
        self._linked_merchant_app_id = value
    @property
    def linked_merchant_logo_url(self):
        return self._linked_merchant_logo_url

    @linked_merchant_logo_url.setter
    def linked_merchant_logo_url(self, value):
        self._linked_merchant_logo_url = value
    @property
    def linked_merchant_name(self):
        return self._linked_merchant_name

    @linked_merchant_name.setter
    def linked_merchant_name(self, value):
        self._linked_merchant_name = value
    @property
    def out_put_facial_picture(self):
        return self._out_put_facial_picture

    @out_put_facial_picture.setter
    def out_put_facial_picture(self, value):
        self._out_put_facial_picture = value
    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_scope:
            if hasattr(self.auth_scope, 'to_alipay_dict'):
                params['auth_scope'] = self.auth_scope.to_alipay_dict()
            else:
                params['auth_scope'] = self.auth_scope
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.face_reserve_strategy:
            if hasattr(self.face_reserve_strategy, 'to_alipay_dict'):
                params['face_reserve_strategy'] = self.face_reserve_strategy.to_alipay_dict()
            else:
                params['face_reserve_strategy'] = self.face_reserve_strategy
        if self.facial_picture_level:
            if hasattr(self.facial_picture_level, 'to_alipay_dict'):
                params['facial_picture_level'] = self.facial_picture_level.to_alipay_dict()
            else:
                params['facial_picture_level'] = self.facial_picture_level
        if self.linked_merchant_app_id:
            if hasattr(self.linked_merchant_app_id, 'to_alipay_dict'):
                params['linked_merchant_app_id'] = self.linked_merchant_app_id.to_alipay_dict()
            else:
                params['linked_merchant_app_id'] = self.linked_merchant_app_id
        if self.linked_merchant_logo_url:
            if hasattr(self.linked_merchant_logo_url, 'to_alipay_dict'):
                params['linked_merchant_logo_url'] = self.linked_merchant_logo_url.to_alipay_dict()
            else:
                params['linked_merchant_logo_url'] = self.linked_merchant_logo_url
        if self.linked_merchant_name:
            if hasattr(self.linked_merchant_name, 'to_alipay_dict'):
                params['linked_merchant_name'] = self.linked_merchant_name.to_alipay_dict()
            else:
                params['linked_merchant_name'] = self.linked_merchant_name
        if self.out_put_facial_picture:
            if hasattr(self.out_put_facial_picture, 'to_alipay_dict'):
                params['out_put_facial_picture'] = self.out_put_facial_picture.to_alipay_dict()
            else:
                params['out_put_facial_picture'] = self.out_put_facial_picture
        if self.return_url:
            if hasattr(self.return_url, 'to_alipay_dict'):
                params['return_url'] = self.return_url.to_alipay_dict()
            else:
                params['return_url'] = self.return_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenCertifyMerchantConfig()
        if 'auth_scope' in d:
            o.auth_scope = d['auth_scope']
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'face_reserve_strategy' in d:
            o.face_reserve_strategy = d['face_reserve_strategy']
        if 'facial_picture_level' in d:
            o.facial_picture_level = d['facial_picture_level']
        if 'linked_merchant_app_id' in d:
            o.linked_merchant_app_id = d['linked_merchant_app_id']
        if 'linked_merchant_logo_url' in d:
            o.linked_merchant_logo_url = d['linked_merchant_logo_url']
        if 'linked_merchant_name' in d:
            o.linked_merchant_name = d['linked_merchant_name']
        if 'out_put_facial_picture' in d:
            o.out_put_facial_picture = d['out_put_facial_picture']
        if 'return_url' in d:
            o.return_url = d['return_url']
        return o


