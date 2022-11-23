#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSceneTokenQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSceneTokenQueryResponse, self).__init__()
        self._biz_code = None
        self._open_id = None
        self._out_user_id = None
        self._parent_logon_id = None
        self._parent_open_id = None
        self._parent_user_id = None
        self._payment_pid_list = None
        self._school_code = None
        self._school_face_pass_status = None
        self._school_face_payment_status = None
        self._school_std_code = None
        self._user_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def parent_logon_id(self):
        return self._parent_logon_id

    @parent_logon_id.setter
    def parent_logon_id(self, value):
        self._parent_logon_id = value
    @property
    def parent_open_id(self):
        return self._parent_open_id

    @parent_open_id.setter
    def parent_open_id(self, value):
        self._parent_open_id = value
    @property
    def parent_user_id(self):
        return self._parent_user_id

    @parent_user_id.setter
    def parent_user_id(self, value):
        self._parent_user_id = value
    @property
    def payment_pid_list(self):
        return self._payment_pid_list

    @payment_pid_list.setter
    def payment_pid_list(self, value):
        if isinstance(value, list):
            self._payment_pid_list = list()
            for i in value:
                self._payment_pid_list.append(i)
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
    def school_std_code(self):
        return self._school_std_code

    @school_std_code.setter
    def school_std_code(self, value):
        self._school_std_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSceneTokenQueryResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_user_id' in response:
            self.out_user_id = response['out_user_id']
        if 'parent_logon_id' in response:
            self.parent_logon_id = response['parent_logon_id']
        if 'parent_open_id' in response:
            self.parent_open_id = response['parent_open_id']
        if 'parent_user_id' in response:
            self.parent_user_id = response['parent_user_id']
        if 'payment_pid_list' in response:
            self.payment_pid_list = response['payment_pid_list']
        if 'school_code' in response:
            self.school_code = response['school_code']
        if 'school_face_pass_status' in response:
            self.school_face_pass_status = response['school_face_pass_status']
        if 'school_face_payment_status' in response:
            self.school_face_payment_status = response['school_face_payment_status']
        if 'school_std_code' in response:
            self.school_std_code = response['school_std_code']
        if 'user_id' in response:
            self.user_id = response['user_id']
