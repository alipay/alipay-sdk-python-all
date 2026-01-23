#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsuranceMaterialInfo(object):

    def __init__(self):
        self._material_content = None
        self._material_desc = None
        self._material_type = None

    @property
    def material_content(self):
        return self._material_content

    @material_content.setter
    def material_content(self, value):
        self._material_content = value
    @property
    def material_desc(self):
        return self._material_desc

    @material_desc.setter
    def material_desc(self, value):
        self._material_desc = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_content:
            if hasattr(self.material_content, 'to_alipay_dict'):
                params['material_content'] = self.material_content.to_alipay_dict()
            else:
                params['material_content'] = self.material_content
        if self.material_desc:
            if hasattr(self.material_desc, 'to_alipay_dict'):
                params['material_desc'] = self.material_desc.to_alipay_dict()
            else:
                params['material_desc'] = self.material_desc
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsuranceMaterialInfo()
        if 'material_content' in d:
            o.material_content = d['material_content']
        if 'material_desc' in d:
            o.material_desc = d['material_desc']
        if 'material_type' in d:
            o.material_type = d['material_type']
        return o


