#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozAuthenticationCustomerFaceverifyMatchModel(object):

    def __init__(self):
        self._auth_img = None
        self._auth_img_channel = None
        self._biz_id = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._merchant_uid = None
        self._ref_img = None
        self._type = None

    @property
    def auth_img(self):
        return self._auth_img

    @auth_img.setter
    def auth_img(self, value):
        self._auth_img = value
    @property
    def auth_img_channel(self):
        return self._auth_img_channel

    @auth_img_channel.setter
    def auth_img_channel(self, value):
        self._auth_img_channel = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def merchant_uid(self):
        return self._merchant_uid

    @merchant_uid.setter
    def merchant_uid(self, value):
        self._merchant_uid = value
    @property
    def ref_img(self):
        return self._ref_img

    @ref_img.setter
    def ref_img(self, value):
        self._ref_img = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_img:
            if hasattr(self.auth_img, 'to_alipay_dict'):
                params['auth_img'] = self.auth_img.to_alipay_dict()
            else:
                params['auth_img'] = self.auth_img
        if self.auth_img_channel:
            if hasattr(self.auth_img_channel, 'to_alipay_dict'):
                params['auth_img_channel'] = self.auth_img_channel.to_alipay_dict()
            else:
                params['auth_img_channel'] = self.auth_img_channel
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.merchant_uid:
            if hasattr(self.merchant_uid, 'to_alipay_dict'):
                params['merchant_uid'] = self.merchant_uid.to_alipay_dict()
            else:
                params['merchant_uid'] = self.merchant_uid
        if self.ref_img:
            if hasattr(self.ref_img, 'to_alipay_dict'):
                params['ref_img'] = self.ref_img.to_alipay_dict()
            else:
                params['ref_img'] = self.ref_img
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationCustomerFaceverifyMatchModel()
        if 'auth_img' in d:
            o.auth_img = d['auth_img']
        if 'auth_img_channel' in d:
            o.auth_img_channel = d['auth_img_channel']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'merchant_uid' in d:
            o.merchant_uid = d['merchant_uid']
        if 'ref_img' in d:
            o.ref_img = d['ref_img']
        if 'type' in d:
            o.type = d['type']
        return o


