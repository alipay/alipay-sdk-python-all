#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserInfoVO(object):

    def __init__(self):
        self._birthday = None
        self._head_url = None
        self._nick_name = None
        self._user_id = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def head_url(self):
        return self._head_url

    @head_url.setter
    def head_url(self, value):
        self._head_url = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
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
        if self.head_url:
            if hasattr(self.head_url, 'to_alipay_dict'):
                params['head_url'] = self.head_url.to_alipay_dict()
            else:
                params['head_url'] = self.head_url
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
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
        o = UserInfoVO()
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'head_url' in d:
            o.head_url = d['head_url']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


