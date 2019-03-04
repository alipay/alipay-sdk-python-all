#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OnlineInviteNewerDetailInfo(object):

    def __init__(self):
        self._fst_login_time = None
        self._invite_time = None
        self._invited_phone = None
        self._partner_id = None
        self._pid = None
        self._user_cert_time = None

    @property
    def fst_login_time(self):
        return self._fst_login_time

    @fst_login_time.setter
    def fst_login_time(self, value):
        self._fst_login_time = value
    @property
    def invite_time(self):
        return self._invite_time

    @invite_time.setter
    def invite_time(self, value):
        self._invite_time = value
    @property
    def invited_phone(self):
        return self._invited_phone

    @invited_phone.setter
    def invited_phone(self, value):
        self._invited_phone = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def user_cert_time(self):
        return self._user_cert_time

    @user_cert_time.setter
    def user_cert_time(self, value):
        self._user_cert_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.fst_login_time:
            if hasattr(self.fst_login_time, 'to_alipay_dict'):
                params['fst_login_time'] = self.fst_login_time.to_alipay_dict()
            else:
                params['fst_login_time'] = self.fst_login_time
        if self.invite_time:
            if hasattr(self.invite_time, 'to_alipay_dict'):
                params['invite_time'] = self.invite_time.to_alipay_dict()
            else:
                params['invite_time'] = self.invite_time
        if self.invited_phone:
            if hasattr(self.invited_phone, 'to_alipay_dict'):
                params['invited_phone'] = self.invited_phone.to_alipay_dict()
            else:
                params['invited_phone'] = self.invited_phone
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.user_cert_time:
            if hasattr(self.user_cert_time, 'to_alipay_dict'):
                params['user_cert_time'] = self.user_cert_time.to_alipay_dict()
            else:
                params['user_cert_time'] = self.user_cert_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OnlineInviteNewerDetailInfo()
        if 'fst_login_time' in d:
            o.fst_login_time = d['fst_login_time']
        if 'invite_time' in d:
            o.invite_time = d['invite_time']
        if 'invited_phone' in d:
            o.invited_phone = d['invited_phone']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'user_cert_time' in d:
            o.user_cert_time = d['user_cert_time']
        return o


