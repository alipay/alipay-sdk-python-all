#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CategoryRequireInfo(object):

    def __init__(self):
        self._business_licence_required = None
        self._category_code = None
        self._category_name = None
        self._category_requirements = None
        self._door_photo_required = None
        self._special_licence_required = None

    @property
    def business_licence_required(self):
        return self._business_licence_required

    @business_licence_required.setter
    def business_licence_required(self, value):
        self._business_licence_required = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def category_requirements(self):
        return self._category_requirements

    @category_requirements.setter
    def category_requirements(self, value):
        self._category_requirements = value
    @property
    def door_photo_required(self):
        return self._door_photo_required

    @door_photo_required.setter
    def door_photo_required(self, value):
        self._door_photo_required = value
    @property
    def special_licence_required(self):
        return self._special_licence_required

    @special_licence_required.setter
    def special_licence_required(self, value):
        self._special_licence_required = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_licence_required:
            if hasattr(self.business_licence_required, 'to_alipay_dict'):
                params['business_licence_required'] = self.business_licence_required.to_alipay_dict()
            else:
                params['business_licence_required'] = self.business_licence_required
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.category_requirements:
            if hasattr(self.category_requirements, 'to_alipay_dict'):
                params['category_requirements'] = self.category_requirements.to_alipay_dict()
            else:
                params['category_requirements'] = self.category_requirements
        if self.door_photo_required:
            if hasattr(self.door_photo_required, 'to_alipay_dict'):
                params['door_photo_required'] = self.door_photo_required.to_alipay_dict()
            else:
                params['door_photo_required'] = self.door_photo_required
        if self.special_licence_required:
            if hasattr(self.special_licence_required, 'to_alipay_dict'):
                params['special_licence_required'] = self.special_licence_required.to_alipay_dict()
            else:
                params['special_licence_required'] = self.special_licence_required
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryRequireInfo()
        if 'business_licence_required' in d:
            o.business_licence_required = d['business_licence_required']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'category_requirements' in d:
            o.category_requirements = d['category_requirements']
        if 'door_photo_required' in d:
            o.door_photo_required = d['door_photo_required']
        if 'special_licence_required' in d:
            o.special_licence_required = d['special_licence_required']
        return o


