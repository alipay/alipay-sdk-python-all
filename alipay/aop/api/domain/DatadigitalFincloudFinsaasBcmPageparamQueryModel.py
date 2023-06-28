#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasBcmPageparamQueryModel(object):

    def __init__(self):
        self._city_name = None
        self._groovy_code = None
        self._page_stage = None
        self._prov_name = None

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def groovy_code(self):
        return self._groovy_code

    @groovy_code.setter
    def groovy_code(self, value):
        self._groovy_code = value
    @property
    def page_stage(self):
        return self._page_stage

    @page_stage.setter
    def page_stage(self, value):
        self._page_stage = value
    @property
    def prov_name(self):
        return self._prov_name

    @prov_name.setter
    def prov_name(self, value):
        self._prov_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.groovy_code:
            if hasattr(self.groovy_code, 'to_alipay_dict'):
                params['groovy_code'] = self.groovy_code.to_alipay_dict()
            else:
                params['groovy_code'] = self.groovy_code
        if self.page_stage:
            if hasattr(self.page_stage, 'to_alipay_dict'):
                params['page_stage'] = self.page_stage.to_alipay_dict()
            else:
                params['page_stage'] = self.page_stage
        if self.prov_name:
            if hasattr(self.prov_name, 'to_alipay_dict'):
                params['prov_name'] = self.prov_name.to_alipay_dict()
            else:
                params['prov_name'] = self.prov_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasBcmPageparamQueryModel()
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'groovy_code' in d:
            o.groovy_code = d['groovy_code']
        if 'page_stage' in d:
            o.page_stage = d['page_stage']
        if 'prov_name' in d:
            o.prov_name = d['prov_name']
        return o


