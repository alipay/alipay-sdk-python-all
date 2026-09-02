#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SportsWhiteItem(object):

    def __init__(self):
        self._bind_status = None
        self._credential_no = None
        self._credential_type = None
        self._department = None
        self._department_code = None
        self._employee_no = None
        self._gender = None
        self._name = None
        self._org_role_code = None
        self._org_role_name = None
        self._organization_code = None
        self._roster_code = None
        self._white_code = None
        self._white_type = None
        self._white_type_name = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
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
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
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
    def org_role_name(self):
        return self._org_role_name

    @org_role_name.setter
    def org_role_name(self, value):
        self._org_role_name = value
    @property
    def organization_code(self):
        return self._organization_code

    @organization_code.setter
    def organization_code(self, value):
        self._organization_code = value
    @property
    def roster_code(self):
        return self._roster_code

    @roster_code.setter
    def roster_code(self, value):
        self._roster_code = value
    @property
    def white_code(self):
        return self._white_code

    @white_code.setter
    def white_code(self, value):
        self._white_code = value
    @property
    def white_type(self):
        return self._white_type

    @white_type.setter
    def white_type(self, value):
        self._white_type = value
    @property
    def white_type_name(self):
        return self._white_type_name

    @white_type_name.setter
    def white_type_name(self, value):
        self._white_type_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_status:
            if hasattr(self.bind_status, 'to_alipay_dict'):
                params['bind_status'] = self.bind_status.to_alipay_dict()
            else:
                params['bind_status'] = self.bind_status
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
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
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
        if self.org_role_name:
            if hasattr(self.org_role_name, 'to_alipay_dict'):
                params['org_role_name'] = self.org_role_name.to_alipay_dict()
            else:
                params['org_role_name'] = self.org_role_name
        if self.organization_code:
            if hasattr(self.organization_code, 'to_alipay_dict'):
                params['organization_code'] = self.organization_code.to_alipay_dict()
            else:
                params['organization_code'] = self.organization_code
        if self.roster_code:
            if hasattr(self.roster_code, 'to_alipay_dict'):
                params['roster_code'] = self.roster_code.to_alipay_dict()
            else:
                params['roster_code'] = self.roster_code
        if self.white_code:
            if hasattr(self.white_code, 'to_alipay_dict'):
                params['white_code'] = self.white_code.to_alipay_dict()
            else:
                params['white_code'] = self.white_code
        if self.white_type:
            if hasattr(self.white_type, 'to_alipay_dict'):
                params['white_type'] = self.white_type.to_alipay_dict()
            else:
                params['white_type'] = self.white_type
        if self.white_type_name:
            if hasattr(self.white_type_name, 'to_alipay_dict'):
                params['white_type_name'] = self.white_type_name.to_alipay_dict()
            else:
                params['white_type_name'] = self.white_type_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SportsWhiteItem()
        if 'bind_status' in d:
            o.bind_status = d['bind_status']
        if 'credential_no' in d:
            o.credential_no = d['credential_no']
        if 'credential_type' in d:
            o.credential_type = d['credential_type']
        if 'department' in d:
            o.department = d['department']
        if 'department_code' in d:
            o.department_code = d['department_code']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'gender' in d:
            o.gender = d['gender']
        if 'name' in d:
            o.name = d['name']
        if 'org_role_code' in d:
            o.org_role_code = d['org_role_code']
        if 'org_role_name' in d:
            o.org_role_name = d['org_role_name']
        if 'organization_code' in d:
            o.organization_code = d['organization_code']
        if 'roster_code' in d:
            o.roster_code = d['roster_code']
        if 'white_code' in d:
            o.white_code = d['white_code']
        if 'white_type' in d:
            o.white_type = d['white_type']
        if 'white_type_name' in d:
            o.white_type_name = d['white_type_name']
        return o


