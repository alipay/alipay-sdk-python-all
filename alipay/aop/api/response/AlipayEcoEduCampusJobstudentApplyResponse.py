#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEduCampusJobstudentApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEduCampusJobstudentApplyResponse, self).__init__()
        self._content = None
        self._content_var = None
        self._degree = None
        self._description = None
        self._enrollment_time = None
        self._is_graduate = None
        self._is_student = None
        self._isv_code = None
        self._school = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_var(self):
        return self._content_var

    @content_var.setter
    def content_var(self, value):
        self._content_var = value
    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        self._degree = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def enrollment_time(self):
        return self._enrollment_time

    @enrollment_time.setter
    def enrollment_time(self, value):
        self._enrollment_time = value
    @property
    def is_graduate(self):
        return self._is_graduate

    @is_graduate.setter
    def is_graduate(self, value):
        self._is_graduate = value
    @property
    def is_student(self):
        return self._is_student

    @is_student.setter
    def is_student(self, value):
        self._is_student = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, value):
        self._school = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEduCampusJobstudentApplyResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'content_var' in response:
            self.content_var = response['content_var']
        if 'degree' in response:
            self.degree = response['degree']
        if 'description' in response:
            self.description = response['description']
        if 'enrollment_time' in response:
            self.enrollment_time = response['enrollment_time']
        if 'is_graduate' in response:
            self.is_graduate = response['is_graduate']
        if 'is_student' in response:
            self.is_student = response['is_student']
        if 'isv_code' in response:
            self.isv_code = response['isv_code']
        if 'school' in response:
            self.school = response['school']
