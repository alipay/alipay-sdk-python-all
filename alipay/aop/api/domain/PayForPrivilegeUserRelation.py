#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayForPrivilegeUserRelation(object):

    def __init__(self):
        self._join_time = None
        self._leave_time = None
        self._member_id = None
        self._partner_id = None
        self._status = None
        self._user_id = None

    @property
    def join_time(self):
        return self._join_time

    @join_time.setter
    def join_time(self, value):
        self._join_time = value
    @property
    def leave_time(self):
        return self._leave_time

    @leave_time.setter
    def leave_time(self, value):
        self._leave_time = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
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
        if self.join_time:
            if hasattr(self.join_time, 'to_alipay_dict'):
                params['join_time'] = self.join_time.to_alipay_dict()
            else:
                params['join_time'] = self.join_time
        if self.leave_time:
            if hasattr(self.leave_time, 'to_alipay_dict'):
                params['leave_time'] = self.leave_time.to_alipay_dict()
            else:
                params['leave_time'] = self.leave_time
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
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
        o = PayForPrivilegeUserRelation()
        if 'join_time' in d:
            o.join_time = d['join_time']
        if 'leave_time' in d:
            o.leave_time = d['leave_time']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


