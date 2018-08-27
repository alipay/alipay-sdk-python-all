#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppMemberInfo(object):

    def __init__(self):
        self._gmt_invite = None
        self._gmt_join = None
        self._logon_id = None
        self._nick_name = None
        self._portrait = None
        self._role = None
        self._status = None
        self._user_id = None

    @property
    def gmt_invite(self):
        return self._gmt_invite

    @gmt_invite.setter
    def gmt_invite(self, value):
        self._gmt_invite = value
    @property
    def gmt_join(self):
        return self._gmt_join

    @gmt_join.setter
    def gmt_join(self, value):
        self._gmt_join = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def portrait(self):
        return self._portrait

    @portrait.setter
    def portrait(self, value):
        self._portrait = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_invite:
            if hasattr(self.gmt_invite, 'to_alipay_dict'):
                params['gmt_invite'] = self.gmt_invite.to_alipay_dict()
            else:
                params['gmt_invite'] = self.gmt_invite
        if self.gmt_join:
            if hasattr(self.gmt_join, 'to_alipay_dict'):
                params['gmt_join'] = self.gmt_join.to_alipay_dict()
            else:
                params['gmt_join'] = self.gmt_join
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.portrait:
            if hasattr(self.portrait, 'to_alipay_dict'):
                params['portrait'] = self.portrait.to_alipay_dict()
            else:
                params['portrait'] = self.portrait
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AppMemberInfo()
        if 'gmt_invite' in d:
            o.gmt_invite = d['gmt_invite']
        if 'gmt_join' in d:
            o.gmt_join = d['gmt_join']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'portrait' in d:
            o.portrait = d['portrait']
        if 'role' in d:
            o.role = d['role']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


