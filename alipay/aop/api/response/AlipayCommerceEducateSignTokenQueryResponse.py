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
        self._parent_logon_id = None
        self._parent_user_id = None
        self._school_code = None
        self._school_face_pass_status = None
        self._school_face_payment_status = None
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
    def parent_logon_id(self):
        return self._parent_logon_id

    @parent_logon_id.setter
    def parent_logon_id(self, value):
        self._parent_logon_id = value
    @property
    def parent_user_id(self):
        return self._parent_user_id

    @parent_user_id.setter
    def parent_user_id(self, value):
        self._parent_user_id = value
    @property
    def school_code(self):
        return self._school_code

    @school_code.setter
    def school_code(self, value):
        self._school_code = value
    @property
    def school_face_pass_status(self):
        return self._school_face_pass_status

    @school_face_pass_status.setter
    def school_face_pass_status(self, value):
        self._school_face_pass_status = value
    @property
    def school_face_payment_status(self):
        return self._school_face_payment_status

    @school_face_payment_status.setter
    def school_face_payment_status(self, value):
        self._school_face_payment_status = value
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
        if 'parent_logon_id' in response:
            self.parent_logon_id = response['parent_logon_id']
        if 'parent_user_id' in response:
            self.parent_user_id = response['parent_user_id']
        if 'school_code' in response:
            self.school_code = response['school_code']
        if 'school_face_pass_status' in response:
            self.school_face_pass_status = response['school_face_pass_status']
        if 'school_face_payment_status' in response:
            self.school_face_payment_status = response['school_face_payment_status']
        if 'school_stdcode' in response:
            self.school_stdcode = response['school_stdcode']
        if 'user_id' in response:
            self.user_id = response['user_id']
