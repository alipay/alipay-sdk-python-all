#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenAttributeDTO import OpenAttributeDTO


class AlipayCommerceEcAuthorizationRedicturlGetModel(object):

    def __init__(self):
        self._access_token = None
        self._employee_id = None
        self._enterprise_id = None
        self._expense_type = None
        self._expense_types = None
        self._institution_id = None
        self._menu_key = None
        self._open_attribute_list = None
        self._scene_type = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def expense_type(self):
        return self._expense_type

    @expense_type.setter
    def expense_type(self, value):
        self._expense_type = value
    @property
    def expense_types(self):
        return self._expense_types

    @expense_types.setter
    def expense_types(self, value):
        if isinstance(value, list):
            self._expense_types = list()
            for i in value:
                self._expense_types.append(i)
    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def menu_key(self):
        return self._menu_key

    @menu_key.setter
    def menu_key(self, value):
        self._menu_key = value
    @property
    def open_attribute_list(self):
        return self._open_attribute_list

    @open_attribute_list.setter
    def open_attribute_list(self, value):
        if isinstance(value, list):
            self._open_attribute_list = list()
            for i in value:
                if isinstance(i, OpenAttributeDTO):
                    self._open_attribute_list.append(i)
                else:
                    self._open_attribute_list.append(OpenAttributeDTO.from_alipay_dict(i))
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.expense_type:
            if hasattr(self.expense_type, 'to_alipay_dict'):
                params['expense_type'] = self.expense_type.to_alipay_dict()
            else:
                params['expense_type'] = self.expense_type
        if self.expense_types:
            if isinstance(self.expense_types, list):
                for i in range(0, len(self.expense_types)):
                    element = self.expense_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.expense_types[i] = element.to_alipay_dict()
            if hasattr(self.expense_types, 'to_alipay_dict'):
                params['expense_types'] = self.expense_types.to_alipay_dict()
            else:
                params['expense_types'] = self.expense_types
        if self.institution_id:
            if hasattr(self.institution_id, 'to_alipay_dict'):
                params['institution_id'] = self.institution_id.to_alipay_dict()
            else:
                params['institution_id'] = self.institution_id
        if self.menu_key:
            if hasattr(self.menu_key, 'to_alipay_dict'):
                params['menu_key'] = self.menu_key.to_alipay_dict()
            else:
                params['menu_key'] = self.menu_key
        if self.open_attribute_list:
            if isinstance(self.open_attribute_list, list):
                for i in range(0, len(self.open_attribute_list)):
                    element = self.open_attribute_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_attribute_list[i] = element.to_alipay_dict()
            if hasattr(self.open_attribute_list, 'to_alipay_dict'):
                params['open_attribute_list'] = self.open_attribute_list.to_alipay_dict()
            else:
                params['open_attribute_list'] = self.open_attribute_list
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
        o = AlipayCommerceEcAuthorizationRedicturlGetModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'expense_type' in d:
            o.expense_type = d['expense_type']
        if 'expense_types' in d:
            o.expense_types = d['expense_types']
        if 'institution_id' in d:
            o.institution_id = d['institution_id']
        if 'menu_key' in d:
            o.menu_key = d['menu_key']
        if 'open_attribute_list' in d:
            o.open_attribute_list = d['open_attribute_list']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


