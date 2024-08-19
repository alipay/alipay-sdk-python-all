#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateRosterIdentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateRosterIdentityQueryResponse, self).__init__()
        self._department_name = None
        self._employee_no = None
        self._gender = None
        self._inst_id = None
        self._inst_name = None
        self._name = None
        self._open_id = None
        self._role_name = None
        self._role_type = None
        self._user_id = None

    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
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
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, value):
        self._role_name = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateRosterIdentityQueryResponse, self).parse_response_content(response_content)
        if 'department_name' in response:
            self.department_name = response['department_name']
        if 'employee_no' in response:
            self.employee_no = response['employee_no']
        if 'gender' in response:
            self.gender = response['gender']
        if 'inst_id' in response:
            self.inst_id = response['inst_id']
        if 'inst_name' in response:
            self.inst_name = response['inst_name']
        if 'name' in response:
            self.name = response['name']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'role_name' in response:
            self.role_name = response['role_name']
        if 'role_type' in response:
            self.role_type = response['role_type']
        if 'user_id' in response:
            self.user_id = response['user_id']
