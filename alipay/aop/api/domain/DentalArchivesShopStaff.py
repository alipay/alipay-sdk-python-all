#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DentalArchivesShopStaff(object):

    def __init__(self):
        self._alipay_logon_id = None
        self._open_id = None
        self._role = None
        self._staff_name = None
        self._staff_user_id = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def staff_name(self):
        return self._staff_name

    @staff_name.setter
    def staff_name(self, value):
        self._staff_name = value
    @property
    def staff_user_id(self):
        return self._staff_user_id

    @staff_user_id.setter
    def staff_user_id(self, value):
        self._staff_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.staff_name:
            if hasattr(self.staff_name, 'to_alipay_dict'):
                params['staff_name'] = self.staff_name.to_alipay_dict()
            else:
                params['staff_name'] = self.staff_name
        if self.staff_user_id:
            if hasattr(self.staff_user_id, 'to_alipay_dict'):
                params['staff_user_id'] = self.staff_user_id.to_alipay_dict()
            else:
                params['staff_user_id'] = self.staff_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DentalArchivesShopStaff()
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'role' in d:
            o.role = d['role']
        if 'staff_name' in d:
            o.staff_name = d['staff_name']
        if 'staff_user_id' in d:
            o.staff_user_id = d['staff_user_id']
        return o


