#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSignTokenQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSignTokenQueryResponse, self).__init__()
        self._biz_code = None
        self._cert_no = None
        self._cert_type = None
        self._school_code = None
        self._school_stdcode = None
        self._user_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
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
    def school_code(self):
        return self._school_code

    @school_code.setter
    def school_code(self, value):
        self._school_code = value
    @property
    def school_stdcode(self):
        return self._school_stdcode

    @school_stdcode.setter
    def school_stdcode(self, value):
        self._school_stdcode = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSignTokenQueryResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'school_code' in response:
            self.school_code = response['school_code']
        if 'school_stdcode' in response:
            self.school_stdcode = response['school_stdcode']
        if 'user_id' in response:
            self.user_id = response['user_id']
