#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberCardUserInfo(object):

    def __init__(self):
        self._birthday = None
        self._gender = None
        self._mobile = None
        self._name = None
        self._open_time = None
        self._user_id = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
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
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberCardUserInfo()
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'gender' in d:
            o.gender = d['gender']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'open_time' in d:
            o.open_time = d['open_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


