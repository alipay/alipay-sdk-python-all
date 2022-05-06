#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupMemberDetail(object):

    def __init__(self):
        self._group_nick_name = None
        self._invite_id = None
        self._join_scene = None
        self._join_time = None
        self._user_id = None

    @property
    def group_nick_name(self):
        return self._group_nick_name

    @group_nick_name.setter
    def group_nick_name(self, value):
        self._group_nick_name = value
    @property
    def invite_id(self):
        return self._invite_id

    @invite_id.setter
    def invite_id(self, value):
        self._invite_id = value
    @property
    def join_scene(self):
        return self._join_scene

    @join_scene.setter
    def join_scene(self, value):
        self._join_scene = value
    @property
    def join_time(self):
        return self._join_time

    @join_time.setter
    def join_time(self, value):
        self._join_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_nick_name:
            if hasattr(self.group_nick_name, 'to_alipay_dict'):
                params['group_nick_name'] = self.group_nick_name.to_alipay_dict()
            else:
                params['group_nick_name'] = self.group_nick_name
        if self.invite_id:
            if hasattr(self.invite_id, 'to_alipay_dict'):
                params['invite_id'] = self.invite_id.to_alipay_dict()
            else:
                params['invite_id'] = self.invite_id
        if self.join_scene:
            if hasattr(self.join_scene, 'to_alipay_dict'):
                params['join_scene'] = self.join_scene.to_alipay_dict()
            else:
                params['join_scene'] = self.join_scene
        if self.join_time:
            if hasattr(self.join_time, 'to_alipay_dict'):
                params['join_time'] = self.join_time.to_alipay_dict()
            else:
                params['join_time'] = self.join_time
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
        o = GroupMemberDetail()
        if 'group_nick_name' in d:
            o.group_nick_name = d['group_nick_name']
        if 'invite_id' in d:
            o.invite_id = d['invite_id']
        if 'join_scene' in d:
            o.join_scene = d['join_scene']
        if 'join_time' in d:
            o.join_time = d['join_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


