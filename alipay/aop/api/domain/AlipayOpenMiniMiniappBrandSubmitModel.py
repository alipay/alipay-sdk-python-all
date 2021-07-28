#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthorizeInfo import AuthorizeInfo
from alipay.aop.api.domain.BrandRegistrationInfo import BrandRegistrationInfo


class AlipayOpenMiniMiniappBrandSubmitModel(object):

    def __init__(self):
        self._apply_type = None
        self._authorize_info = None
        self._brand_id = None
        self._brand_name = None
        self._brand_registration_info = None
        self._id_materials = None

    @property
    def apply_type(self):
        return self._apply_type

    @apply_type.setter
    def apply_type(self, value):
        self._apply_type = value
    @property
    def authorize_info(self):
        return self._authorize_info

    @authorize_info.setter
    def authorize_info(self, value):
        if isinstance(value, AuthorizeInfo):
            self._authorize_info = value
        else:
            self._authorize_info = AuthorizeInfo.from_alipay_dict(value)
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
    def brand_registration_info(self):
        return self._brand_registration_info

    @brand_registration_info.setter
    def brand_registration_info(self, value):
        if isinstance(value, BrandRegistrationInfo):
            self._brand_registration_info = value
        else:
            self._brand_registration_info = BrandRegistrationInfo.from_alipay_dict(value)
    @property
    def id_materials(self):
        return self._id_materials

    @id_materials.setter
    def id_materials(self, value):
        if isinstance(value, list):
            self._id_materials = list()
            for i in value:
                self._id_materials.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_type:
            if hasattr(self.apply_type, 'to_alipay_dict'):
                params['apply_type'] = self.apply_type.to_alipay_dict()
            else:
                params['apply_type'] = self.apply_type
        if self.authorize_info:
            if hasattr(self.authorize_info, 'to_alipay_dict'):
                params['authorize_info'] = self.authorize_info.to_alipay_dict()
            else:
                params['authorize_info'] = self.authorize_info
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
        if self.brand_registration_info:
            if hasattr(self.brand_registration_info, 'to_alipay_dict'):
                params['brand_registration_info'] = self.brand_registration_info.to_alipay_dict()
            else:
                params['brand_registration_info'] = self.brand_registration_info
        if self.id_materials:
            if isinstance(self.id_materials, list):
                for i in range(0, len(self.id_materials)):
                    element = self.id_materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.id_materials[i] = element.to_alipay_dict()
            if hasattr(self.id_materials, 'to_alipay_dict'):
                params['id_materials'] = self.id_materials.to_alipay_dict()
            else:
                params['id_materials'] = self.id_materials
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMiniappBrandSubmitModel()
        if 'apply_type' in d:
            o.apply_type = d['apply_type']
        if 'authorize_info' in d:
            o.authorize_info = d['authorize_info']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'brand_registration_info' in d:
            o.brand_registration_info = d['brand_registration_info']
        if 'id_materials' in d:
            o.id_materials = d['id_materials']
        return o


