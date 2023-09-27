#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCommonUsertaxbillsignCreateModel(object):

    def __init__(self):
        self._back_url = None
        self._sign_user_id = None
        self._sign_user_open_id = None

    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def sign_user_id(self):
        return self._sign_user_id

    @sign_user_id.setter
    def sign_user_id(self, value):
        self._sign_user_id = value
    @property
    def sign_user_open_id(self):
        return self._sign_user_open_id

    @sign_user_open_id.setter
    def sign_user_open_id(self, value):
        self._sign_user_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.sign_user_id:
            if hasattr(self.sign_user_id, 'to_alipay_dict'):
                params['sign_user_id'] = self.sign_user_id.to_alipay_dict()
            else:
                params['sign_user_id'] = self.sign_user_id
        if self.sign_user_open_id:
            if hasattr(self.sign_user_open_id, 'to_alipay_dict'):
                params['sign_user_open_id'] = self.sign_user_open_id.to_alipay_dict()
            else:
                params['sign_user_open_id'] = self.sign_user_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommonUsertaxbillsignCreateModel()
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'sign_user_id' in d:
            o.sign_user_id = d['sign_user_id']
        if 'sign_user_open_id' in d:
            o.sign_user_open_id = d['sign_user_open_id']
        return o


