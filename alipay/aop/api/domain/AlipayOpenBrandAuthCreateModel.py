#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandAuthAdditionalInfoOpenApi import BrandAuthAdditionalInfoOpenApi
from alipay.aop.api.domain.BrandAuthMaterialInfoOpenApi import BrandAuthMaterialInfoOpenApi


class AlipayOpenBrandAuthCreateModel(object):

    def __init__(self):
        self._brand_additional_info = None
        self._brand_auth_material = None
        self._brand_id = None

    @property
    def brand_additional_info(self):
        return self._brand_additional_info

    @brand_additional_info.setter
    def brand_additional_info(self, value):
        if isinstance(value, BrandAuthAdditionalInfoOpenApi):
            self._brand_additional_info = value
        else:
            self._brand_additional_info = BrandAuthAdditionalInfoOpenApi.from_alipay_dict(value)
    @property
    def brand_auth_material(self):
        return self._brand_auth_material

    @brand_auth_material.setter
    def brand_auth_material(self, value):
        if isinstance(value, BrandAuthMaterialInfoOpenApi):
            self._brand_auth_material = value
        else:
            self._brand_auth_material = BrandAuthMaterialInfoOpenApi.from_alipay_dict(value)
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_additional_info:
            if hasattr(self.brand_additional_info, 'to_alipay_dict'):
                params['brand_additional_info'] = self.brand_additional_info.to_alipay_dict()
            else:
                params['brand_additional_info'] = self.brand_additional_info
        if self.brand_auth_material:
            if hasattr(self.brand_auth_material, 'to_alipay_dict'):
                params['brand_auth_material'] = self.brand_auth_material.to_alipay_dict()
            else:
                params['brand_auth_material'] = self.brand_auth_material
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenBrandAuthCreateModel()
        if 'brand_additional_info' in d:
            o.brand_additional_info = d['brand_additional_info']
        if 'brand_auth_material' in d:
            o.brand_auth_material = d['brand_auth_material']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        return o


