#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubTestDesensitive(object):

    def __init__(self):
        self._email = None
        self._email_list = None
        self._is_student = None
        self._is_student_list = None
        self._school = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def email_list(self):
        return self._email_list

    @email_list.setter
    def email_list(self, value):
        if isinstance(value, list):
            self._email_list = list()
            for i in value:
                self._email_list.append(i)
    @property
    def is_student(self):
        return self._is_student

    @is_student.setter
    def is_student(self, value):
        self._is_student = value
    @property
    def is_student_list(self):
        return self._is_student_list

    @is_student_list.setter
    def is_student_list(self, value):
        if isinstance(value, list):
            self._is_student_list = list()
            for i in value:
                self._is_student_list.append(i)
    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, value):
        self._school = value


    def to_alipay_dict(self):
        params = dict()
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.email_list:
            if isinstance(self.email_list, list):
                for i in range(0, len(self.email_list)):
                    element = self.email_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.email_list[i] = element.to_alipay_dict()
            if hasattr(self.email_list, 'to_alipay_dict'):
                params['email_list'] = self.email_list.to_alipay_dict()
            else:
                params['email_list'] = self.email_list
        if self.is_student:
            if hasattr(self.is_student, 'to_alipay_dict'):
                params['is_student'] = self.is_student.to_alipay_dict()
            else:
                params['is_student'] = self.is_student
        if self.is_student_list:
            if isinstance(self.is_student_list, list):
                for i in range(0, len(self.is_student_list)):
                    element = self.is_student_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.is_student_list[i] = element.to_alipay_dict()
            if hasattr(self.is_student_list, 'to_alipay_dict'):
                params['is_student_list'] = self.is_student_list.to_alipay_dict()
            else:
                params['is_student_list'] = self.is_student_list
        if self.school:
            if hasattr(self.school, 'to_alipay_dict'):
                params['school'] = self.school.to_alipay_dict()
            else:
                params['school'] = self.school
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubTestDesensitive()
        if 'email' in d:
            o.email = d['email']
        if 'email_list' in d:
            o.email_list = d['email_list']
        if 'is_student' in d:
            o.is_student = d['is_student']
        if 'is_student_list' in d:
            o.is_student_list = d['is_student_list']
        if 'school' in d:
            o.school = d['school']
        return o


