#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdMateriallibraryDeleteModel(object):

    def __init__(self):
        self._material_type = None
        self._principal_tag = None
        self._user_material_id_list = None

    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def user_material_id_list(self):
        return self._user_material_id_list

    @user_material_id_list.setter
    def user_material_id_list(self, value):
        if isinstance(value, list):
            self._user_material_id_list = list()
            for i in value:
                self._user_material_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.user_material_id_list:
            if isinstance(self.user_material_id_list, list):
                for i in range(0, len(self.user_material_id_list)):
                    element = self.user_material_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_material_id_list[i] = element.to_alipay_dict()
            if hasattr(self.user_material_id_list, 'to_alipay_dict'):
                params['user_material_id_list'] = self.user_material_id_list.to_alipay_dict()
            else:
                params['user_material_id_list'] = self.user_material_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdMateriallibraryDeleteModel()
        if 'material_type' in d:
            o.material_type = d['material_type']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'user_material_id_list' in d:
            o.user_material_id_list = d['user_material_id_list']
        return o


