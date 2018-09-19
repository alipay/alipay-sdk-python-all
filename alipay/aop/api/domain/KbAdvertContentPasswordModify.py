#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertContentPasswordModify(object):

    def __init__(self):
        self._background_img_id = None
        self._brand_name = None
        self._password = None
        self._voucher_logo_id = None

    @property
    def background_img_id(self):
        return self._background_img_id

    @background_img_id.setter
    def background_img_id(self, value):
        self._background_img_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    @property
    def voucher_logo_id(self):
        return self._voucher_logo_id

    @voucher_logo_id.setter
    def voucher_logo_id(self, value):
        self._voucher_logo_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.background_img_id:
            if hasattr(self.background_img_id, 'to_alipay_dict'):
                params['background_img_id'] = self.background_img_id.to_alipay_dict()
            else:
                params['background_img_id'] = self.background_img_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.password:
            if hasattr(self.password, 'to_alipay_dict'):
                params['password'] = self.password.to_alipay_dict()
            else:
                params['password'] = self.password
        if self.voucher_logo_id:
            if hasattr(self.voucher_logo_id, 'to_alipay_dict'):
                params['voucher_logo_id'] = self.voucher_logo_id.to_alipay_dict()
            else:
                params['voucher_logo_id'] = self.voucher_logo_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertContentPasswordModify()
        if 'background_img_id' in d:
            o.background_img_id = d['background_img_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'password' in d:
            o.password = d['password']
        if 'voucher_logo_id' in d:
            o.voucher_logo_id = d['voucher_logo_id']
        return o


