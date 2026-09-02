#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozAuthenticationCustomerFaceanonymousCertifyModel(object):

    def __init__(self):
        self._auth_img = None
        self._auth_img_source = None
        self._biz_id = None
        self._merchant_uid = None

    @property
    def auth_img(self):
        return self._auth_img

    @auth_img.setter
    def auth_img(self, value):
        self._auth_img = value
    @property
    def auth_img_source(self):
        return self._auth_img_source

    @auth_img_source.setter
    def auth_img_source(self, value):
        self._auth_img_source = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def merchant_uid(self):
        return self._merchant_uid

    @merchant_uid.setter
    def merchant_uid(self, value):
        self._merchant_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_img:
            if hasattr(self.auth_img, 'to_alipay_dict'):
                params['auth_img'] = self.auth_img.to_alipay_dict()
            else:
                params['auth_img'] = self.auth_img
        if self.auth_img_source:
            if hasattr(self.auth_img_source, 'to_alipay_dict'):
                params['auth_img_source'] = self.auth_img_source.to_alipay_dict()
            else:
                params['auth_img_source'] = self.auth_img_source
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.merchant_uid:
            if hasattr(self.merchant_uid, 'to_alipay_dict'):
                params['merchant_uid'] = self.merchant_uid.to_alipay_dict()
            else:
                params['merchant_uid'] = self.merchant_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationCustomerFaceanonymousCertifyModel()
        if 'auth_img' in d:
            o.auth_img = d['auth_img']
        if 'auth_img_source' in d:
            o.auth_img_source = d['auth_img_source']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'merchant_uid' in d:
            o.merchant_uid = d['merchant_uid']
        return o


