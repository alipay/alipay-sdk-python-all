#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContactFollower(object):

    def __init__(self):
        self._avatar = None
        self._default_avatar = None
        self._each_record_flag = None
        self._user_id = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def default_avatar(self):
        return self._default_avatar

    @default_avatar.setter
    def default_avatar(self, value):
        self._default_avatar = value
    @property
    def each_record_flag(self):
        return self._each_record_flag

    @each_record_flag.setter
    def each_record_flag(self, value):
        self._each_record_flag = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
        if self.default_avatar:
            if hasattr(self.default_avatar, 'to_alipay_dict'):
                params['default_avatar'] = self.default_avatar.to_alipay_dict()
            else:
                params['default_avatar'] = self.default_avatar
        if self.each_record_flag:
            if hasattr(self.each_record_flag, 'to_alipay_dict'):
                params['each_record_flag'] = self.each_record_flag.to_alipay_dict()
            else:
                params['each_record_flag'] = self.each_record_flag
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
        o = ContactFollower()
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'default_avatar' in d:
            o.default_avatar = d['default_avatar']
        if 'each_record_flag' in d:
            o.each_record_flag = d['each_record_flag']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


