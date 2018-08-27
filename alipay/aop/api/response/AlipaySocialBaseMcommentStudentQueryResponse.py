#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseMcommentStudentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseMcommentStudentQueryResponse, self).__init__()
        self._campus_code = None
        self._campus_name = None
        self._degree = None
        self._enrollment_time = None
        self._graduation_time = None
        self._province_code = None
        self._province_name = None
        self._status_enum = None
        self._user_id = None

    @property
    def campus_code(self):
        return self._campus_code

    @campus_code.setter
    def campus_code(self, value):
        self._campus_code = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        self._degree = value
    @property
    def enrollment_time(self):
        return self._enrollment_time

    @enrollment_time.setter
    def enrollment_time(self, value):
        self._enrollment_time = value
    @property
    def graduation_time(self):
        return self._graduation_time

    @graduation_time.setter
    def graduation_time(self, value):
        self._graduation_time = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def status_enum(self):
        return self._status_enum

    @status_enum.setter
    def status_enum(self, value):
        self._status_enum = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseMcommentStudentQueryResponse, self).parse_response_content(response_content)
        if 'campus_code' in response:
            self.campus_code = response['campus_code']
        if 'campus_name' in response:
            self.campus_name = response['campus_name']
        if 'degree' in response:
            self.degree = response['degree']
        if 'enrollment_time' in response:
            self.enrollment_time = response['enrollment_time']
        if 'graduation_time' in response:
            self.graduation_time = response['graduation_time']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'province_name' in response:
            self.province_name = response['province_name']
        if 'status_enum' in response:
            self.status_enum = response['status_enum']
        if 'user_id' in response:
            self.user_id = response['user_id']
