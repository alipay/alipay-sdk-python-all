#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthorizedFamilyInfo(object):

    def __init__(self):
        self._user_cert_no = None
        self._user_cert_type = None
        self._user_relation_type = None
        self._username = None

    @property
    def user_cert_no(self):
        return self._user_cert_no

    @user_cert_no.setter
    def user_cert_no(self, value):
        self._user_cert_no = value
    @property
    def user_cert_type(self):
        return self._user_cert_type

    @user_cert_type.setter
    def user_cert_type(self, value):
        self._user_cert_type = value
    @property
    def user_relation_type(self):
        return self._user_relation_type

    @user_relation_type.setter
    def user_relation_type(self, value):
        self._user_relation_type = value
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value


    def to_alipay_dict(self):
        params = dict()
        if self.user_cert_no:
            if hasattr(self.user_cert_no, 'to_alipay_dict'):
                params['user_cert_no'] = self.user_cert_no.to_alipay_dict()
            else:
                params['user_cert_no'] = self.user_cert_no
        if self.user_cert_type:
            if hasattr(self.user_cert_type, 'to_alipay_dict'):
                params['user_cert_type'] = self.user_cert_type.to_alipay_dict()
            else:
                params['user_cert_type'] = self.user_cert_type
        if self.user_relation_type:
            if hasattr(self.user_relation_type, 'to_alipay_dict'):
                params['user_relation_type'] = self.user_relation_type.to_alipay_dict()
            else:
                params['user_relation_type'] = self.user_relation_type
        if self.username:
            if hasattr(self.username, 'to_alipay_dict'):
                params['username'] = self.username.to_alipay_dict()
            else:
                params['username'] = self.username
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthorizedFamilyInfo()
        if 'user_cert_no' in d:
            o.user_cert_no = d['user_cert_no']
        if 'user_cert_type' in d:
            o.user_cert_type = d['user_cert_type']
        if 'user_relation_type' in d:
            o.user_relation_type = d['user_relation_type']
        if 'username' in d:
            o.username = d['username']
        return o


