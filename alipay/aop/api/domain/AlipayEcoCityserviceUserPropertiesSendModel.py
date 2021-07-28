#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCityserviceUserPropertiesSendModel(object):

    def __init__(self):
        self._city_code = None
        self._cud_type = None
        self._industry_type = None
        self._prop_type = None
        self._prop_value = None
        self._user_id = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def cud_type(self):
        return self._cud_type

    @cud_type.setter
    def cud_type(self, value):
        self._cud_type = value
    @property
    def industry_type(self):
        return self._industry_type

    @industry_type.setter
    def industry_type(self, value):
        self._industry_type = value
    @property
    def prop_type(self):
        return self._prop_type

    @prop_type.setter
    def prop_type(self, value):
        self._prop_type = value
    @property
    def prop_value(self):
        return self._prop_value

    @prop_value.setter
    def prop_value(self, value):
        self._prop_value = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.cud_type:
            if hasattr(self.cud_type, 'to_alipay_dict'):
                params['cud_type'] = self.cud_type.to_alipay_dict()
            else:
                params['cud_type'] = self.cud_type
        if self.industry_type:
            if hasattr(self.industry_type, 'to_alipay_dict'):
                params['industry_type'] = self.industry_type.to_alipay_dict()
            else:
                params['industry_type'] = self.industry_type
        if self.prop_type:
            if hasattr(self.prop_type, 'to_alipay_dict'):
                params['prop_type'] = self.prop_type.to_alipay_dict()
            else:
                params['prop_type'] = self.prop_type
        if self.prop_value:
            if hasattr(self.prop_value, 'to_alipay_dict'):
                params['prop_value'] = self.prop_value.to_alipay_dict()
            else:
                params['prop_value'] = self.prop_value
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCityserviceUserPropertiesSendModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'cud_type' in d:
            o.cud_type = d['cud_type']
        if 'industry_type' in d:
            o.industry_type = d['industry_type']
        if 'prop_type' in d:
            o.prop_type = d['prop_type']
        if 'prop_value' in d:
            o.prop_value = d['prop_value']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


