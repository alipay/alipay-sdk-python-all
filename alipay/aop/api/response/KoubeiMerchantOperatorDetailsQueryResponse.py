#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMerchantOperatorDetailsQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantOperatorDetailsQueryResponse, self).__init__()
        self._department_id = None
        self._department_name = None
        self._discount_limit_unit = None
        self._discount_limit_value = None
        self._free_limit_unit = None
        self._free_limit_value = None
        self._gender = None
        self._job_type = None
        self._login_id = None
        self._manage_shops = None
        self._mobile = None
        self._operator_id = None
        self._operator_name = None
        self._qr_code_url = None
        self._role_code = None
        self._role_id = None
        self._role_name = None
        self._status = None

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
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
    def manage_shops(self):
        return self._manage_shops

    @manage_shops.setter
    def manage_shops(self, value):
        self._manage_shops = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value
    @property
    def role_code(self):
        return self._role_code

    @role_code.setter
    def role_code(self, value):
        self._role_code = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value
    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, value):
        self._role_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantOperatorDetailsQueryResponse, self).parse_response_content(response_content)
        if 'department_id' in response:
            self.department_id = response['department_id']
        if 'department_name' in response:
            self.department_name = response['department_name']
        if 'discount_limit_unit' in response:
            self.discount_limit_unit = response['discount_limit_unit']
        if 'discount_limit_value' in response:
            self.discount_limit_value = response['discount_limit_value']
        if 'free_limit_unit' in response:
            self.free_limit_unit = response['free_limit_unit']
        if 'free_limit_value' in response:
            self.free_limit_value = response['free_limit_value']
        if 'gender' in response:
            self.gender = response['gender']
        if 'job_type' in response:
            self.job_type = response['job_type']
        if 'login_id' in response:
            self.login_id = response['login_id']
        if 'manage_shops' in response:
            self.manage_shops = response['manage_shops']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'operator_id' in response:
            self.operator_id = response['operator_id']
        if 'operator_name' in response:
            self.operator_name = response['operator_name']
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
        if 'role_code' in response:
            self.role_code = response['role_code']
        if 'role_id' in response:
            self.role_id = response['role_id']
        if 'role_name' in response:
            self.role_name = response['role_name']
        if 'status' in response:
            self.status = response['status']
