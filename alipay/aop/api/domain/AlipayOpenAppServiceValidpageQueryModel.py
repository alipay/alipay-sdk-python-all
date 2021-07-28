#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppServiceValidpageQueryModel(object):

    def __init__(self):
        self._current_page = None
        self._page_size = None
        self._region_codes = None
        self._scene_code = None
        self._service_name = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def region_codes(self):
        return self._region_codes

    @region_codes.setter
    def region_codes(self, value):
        if isinstance(value, list):
            self._region_codes = list()
            for i in value:
                self._region_codes.append(i)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.region_codes:
            if isinstance(self.region_codes, list):
                for i in range(0, len(self.region_codes)):
                    element = self.region_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.region_codes[i] = element.to_alipay_dict()
            if hasattr(self.region_codes, 'to_alipay_dict'):
                params['region_codes'] = self.region_codes.to_alipay_dict()
            else:
                params['region_codes'] = self.region_codes
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppServiceValidpageQueryModel()
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'region_codes' in d:
            o.region_codes = d['region_codes']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        return o


