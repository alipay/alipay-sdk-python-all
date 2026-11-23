#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtEmbenefitWelfareUserinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtEmbenefitWelfareUserinfoQueryResponse, self).__init__()
        self._birthday = None
        self._emp_login_id = None
        self._emp_sid = None
        self._gender = None
        self._has_auth = None
        self._mobile = None
        self._name = None
        self._tag_id = None
        self._tenant_code = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def emp_login_id(self):
        return self._emp_login_id

    @emp_login_id.setter
    def emp_login_id(self, value):
        self._emp_login_id = value
    @property
    def emp_sid(self):
        return self._emp_sid

    @emp_sid.setter
    def emp_sid(self, value):
        self._emp_sid = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def has_auth(self):
        return self._has_auth

    @has_auth.setter
    def has_auth(self, value):
        self._has_auth = value
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
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtEmbenefitWelfareUserinfoQueryResponse, self).parse_response_content(response_content)
        if 'birthday' in response:
            self.birthday = response['birthday']
        if 'emp_login_id' in response:
            self.emp_login_id = response['emp_login_id']
        if 'emp_sid' in response:
            self.emp_sid = response['emp_sid']
        if 'gender' in response:
            self.gender = response['gender']
        if 'has_auth' in response:
            self.has_auth = response['has_auth']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'name' in response:
            self.name = response['name']
        if 'tag_id' in response:
            self.tag_id = response['tag_id']
        if 'tenant_code' in response:
            self.tenant_code = response['tenant_code']
