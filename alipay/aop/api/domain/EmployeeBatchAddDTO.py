#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EmployeeBatchAddDTO(object):

    def __init__(self):
        self._department_ids = None
        self._employee_cert_no = None
        self._employee_cert_type = None
        self._employee_email = None
        self._employee_mobile = None
        self._employee_name = None
        self._employee_no = None
        self._encrypt_cert_no = None
        self._encrypt_mobile = None
        self._role_list = None

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
    def employee_cert_no(self):
        return self._employee_cert_no

    @employee_cert_no.setter
    def employee_cert_no(self, value):
        self._employee_cert_no = value
    @property
    def employee_cert_type(self):
        return self._employee_cert_type

    @employee_cert_type.setter
    def employee_cert_type(self, value):
        self._employee_cert_type = value
    @property
    def employee_email(self):
        return self._employee_email

    @employee_email.setter
    def employee_email(self, value):
        self._employee_email = value
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
    def encrypt_cert_no(self):
        return self._encrypt_cert_no

    @encrypt_cert_no.setter
    def encrypt_cert_no(self, value):
        self._encrypt_cert_no = value
    @property
    def encrypt_mobile(self):
        return self._encrypt_mobile

    @encrypt_mobile.setter
    def encrypt_mobile(self, value):
        self._encrypt_mobile = value
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
        if self.employee_cert_no:
            if hasattr(self.employee_cert_no, 'to_alipay_dict'):
                params['employee_cert_no'] = self.employee_cert_no.to_alipay_dict()
            else:
                params['employee_cert_no'] = self.employee_cert_no
        if self.employee_cert_type:
            if hasattr(self.employee_cert_type, 'to_alipay_dict'):
                params['employee_cert_type'] = self.employee_cert_type.to_alipay_dict()
            else:
                params['employee_cert_type'] = self.employee_cert_type
        if self.employee_email:
            if hasattr(self.employee_email, 'to_alipay_dict'):
                params['employee_email'] = self.employee_email.to_alipay_dict()
            else:
                params['employee_email'] = self.employee_email
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
        if self.encrypt_cert_no:
            if hasattr(self.encrypt_cert_no, 'to_alipay_dict'):
                params['encrypt_cert_no'] = self.encrypt_cert_no.to_alipay_dict()
            else:
                params['encrypt_cert_no'] = self.encrypt_cert_no
        if self.encrypt_mobile:
            if hasattr(self.encrypt_mobile, 'to_alipay_dict'):
                params['encrypt_mobile'] = self.encrypt_mobile.to_alipay_dict()
            else:
                params['encrypt_mobile'] = self.encrypt_mobile
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
        o = EmployeeBatchAddDTO()
        if 'department_ids' in d:
            o.department_ids = d['department_ids']
        if 'employee_cert_no' in d:
            o.employee_cert_no = d['employee_cert_no']
        if 'employee_cert_type' in d:
            o.employee_cert_type = d['employee_cert_type']
        if 'employee_email' in d:
            o.employee_email = d['employee_email']
        if 'employee_mobile' in d:
            o.employee_mobile = d['employee_mobile']
        if 'employee_name' in d:
            o.employee_name = d['employee_name']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'encrypt_cert_no' in d:
            o.encrypt_cert_no = d['encrypt_cert_no']
        if 'encrypt_mobile' in d:
            o.encrypt_mobile = d['encrypt_mobile']
        if 'role_list' in d:
            o.role_list = d['role_list']
        return o


