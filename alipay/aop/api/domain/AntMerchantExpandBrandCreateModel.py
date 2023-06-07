#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandBrandCreateModel(object):

    def __init__(self):
        self._brand_chs_name = None
        self._brand_eng_name = None
        self._carrier_id = None
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
    def carrier_id(self):
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, value):
        self._carrier_id = value
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
        if self.carrier_id:
            if hasattr(self.carrier_id, 'to_alipay_dict'):
                params['carrier_id'] = self.carrier_id.to_alipay_dict()
            else:
                params['carrier_id'] = self.carrier_id
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
        o = AntMerchantExpandBrandCreateModel()
        if 'brand_chs_name' in d:
            o.brand_chs_name = d['brand_chs_name']
        if 'brand_eng_name' in d:
            o.brand_eng_name = d['brand_eng_name']
        if 'carrier_id' in d:
            o.carrier_id = d['carrier_id']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        return o


