#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TaxUserNameDto import TaxUserNameDto


class TaxUserDto(object):

    def __init__(self):
        self._payee_user_open_id = None
        self._user_id = None
        self._user_login_id = None
        self._user_name = None

    @property
    def payee_user_open_id(self):
        return self._payee_user_open_id

    @payee_user_open_id.setter
    def payee_user_open_id(self, value):
        self._payee_user_open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_login_id(self):
        return self._user_login_id

    @user_login_id.setter
    def user_login_id(self, value):
        self._user_login_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        if isinstance(value, TaxUserNameDto):
            self._user_name = value
        else:
            self._user_name = TaxUserNameDto.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.payee_user_open_id:
            if hasattr(self.payee_user_open_id, 'to_alipay_dict'):
                params['payee_user_open_id'] = self.payee_user_open_id.to_alipay_dict()
            else:
                params['payee_user_open_id'] = self.payee_user_open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_login_id:
            if hasattr(self.user_login_id, 'to_alipay_dict'):
                params['user_login_id'] = self.user_login_id.to_alipay_dict()
            else:
                params['user_login_id'] = self.user_login_id
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
        o = TaxUserDto()
        if 'payee_user_open_id' in d:
            o.payee_user_open_id = d['payee_user_open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_login_id' in d:
            o.user_login_id = d['user_login_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


