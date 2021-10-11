#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCampusSchoolQueryModel(object):

    def __init__(self):
        self._city_code = None
        self._inst_id = None
        self._inst_id_list = None
        self._inst_name = None
        self._inst_name_like = None
        self._inst_std_code = None
        self._inst_std_code_list = None
        self._province_code = None
        self._school_property = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_id_list(self):
        return self._inst_id_list

    @inst_id_list.setter
    def inst_id_list(self, value):
        if isinstance(value, list):
            self._inst_id_list = list()
            for i in value:
                self._inst_id_list.append(i)
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def inst_name_like(self):
        return self._inst_name_like

    @inst_name_like.setter
    def inst_name_like(self, value):
        self._inst_name_like = value
    @property
    def inst_std_code(self):
        return self._inst_std_code

    @inst_std_code.setter
    def inst_std_code(self, value):
        self._inst_std_code = value
    @property
    def inst_std_code_list(self):
        return self._inst_std_code_list

    @inst_std_code_list.setter
    def inst_std_code_list(self, value):
        if isinstance(value, list):
            self._inst_std_code_list = list()
            for i in value:
                self._inst_std_code_list.append(i)
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
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_id_list:
            if isinstance(self.inst_id_list, list):
                for i in range(0, len(self.inst_id_list)):
                    element = self.inst_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inst_id_list[i] = element.to_alipay_dict()
            if hasattr(self.inst_id_list, 'to_alipay_dict'):
                params['inst_id_list'] = self.inst_id_list.to_alipay_dict()
            else:
                params['inst_id_list'] = self.inst_id_list
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.inst_name_like:
            if hasattr(self.inst_name_like, 'to_alipay_dict'):
                params['inst_name_like'] = self.inst_name_like.to_alipay_dict()
            else:
                params['inst_name_like'] = self.inst_name_like
        if self.inst_std_code:
            if hasattr(self.inst_std_code, 'to_alipay_dict'):
                params['inst_std_code'] = self.inst_std_code.to_alipay_dict()
            else:
                params['inst_std_code'] = self.inst_std_code
        if self.inst_std_code_list:
            if isinstance(self.inst_std_code_list, list):
                for i in range(0, len(self.inst_std_code_list)):
                    element = self.inst_std_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inst_std_code_list[i] = element.to_alipay_dict()
            if hasattr(self.inst_std_code_list, 'to_alipay_dict'):
                params['inst_std_code_list'] = self.inst_std_code_list.to_alipay_dict()
            else:
                params['inst_std_code_list'] = self.inst_std_code_list
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
        o = AlipayCommerceEducateCampusSchoolQueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_id_list' in d:
            o.inst_id_list = d['inst_id_list']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'inst_name_like' in d:
            o.inst_name_like = d['inst_name_like']
        if 'inst_std_code' in d:
            o.inst_std_code = d['inst_std_code']
        if 'inst_std_code_list' in d:
            o.inst_std_code_list = d['inst_std_code_list']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'school_property' in d:
            o.school_property = d['school_property']
        return o


