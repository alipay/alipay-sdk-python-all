#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupUserVO(object):

    def __init__(self):
        self._invite_id = None
        self._invite_open_id = None
        self._join_time = None
        self._login_id = None
        self._open_id = None
        self._user_id = None
        self._user_name = None

    @property
    def invite_id(self):
        return self._invite_id

    @invite_id.setter
    def invite_id(self, value):
        self._invite_id = value
    @property
    def invite_open_id(self):
        return self._invite_open_id

    @invite_open_id.setter
    def invite_open_id(self, value):
        self._invite_open_id = value
    @property
    def join_time(self):
        return self._join_time

    @join_time.setter
    def join_time(self, value):
        self._join_time = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.invite_id:
            if hasattr(self.invite_id, 'to_alipay_dict'):
                params['invite_id'] = self.invite_id.to_alipay_dict()
            else:
                params['invite_id'] = self.invite_id
        if self.invite_open_id:
            if hasattr(self.invite_open_id, 'to_alipay_dict'):
                params['invite_open_id'] = self.invite_open_id.to_alipay_dict()
            else:
                params['invite_open_id'] = self.invite_open_id
        if self.join_time:
            if hasattr(self.join_time, 'to_alipay_dict'):
                params['join_time'] = self.join_time.to_alipay_dict()
            else:
                params['join_time'] = self.join_time
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupUserVO()
        if 'invite_id' in d:
            o.invite_id = d['invite_id']
        if 'invite_open_id' in d:
            o.invite_open_id = d['invite_open_id']
        if 'join_time' in d:
            o.join_time = d['join_time']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


