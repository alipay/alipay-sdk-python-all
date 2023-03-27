#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlcollectioncenterUserDTO(object):

    def __init__(self):
        self._affair_id = None
        self._dept_name = None
        self._dept_no = None
        self._email = None
        self._nick_name = None
        self._real_name = None
        self._user_type = None
        self._work_no = None

    @property
    def affair_id(self):
        return self._affair_id

    @affair_id.setter
    def affair_id(self, value):
        self._affair_id = value
    @property
    def dept_name(self):
        return self._dept_name

    @dept_name.setter
    def dept_name(self, value):
        self._dept_name = value
    @property
    def dept_no(self):
        return self._dept_no

    @dept_no.setter
    def dept_no(self, value):
        self._dept_no = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.affair_id:
            if hasattr(self.affair_id, 'to_alipay_dict'):
                params['affair_id'] = self.affair_id.to_alipay_dict()
            else:
                params['affair_id'] = self.affair_id
        if self.dept_name:
            if hasattr(self.dept_name, 'to_alipay_dict'):
                params['dept_name'] = self.dept_name.to_alipay_dict()
            else:
                params['dept_name'] = self.dept_name
        if self.dept_no:
            if hasattr(self.dept_no, 'to_alipay_dict'):
                params['dept_no'] = self.dept_no.to_alipay_dict()
            else:
                params['dept_no'] = self.dept_no
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlcollectioncenterUserDTO()
        if 'affair_id' in d:
            o.affair_id = d['affair_id']
        if 'dept_name' in d:
            o.dept_name = d['dept_name']
        if 'dept_no' in d:
            o.dept_no = d['dept_no']
        if 'email' in d:
            o.email = d['email']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'user_type' in d:
            o.user_type = d['user_type']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


