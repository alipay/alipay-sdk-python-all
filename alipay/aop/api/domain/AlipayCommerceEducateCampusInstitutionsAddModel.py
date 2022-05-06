#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCampusInstitutionsAddModel(object):

    def __init__(self):
        self._card_pict_url = None
        self._city_code = None
        self._inst_name = None
        self._inst_std_code = None
        self._learning_stage = None
        self._province_code = None
        self._school_property = None

    @property
    def card_pict_url(self):
        return self._card_pict_url

    @card_pict_url.setter
    def card_pict_url(self, value):
        self._card_pict_url = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def inst_std_code(self):
        return self._inst_std_code

    @inst_std_code.setter
    def inst_std_code(self, value):
        self._inst_std_code = value
    @property
    def learning_stage(self):
        return self._learning_stage

    @learning_stage.setter
    def learning_stage(self, value):
        self._learning_stage = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def school_property(self):
        return self._school_property

    @school_property.setter
    def school_property(self, value):
        self._school_property = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_pict_url:
            if hasattr(self.card_pict_url, 'to_alipay_dict'):
                params['card_pict_url'] = self.card_pict_url.to_alipay_dict()
            else:
                params['card_pict_url'] = self.card_pict_url
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.inst_std_code:
            if hasattr(self.inst_std_code, 'to_alipay_dict'):
                params['inst_std_code'] = self.inst_std_code.to_alipay_dict()
            else:
                params['inst_std_code'] = self.inst_std_code
        if self.learning_stage:
            if hasattr(self.learning_stage, 'to_alipay_dict'):
                params['learning_stage'] = self.learning_stage.to_alipay_dict()
            else:
                params['learning_stage'] = self.learning_stage
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.school_property:
            if hasattr(self.school_property, 'to_alipay_dict'):
                params['school_property'] = self.school_property.to_alipay_dict()
            else:
                params['school_property'] = self.school_property
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateCampusInstitutionsAddModel()
        if 'card_pict_url' in d:
            o.card_pict_url = d['card_pict_url']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'inst_std_code' in d:
            o.inst_std_code = d['inst_std_code']
        if 'learning_stage' in d:
            o.learning_stage = d['learning_stage']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'school_property' in d:
            o.school_property = d['school_property']
        return o


