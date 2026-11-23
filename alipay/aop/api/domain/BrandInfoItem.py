#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BrandInfoItem(object):

    def __init__(self):
        self._brand_chs_name = None
        self._brand_eng_name = None
        self._brand_id = None
        self._brand_name = None
        self._logo_url = None

    @property
    def brand_chs_name(self):
        return self._brand_chs_name

    @brand_chs_name.setter
    def brand_chs_name(self, value):
        self._brand_chs_name = value
    @property
    def brand_eng_name(self):
        return self._brand_eng_name

    @brand_eng_name.setter
    def brand_eng_name(self, value):
        self._brand_eng_name = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_chs_name:
            if hasattr(self.brand_chs_name, 'to_alipay_dict'):
                params['brand_chs_name'] = self.brand_chs_name.to_alipay_dict()
            else:
                params['brand_chs_name'] = self.brand_chs_name
        if self.brand_eng_name:
            if hasattr(self.brand_eng_name, 'to_alipay_dict'):
                params['brand_eng_name'] = self.brand_eng_name.to_alipay_dict()
            else:
                params['brand_eng_name'] = self.brand_eng_name
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandInfoItem()
        if 'brand_chs_name' in d:
            o.brand_chs_name = d['brand_chs_name']
        if 'brand_eng_name' in d:
            o.brand_eng_name = d['brand_eng_name']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        return o


