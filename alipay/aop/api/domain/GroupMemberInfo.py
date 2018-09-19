#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupMemberInfo(object):

    def __init__(self):
        self._group_nickname = None
        self._nickname = None
        self._user_id = None

    @property
    def group_nickname(self):
        return self._group_nickname

    @group_nickname.setter
    def group_nickname(self, value):
        self._group_nickname = value
    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        self._nickname = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_nickname:
            if hasattr(self.group_nickname, 'to_alipay_dict'):
                params['group_nickname'] = self.group_nickname.to_alipay_dict()
            else:
                params['group_nickname'] = self.group_nickname
        if self.nickname:
            if hasattr(self.nickname, 'to_alipay_dict'):
                params['nickname'] = self.nickname.to_alipay_dict()
            else:
                params['nickname'] = self.nickname
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
        o = GroupMemberInfo()
        if 'group_nickname' in d:
            o.group_nickname = d['group_nickname']
        if 'nickname' in d:
            o.nickname = d['nickname']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


