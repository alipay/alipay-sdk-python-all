#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WelfareAuthExtResp import WelfareAuthExtResp


class AlipayDigitalmgmtWelfareSupplierauthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtWelfareSupplierauthQueryResponse, self).__init__()
        self._birthday = None
        self._emp_unique_id = None
        self._ext_info = None
        self._family_sid = None
        self._gender = None
        self._has_auth = None
        self._mobile = None
        self._name = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def emp_unique_id(self):
        return self._emp_unique_id

    @emp_unique_id.setter
    def emp_unique_id(self, value):
        self._emp_unique_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, WelfareAuthExtResp):
            self._ext_info = value
        else:
            self._ext_info = WelfareAuthExtResp.from_alipay_dict(value)
    @property
    def family_sid(self):
        return self._family_sid

    @family_sid.setter
    def family_sid(self, value):
        self._family_sid = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtWelfareSupplierauthQueryResponse, self).parse_response_content(response_content)
        if 'birthday' in response:
            self.birthday = response['birthday']
        if 'emp_unique_id' in response:
            self.emp_unique_id = response['emp_unique_id']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'family_sid' in response:
            self.family_sid = response['family_sid']
        if 'gender' in response:
            self.gender = response['gender']
        if 'has_auth' in response:
            self.has_auth = response['has_auth']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'name' in response:
            self.name = response['name']
