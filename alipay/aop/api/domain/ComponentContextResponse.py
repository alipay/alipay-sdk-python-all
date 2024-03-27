#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ComponentContextResponse(object):

    def __init__(self):
        self._component_code = None
        self._property_model_map = None

    @property
    def component_code(self):
        return self._component_code

    @component_code.setter
    def component_code(self, value):
        self._component_code = value
    @property
    def property_model_map(self):
        return self._property_model_map

    @property_model_map.setter
    def property_model_map(self, value):
        self._property_model_map = value


    def to_alipay_dict(self):
        params = dict()
        if self.component_code:
            if hasattr(self.component_code, 'to_alipay_dict'):
                params['component_code'] = self.component_code.to_alipay_dict()
            else:
                params['component_code'] = self.component_code
        if self.property_model_map:
            if hasattr(self.property_model_map, 'to_alipay_dict'):
                params['property_model_map'] = self.property_model_map.to_alipay_dict()
            else:
                params['property_model_map'] = self.property_model_map
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ComponentContextResponse()
        if 'component_code' in d:
            o.component_code = d['component_code']
        if 'property_model_map' in d:
            o.property_model_map = d['property_model_map']
        return o


