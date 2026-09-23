#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CorroborationMaterials(object):

    def __init__(self):
        self._material_file_list = None
        self._material_type = None

    @property
    def material_file_list(self):
        return self._material_file_list

    @material_file_list.setter
    def material_file_list(self, value):
        if isinstance(value, list):
            self._material_file_list = list()
            for i in value:
                self._material_file_list.append(i)
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_file_list:
            if isinstance(self.material_file_list, list):
                for i in range(0, len(self.material_file_list)):
                    element = self.material_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_file_list[i] = element.to_alipay_dict()
            if hasattr(self.material_file_list, 'to_alipay_dict'):
                params['material_file_list'] = self.material_file_list.to_alipay_dict()
            else:
                params['material_file_list'] = self.material_file_list
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
        o = CorroborationMaterials()
        if 'material_file_list' in d:
            o.material_file_list = d['material_file_list']
        if 'material_type' in d:
            o.material_type = d['material_type']
        return o


