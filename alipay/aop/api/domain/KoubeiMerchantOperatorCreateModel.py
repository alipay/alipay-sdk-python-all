#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantOperatorCreateModel(object):

    def __init__(self):
        self._auth_code = None
        self._department_id = None
        self._discount_limit_unit = None
        self._discount_limit_value = None
        self._free_limit_unit = None
        self._free_limit_value = None
        self._gender = None
        self._job_type = None
        self._login_id = None
        self._mobile = None
        self._operator_name = None
        self._role_id = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def discount_limit_unit(self):
        return self._discount_limit_unit

    @discount_limit_unit.setter
    def discount_limit_unit(self, value):
        self._discount_limit_unit = value
    @property
    def discount_limit_value(self):
        return self._discount_limit_value

    @discount_limit_value.setter
    def discount_limit_value(self, value):
        self._discount_limit_value = value
    @property
    def free_limit_unit(self):
        return self._free_limit_unit

    @free_limit_unit.setter
    def free_limit_unit(self, value):
        self._free_limit_unit = value
    @property
    def free_limit_value(self):
        return self._free_limit_value

    @free_limit_value.setter
    def free_limit_value(self, value):
        self._free_limit_value = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, value):
        self._job_type = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.discount_limit_unit:
            if hasattr(self.discount_limit_unit, 'to_alipay_dict'):
                params['discount_limit_unit'] = self.discount_limit_unit.to_alipay_dict()
            else:
                params['discount_limit_unit'] = self.discount_limit_unit
        if self.discount_limit_value:
            if hasattr(self.discount_limit_value, 'to_alipay_dict'):
                params['discount_limit_value'] = self.discount_limit_value.to_alipay_dict()
            else:
                params['discount_limit_value'] = self.discount_limit_value
        if self.free_limit_unit:
            if hasattr(self.free_limit_unit, 'to_alipay_dict'):
                params['free_limit_unit'] = self.free_limit_unit.to_alipay_dict()
            else:
                params['free_limit_unit'] = self.free_limit_unit
        if self.free_limit_value:
            if hasattr(self.free_limit_value, 'to_alipay_dict'):
                params['free_limit_value'] = self.free_limit_value.to_alipay_dict()
            else:
                params['free_limit_value'] = self.free_limit_value
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.job_type:
            if hasattr(self.job_type, 'to_alipay_dict'):
                params['job_type'] = self.job_type.to_alipay_dict()
            else:
                params['job_type'] = self.job_type
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.role_id:
            if hasattr(self.role_id, 'to_alipay_dict'):
                params['role_id'] = self.role_id.to_alipay_dict()
            else:
                params['role_id'] = self.role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantOperatorCreateModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'discount_limit_unit' in d:
            o.discount_limit_unit = d['discount_limit_unit']
        if 'discount_limit_value' in d:
            o.discount_limit_value = d['discount_limit_value']
        if 'free_limit_unit' in d:
            o.free_limit_unit = d['free_limit_unit']
        if 'free_limit_value' in d:
            o.free_limit_value = d['free_limit_value']
        if 'gender' in d:
            o.gender = d['gender']
        if 'job_type' in d:
            o.job_type = d['job_type']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'role_id' in d:
            o.role_id = d['role_id']
        return o


