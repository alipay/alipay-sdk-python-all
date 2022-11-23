#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AreaDTO(object):

    def __init__(self):
        self._area_code = None
        self._area_english_name = None
        self._area_name = None
        self._area_pinyin_name = None
        self._area_type = None
        self._area_version = None
        self._ext_info = None
        self._parent_area_code = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def area_english_name(self):
        return self._area_english_name

    @area_english_name.setter
    def area_english_name(self, value):
        self._area_english_name = value
    @property
    def area_name(self):
        return self._area_name

    @area_name.setter
    def area_name(self, value):
        self._area_name = value
    @property
    def area_pinyin_name(self):
        return self._area_pinyin_name

    @area_pinyin_name.setter
    def area_pinyin_name(self, value):
        self._area_pinyin_name = value
    @property
    def area_type(self):
        return self._area_type

    @area_type.setter
    def area_type(self, value):
        self._area_type = value
    @property
    def area_version(self):
        return self._area_version

    @area_version.setter
    def area_version(self, value):
        self._area_version = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def parent_area_code(self):
        return self._parent_area_code

    @parent_area_code.setter
    def parent_area_code(self, value):
        self._parent_area_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.area_english_name:
            if hasattr(self.area_english_name, 'to_alipay_dict'):
                params['area_english_name'] = self.area_english_name.to_alipay_dict()
            else:
                params['area_english_name'] = self.area_english_name
        if self.area_name:
            if hasattr(self.area_name, 'to_alipay_dict'):
                params['area_name'] = self.area_name.to_alipay_dict()
            else:
                params['area_name'] = self.area_name
        if self.area_pinyin_name:
            if hasattr(self.area_pinyin_name, 'to_alipay_dict'):
                params['area_pinyin_name'] = self.area_pinyin_name.to_alipay_dict()
            else:
                params['area_pinyin_name'] = self.area_pinyin_name
        if self.area_type:
            if hasattr(self.area_type, 'to_alipay_dict'):
                params['area_type'] = self.area_type.to_alipay_dict()
            else:
                params['area_type'] = self.area_type
        if self.area_version:
            if hasattr(self.area_version, 'to_alipay_dict'):
                params['area_version'] = self.area_version.to_alipay_dict()
            else:
                params['area_version'] = self.area_version
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.parent_area_code:
            if hasattr(self.parent_area_code, 'to_alipay_dict'):
                params['parent_area_code'] = self.parent_area_code.to_alipay_dict()
            else:
                params['parent_area_code'] = self.parent_area_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AreaDTO()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'area_english_name' in d:
            o.area_english_name = d['area_english_name']
        if 'area_name' in d:
            o.area_name = d['area_name']
        if 'area_pinyin_name' in d:
            o.area_pinyin_name = d['area_pinyin_name']
        if 'area_type' in d:
            o.area_type = d['area_type']
        if 'area_version' in d:
            o.area_version = d['area_version']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'parent_area_code' in d:
            o.parent_area_code = d['parent_area_code']
        return o


