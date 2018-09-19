#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditUserRoleCreateModel(object):

    def __init__(self):
        self._entity_code = None
        self._entity_name = None
        self._entity_type = None
        self._ext_data = None
        self._scene_type = None

    @property
    def entity_code(self):
        return self._entity_code

    @entity_code.setter
    def entity_code(self, value):
        self._entity_code = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_code:
            if hasattr(self.entity_code, 'to_alipay_dict'):
                params['entity_code'] = self.entity_code.to_alipay_dict()
            else:
                params['entity_code'] = self.entity_code
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditUserRoleCreateModel()
        if 'entity_code' in d:
            o.entity_code = d['entity_code']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


