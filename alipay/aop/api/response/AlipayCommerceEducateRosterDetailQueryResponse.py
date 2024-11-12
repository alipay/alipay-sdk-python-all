#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduDepartmentNode import EduDepartmentNode


class AlipayCommerceEducateRosterDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateRosterDetailQueryResponse, self).__init__()
        self._bind_status = None
        self._cert_no = None
        self._cert_type = None
        self._department_info = None
        self._employee_no = None
        self._expire_time = None
        self._gender = None
        self._inst_id = None
        self._inst_name = None
        self._mobile = None
        self._name = None
        self._role_name = None
        self._role_type = None
        self._roster_id = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def department_info(self):
        return self._department_info

    @department_info.setter
    def department_info(self, value):
        if isinstance(value, list):
            self._department_info = list()
            for i in value:
                if isinstance(i, EduDepartmentNode):
                    self._department_info.append(i)
                else:
                    self._department_info.append(EduDepartmentNode.from_alipay_dict(i))
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
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
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
    def roster_id(self):
        return self._roster_id

    @roster_id.setter
    def roster_id(self, value):
        self._roster_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateRosterDetailQueryResponse, self).parse_response_content(response_content)
        if 'bind_status' in response:
            self.bind_status = response['bind_status']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'department_info' in response:
            self.department_info = response['department_info']
        if 'employee_no' in response:
            self.employee_no = response['employee_no']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'gender' in response:
            self.gender = response['gender']
        if 'inst_id' in response:
            self.inst_id = response['inst_id']
        if 'inst_name' in response:
            self.inst_name = response['inst_name']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'name' in response:
            self.name = response['name']
        if 'role_name' in response:
            self.role_name = response['role_name']
        if 'role_type' in response:
            self.role_type = response['role_type']
        if 'roster_id' in response:
            self.roster_id = response['roster_id']
