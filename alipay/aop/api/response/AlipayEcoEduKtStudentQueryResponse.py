#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserDetails import UserDetails


class AlipayEcoEduKtStudentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEduKtStudentQueryResponse, self).__init__()
        self._child_name = None
        self._class_name = None
        self._school_name = None
        self._student_code = None
        self._student_identify = None
        self._users = None

    @property
    def child_name(self):
        return self._child_name

    @child_name.setter
    def child_name(self, value):
        self._child_name = value
    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def student_code(self):
        return self._student_code

    @student_code.setter
    def student_code(self, value):
        self._student_code = value
    @property
    def student_identify(self):
        return self._student_identify

    @student_identify.setter
    def student_identify(self, value):
        self._student_identify = value
    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        if isinstance(value, list):
            self._users = list()
            for i in value:
                if isinstance(i, UserDetails):
                    self._users.append(i)
                else:
                    self._users.append(UserDetails.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEduKtStudentQueryResponse, self).parse_response_content(response_content)
        if 'child_name' in response:
            self.child_name = response['child_name']
        if 'class_name' in response:
            self.class_name = response['class_name']
        if 'school_name' in response:
            self.school_name = response['school_name']
        if 'student_code' in response:
            self.student_code = response['student_code']
        if 'student_identify' in response:
            self.student_identify = response['student_identify']
        if 'users' in response:
            self.users = response['users']
