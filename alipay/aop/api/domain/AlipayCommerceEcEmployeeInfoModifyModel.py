#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEmployeeInfoModifyModel(object):

    def __init__(self):
        self._accounting_entity_ids = None
        self._department_ids = None
        self._employee_email = None
        self._employee_id = None
        self._employee_mobile = None
        self._employee_name = None
        self._employee_no = None
        self._enterprise_id = None
        self._label_names = None
        self._profiles = None
        self._role_list = None

    @property
    def accounting_entity_ids(self):
        return self._accounting_entity_ids

    @accounting_entity_ids.setter
    def accounting_entity_ids(self, value):
        if isinstance(value, list):
            self._accounting_entity_ids = list()
            for i in value:
                self._accounting_entity_ids.append(i)
    @property
    def department_ids(self):
        return self._department_ids

    @department_ids.setter
    def department_ids(self, value):
        if isinstance(value, list):
            self._department_ids = list()
            for i in value:
                self._department_ids.append(i)
    @property
    def employee_email(self):
        return self._employee_email

    @employee_email.setter
    def employee_email(self, value):
        self._employee_email = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def employee_mobile(self):
        return self._employee_mobile

    @employee_mobile.setter
    def employee_mobile(self, value):
        self._employee_mobile = value
    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self, value):
        self._employee_name = value
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def label_names(self):
        return self._label_names

    @label_names.setter
    def label_names(self, value):
        if isinstance(value, list):
            self._label_names = list()
            for i in value:
                self._label_names.append(i)
    @property
    def profiles(self):
        return self._profiles

    @profiles.setter
    def profiles(self, value):
        self._profiles = value
    @property
    def role_list(self):
        return self._role_list

    @role_list.setter
    def role_list(self, value):
        if isinstance(value, list):
            self._role_list = list()
            for i in value:
                self._role_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.accounting_entity_ids:
            if isinstance(self.accounting_entity_ids, list):
                for i in range(0, len(self.accounting_entity_ids)):
                    element = self.accounting_entity_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.accounting_entity_ids[i] = element.to_alipay_dict()
            if hasattr(self.accounting_entity_ids, 'to_alipay_dict'):
                params['accounting_entity_ids'] = self.accounting_entity_ids.to_alipay_dict()
            else:
                params['accounting_entity_ids'] = self.accounting_entity_ids
        if self.department_ids:
            if isinstance(self.department_ids, list):
                for i in range(0, len(self.department_ids)):
                    element = self.department_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.department_ids[i] = element.to_alipay_dict()
            if hasattr(self.department_ids, 'to_alipay_dict'):
                params['department_ids'] = self.department_ids.to_alipay_dict()
            else:
                params['department_ids'] = self.department_ids
        if self.employee_email:
            if hasattr(self.employee_email, 'to_alipay_dict'):
                params['employee_email'] = self.employee_email.to_alipay_dict()
            else:
                params['employee_email'] = self.employee_email
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.employee_mobile:
            if hasattr(self.employee_mobile, 'to_alipay_dict'):
                params['employee_mobile'] = self.employee_mobile.to_alipay_dict()
            else:
                params['employee_mobile'] = self.employee_mobile
        if self.employee_name:
            if hasattr(self.employee_name, 'to_alipay_dict'):
                params['employee_name'] = self.employee_name.to_alipay_dict()
            else:
                params['employee_name'] = self.employee_name
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.label_names:
            if isinstance(self.label_names, list):
                for i in range(0, len(self.label_names)):
                    element = self.label_names[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_names[i] = element.to_alipay_dict()
            if hasattr(self.label_names, 'to_alipay_dict'):
                params['label_names'] = self.label_names.to_alipay_dict()
            else:
                params['label_names'] = self.label_names
        if self.profiles:
            if hasattr(self.profiles, 'to_alipay_dict'):
                params['profiles'] = self.profiles.to_alipay_dict()
            else:
                params['profiles'] = self.profiles
        if self.role_list:
            if isinstance(self.role_list, list):
                for i in range(0, len(self.role_list)):
                    element = self.role_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_list[i] = element.to_alipay_dict()
            if hasattr(self.role_list, 'to_alipay_dict'):
                params['role_list'] = self.role_list.to_alipay_dict()
            else:
                params['role_list'] = self.role_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEmployeeInfoModifyModel()
        if 'accounting_entity_ids' in d:
            o.accounting_entity_ids = d['accounting_entity_ids']
        if 'department_ids' in d:
            o.department_ids = d['department_ids']
        if 'employee_email' in d:
            o.employee_email = d['employee_email']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'employee_mobile' in d:
            o.employee_mobile = d['employee_mobile']
        if 'employee_name' in d:
            o.employee_name = d['employee_name']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'label_names' in d:
            o.label_names = d['label_names']
        if 'profiles' in d:
            o.profiles = d['profiles']
        if 'role_list' in d:
            o.role_list = d['role_list']
        return o


