#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserDetails(object):

    def __init__(self):
        self._user_change_mobile = None
        self._user_mobile = None
        self._user_name = None
        self._user_relation = None

    @property
    def user_change_mobile(self):
        return self._user_change_mobile

    @user_change_mobile.setter
    def user_change_mobile(self, value):
        self._user_change_mobile = value
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
    @property
    def user_relation(self):
        return self._user_relation

    @user_relation.setter
    def user_relation(self, value):
        self._user_relation = value


    def to_alipay_dict(self):
        params = dict()
        if self.user_change_mobile:
            if hasattr(self.user_change_mobile, 'to_alipay_dict'):
                params['user_change_mobile'] = self.user_change_mobile.to_alipay_dict()
            else:
                params['user_change_mobile'] = self.user_change_mobile
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
        if self.user_relation:
            if hasattr(self.user_relation, 'to_alipay_dict'):
                params['user_relation'] = self.user_relation.to_alipay_dict()
            else:
                params['user_relation'] = self.user_relation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserDetails()
        if 'user_change_mobile' in d:
            o.user_change_mobile = d['user_change_mobile']
        if 'user_mobile' in d:
            o.user_mobile = d['user_mobile']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_relation' in d:
            o.user_relation = d['user_relation']
        return o


