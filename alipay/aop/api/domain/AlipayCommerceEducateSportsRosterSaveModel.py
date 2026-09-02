#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSportsRosterSaveModel(object):

    def __init__(self):
        self._credential_no = None
        self._credential_type = None
        self._department_code = None
        self._employee_no = None
        self._gender = None
        self._invalid_date = None
        self._name = None
        self._org_role_code = None
        self._organization_code = None
        self._phone = None

    @property
    def credential_no(self):
        return self._credential_no

    @credential_no.setter
    def credential_no(self, value):
        self._credential_no = value
    @property
    def credential_type(self):
        return self._credential_type

    @credential_type.setter
    def credential_type(self, value):
        self._credential_type = value
    @property
    def department_code(self):
        return self._department_code

    @department_code.setter
    def department_code(self, value):
        self._department_code = value
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def invalid_date(self):
        return self._invalid_date

    @invalid_date.setter
    def invalid_date(self, value):
        self._invalid_date = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def org_role_code(self):
        return self._org_role_code

    @org_role_code.setter
    def org_role_code(self, value):
        self._org_role_code = value
    @property
    def organization_code(self):
        return self._organization_code

    @organization_code.setter
    def organization_code(self, value):
        self._organization_code = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.credential_no:
            if hasattr(self.credential_no, 'to_alipay_dict'):
                params['credential_no'] = self.credential_no.to_alipay_dict()
            else:
                params['credential_no'] = self.credential_no
        if self.credential_type:
            if hasattr(self.credential_type, 'to_alipay_dict'):
                params['credential_type'] = self.credential_type.to_alipay_dict()
            else:
                params['credential_type'] = self.credential_type
        if self.department_code:
            if hasattr(self.department_code, 'to_alipay_dict'):
                params['department_code'] = self.department_code.to_alipay_dict()
            else:
                params['department_code'] = self.department_code
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.invalid_date:
            if hasattr(self.invalid_date, 'to_alipay_dict'):
                params['invalid_date'] = self.invalid_date.to_alipay_dict()
            else:
                params['invalid_date'] = self.invalid_date
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.org_role_code:
            if hasattr(self.org_role_code, 'to_alipay_dict'):
                params['org_role_code'] = self.org_role_code.to_alipay_dict()
            else:
                params['org_role_code'] = self.org_role_code
        if self.organization_code:
            if hasattr(self.organization_code, 'to_alipay_dict'):
                params['organization_code'] = self.organization_code.to_alipay_dict()
            else:
                params['organization_code'] = self.organization_code
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSportsRosterSaveModel()
        if 'credential_no' in d:
            o.credential_no = d['credential_no']
        if 'credential_type' in d:
            o.credential_type = d['credential_type']
        if 'department_code' in d:
            o.department_code = d['department_code']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'gender' in d:
            o.gender = d['gender']
        if 'invalid_date' in d:
            o.invalid_date = d['invalid_date']
        if 'name' in d:
            o.name = d['name']
        if 'org_role_code' in d:
            o.org_role_code = d['org_role_code']
        if 'organization_code' in d:
            o.organization_code = d['organization_code']
        if 'phone' in d:
            o.phone = d['phone']
        return o


