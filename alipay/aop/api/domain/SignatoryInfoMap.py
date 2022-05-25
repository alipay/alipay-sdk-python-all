#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignatoryInfoMap(object):

    def __init__(self):
        self._app_desens_display_name = None
        self._avatar = None
        self._binded_mobile = None
        self._cert_no = None
        self._customer_id = None
        self._email = None
        self._is_certified = None
        self._logon_id = None
        self._nick_name = None
        self._user_id = None
        self._user_name = None
        self._user_type = None

    @property
    def app_desens_display_name(self):
        return self._app_desens_display_name

    @app_desens_display_name.setter
    def app_desens_display_name(self, value):
        self._app_desens_display_name = value
    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def binded_mobile(self):
        return self._binded_mobile

    @binded_mobile.setter
    def binded_mobile(self, value):
        self._binded_mobile = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def is_certified(self):
        return self._is_certified

    @is_certified.setter
    def is_certified(self, value):
        self._is_certified = value
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
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_desens_display_name:
            if hasattr(self.app_desens_display_name, 'to_alipay_dict'):
                params['app_desens_display_name'] = self.app_desens_display_name.to_alipay_dict()
            else:
                params['app_desens_display_name'] = self.app_desens_display_name
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
        if self.binded_mobile:
            if hasattr(self.binded_mobile, 'to_alipay_dict'):
                params['binded_mobile'] = self.binded_mobile.to_alipay_dict()
            else:
                params['binded_mobile'] = self.binded_mobile
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.is_certified:
            if hasattr(self.is_certified, 'to_alipay_dict'):
                params['is_certified'] = self.is_certified.to_alipay_dict()
            else:
                params['is_certified'] = self.is_certified
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
        o = SignatoryInfoMap()
        if 'app_desens_display_name' in d:
            o.app_desens_display_name = d['app_desens_display_name']
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'binded_mobile' in d:
            o.binded_mobile = d['binded_mobile']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'email' in d:
            o.email = d['email']
        if 'is_certified' in d:
            o.is_certified = d['is_certified']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


