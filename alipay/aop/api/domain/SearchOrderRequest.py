#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchOrderRequest(object):

    def __init__(self):
        self._apply_id = None
        self._apply_type = None
        self._brand_template_id = None
        self._service_code = None
        self._spec_code = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_type(self):
        return self._apply_type

    @apply_type.setter
    def apply_type(self, value):
        self._apply_type = value
    @property
    def brand_template_id(self):
        return self._brand_template_id

    @brand_template_id.setter
    def brand_template_id(self, value):
        self._brand_template_id = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_type:
            if hasattr(self.apply_type, 'to_alipay_dict'):
                params['apply_type'] = self.apply_type.to_alipay_dict()
            else:
                params['apply_type'] = self.apply_type
        if self.brand_template_id:
            if hasattr(self.brand_template_id, 'to_alipay_dict'):
                params['brand_template_id'] = self.brand_template_id.to_alipay_dict()
            else:
                params['brand_template_id'] = self.brand_template_id
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchOrderRequest()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_type' in d:
            o.apply_type = d['apply_type']
        if 'brand_template_id' in d:
            o.brand_template_id = d['brand_template_id']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        return o


