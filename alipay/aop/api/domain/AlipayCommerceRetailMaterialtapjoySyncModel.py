#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailMaterialtapjoySyncModel(object):

    def __init__(self):
        self._ad_id = None
        self._brand_name = None
        self._material_url = None

    @property
    def ad_id(self):
        return self._ad_id

    @ad_id.setter
    def ad_id(self, value):
        self._ad_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def material_url(self):
        return self._material_url

    @material_url.setter
    def material_url(self, value):
        self._material_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_id:
            if hasattr(self.ad_id, 'to_alipay_dict'):
                params['ad_id'] = self.ad_id.to_alipay_dict()
            else:
                params['ad_id'] = self.ad_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.material_url:
            if hasattr(self.material_url, 'to_alipay_dict'):
                params['material_url'] = self.material_url.to_alipay_dict()
            else:
                params['material_url'] = self.material_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailMaterialtapjoySyncModel()
        if 'ad_id' in d:
            o.ad_id = d['ad_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'material_url' in d:
            o.material_url = d['material_url']
        return o


