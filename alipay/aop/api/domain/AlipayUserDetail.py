#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDetail(object):

    def __init__(self):
        self._alipay_user_id = None
        self._certified = None
        self._logon_id = None
        self._real_name = None
        self._sex = None
        self._user_status = None
        self._user_type = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def certified(self):
        return self._certified

    @certified.setter
    def certified(self, value):
        self._certified = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.certified:
            if hasattr(self.certified, 'to_alipay_dict'):
                params['certified'] = self.certified.to_alipay_dict()
            else:
                params['certified'] = self.certified
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        if self.user_status:
            if hasattr(self.user_status, 'to_alipay_dict'):
                params['user_status'] = self.user_status.to_alipay_dict()
            else:
                params['user_status'] = self.user_status
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserDetail()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'certified' in d:
            o.certified = d['certified']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'sex' in d:
            o.sex = d['sex']
        if 'user_status' in d:
            o.user_status = d['user_status']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


