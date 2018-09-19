#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserDetails import UserDetails


class AlipayEcoEduKtStudentModifyModel(object):

    def __init__(self):
        self._child_name = None
        self._isv_pid = None
        self._school_no = None
        self._school_pid = None
        self._status = None
        self._student_code = None
        self._student_identify = None
        self._student_no = None
        self._users = None

    @property
    def child_name(self):
        return self._child_name

    @child_name.setter
    def child_name(self, value):
        self._child_name = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def school_no(self):
        return self._school_no

    @school_no.setter
    def school_no(self, value):
        self._school_no = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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
    def student_no(self):
        return self._student_no

    @student_no.setter
    def student_no(self, value):
        self._student_no = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.child_name:
            if hasattr(self.child_name, 'to_alipay_dict'):
                params['child_name'] = self.child_name.to_alipay_dict()
            else:
                params['child_name'] = self.child_name
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.school_no:
            if hasattr(self.school_no, 'to_alipay_dict'):
                params['school_no'] = self.school_no.to_alipay_dict()
            else:
                params['school_no'] = self.school_no
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.student_code:
            if hasattr(self.student_code, 'to_alipay_dict'):
                params['student_code'] = self.student_code.to_alipay_dict()
            else:
                params['student_code'] = self.student_code
        if self.student_identify:
            if hasattr(self.student_identify, 'to_alipay_dict'):
                params['student_identify'] = self.student_identify.to_alipay_dict()
            else:
                params['student_identify'] = self.student_identify
        if self.student_no:
            if hasattr(self.student_no, 'to_alipay_dict'):
                params['student_no'] = self.student_no.to_alipay_dict()
            else:
                params['student_no'] = self.student_no
        if self.users:
            if isinstance(self.users, list):
                for i in range(0, len(self.users)):
                    element = self.users[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.users[i] = element.to_alipay_dict()
            if hasattr(self.users, 'to_alipay_dict'):
                params['users'] = self.users.to_alipay_dict()
            else:
                params['users'] = self.users
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduKtStudentModifyModel()
        if 'child_name' in d:
            o.child_name = d['child_name']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'school_no' in d:
            o.school_no = d['school_no']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        if 'status' in d:
            o.status = d['status']
        if 'student_code' in d:
            o.student_code = d['student_code']
        if 'student_identify' in d:
            o.student_identify = d['student_identify']
        if 'student_no' in d:
            o.student_no = d['student_no']
        if 'users' in d:
            o.users = d['users']
        return o


