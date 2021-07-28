#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DefiCustMemberDTO import DefiCustMemberDTO


class DefiCustUserDTO(object):

    def __init__(self):
        self._admin_name = None
        self._member_info = None
        self._role_types = None
        self._status = None
        self._user_email = None
        self._user_id = None
        self._user_mobile = None
        self._user_name = None

    @property
    def admin_name(self):
        return self._admin_name

    @admin_name.setter
    def admin_name(self, value):
        self._admin_name = value
    @property
    def member_info(self):
        return self._member_info

    @member_info.setter
    def member_info(self, value):
        if isinstance(value, DefiCustMemberDTO):
            self._member_info = value
        else:
            self._member_info = DefiCustMemberDTO.from_alipay_dict(value)
    @property
    def role_types(self):
        return self._role_types

    @role_types.setter
    def role_types(self, value):
        if isinstance(value, list):
            self._role_types = list()
            for i in value:
                self._role_types.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_email(self):
        return self._user_email

    @user_email.setter
    def user_email(self, value):
        self._user_email = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_mobile(self):
        return self._user_mobile

    @user_mobile.setter
    def user_mobile(self, value):
        self._user_mobile = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.admin_name:
            if hasattr(self.admin_name, 'to_alipay_dict'):
                params['admin_name'] = self.admin_name.to_alipay_dict()
            else:
                params['admin_name'] = self.admin_name
        if self.member_info:
            if hasattr(self.member_info, 'to_alipay_dict'):
                params['member_info'] = self.member_info.to_alipay_dict()
            else:
                params['member_info'] = self.member_info
        if self.role_types:
            if isinstance(self.role_types, list):
                for i in range(0, len(self.role_types)):
                    element = self.role_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_types[i] = element.to_alipay_dict()
            if hasattr(self.role_types, 'to_alipay_dict'):
                params['role_types'] = self.role_types.to_alipay_dict()
            else:
                params['role_types'] = self.role_types
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_email:
            if hasattr(self.user_email, 'to_alipay_dict'):
                params['user_email'] = self.user_email.to_alipay_dict()
            else:
                params['user_email'] = self.user_email
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_mobile:
            if hasattr(self.user_mobile, 'to_alipay_dict'):
                params['user_mobile'] = self.user_mobile.to_alipay_dict()
            else:
                params['user_mobile'] = self.user_mobile
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
        o = DefiCustUserDTO()
        if 'admin_name' in d:
            o.admin_name = d['admin_name']
        if 'member_info' in d:
            o.member_info = d['member_info']
        if 'role_types' in d:
            o.role_types = d['role_types']
        if 'status' in d:
            o.status = d['status']
        if 'user_email' in d:
            o.user_email = d['user_email']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_mobile' in d:
            o.user_mobile = d['user_mobile']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


