#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BrandCertInfo(object):

    def __init__(self):
        self._brand_cert = None
        self._brand_id = None
        self._brand_name_cn = None
        self._brand_name_en = None

    @property
    def brand_cert(self):
        return self._brand_cert

    @brand_cert.setter
    def brand_cert(self, value):
        self._brand_cert = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_name_cn(self):
        return self._brand_name_cn

    @brand_name_cn.setter
    def brand_name_cn(self, value):
        self._brand_name_cn = value
    @property
    def brand_name_en(self):
        return self._brand_name_en

    @brand_name_en.setter
    def brand_name_en(self, value):
        self._brand_name_en = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_cert:
            if hasattr(self.brand_cert, 'to_alipay_dict'):
                params['brand_cert'] = self.brand_cert.to_alipay_dict()
            else:
                params['brand_cert'] = self.brand_cert
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_name_cn:
            if hasattr(self.brand_name_cn, 'to_alipay_dict'):
                params['brand_name_cn'] = self.brand_name_cn.to_alipay_dict()
            else:
                params['brand_name_cn'] = self.brand_name_cn
        if self.brand_name_en:
            if hasattr(self.brand_name_en, 'to_alipay_dict'):
                params['brand_name_en'] = self.brand_name_en.to_alipay_dict()
            else:
                params['brand_name_en'] = self.brand_name_en
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandCertInfo()
        if 'brand_cert' in d:
            o.brand_cert = d['brand_cert']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name_cn' in d:
            o.brand_name_cn = d['brand_name_cn']
        if 'brand_name_en' in d:
            o.brand_name_en = d['brand_name_en']
        return o


