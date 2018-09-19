#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntpaasTokenCreateModel(object):

    def __init__(self):
        self._bind_mobile = None
        self._country = None
        self._login_password = None
        self._logon_id = None
        self._need_supply = None
        self._security_password = None
        self._source = None
        self._user_type = None

    @property
    def bind_mobile(self):
        return self._bind_mobile

    @bind_mobile.setter
    def bind_mobile(self, value):
        self._bind_mobile = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def login_password(self):
        return self._login_password

    @login_password.setter
    def login_password(self, value):
        self._login_password = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def need_supply(self):
        return self._need_supply

    @need_supply.setter
    def need_supply(self, value):
        self._need_supply = value
    @property
    def security_password(self):
        return self._security_password

    @security_password.setter
    def security_password(self, value):
        self._security_password = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_mobile:
            if hasattr(self.bind_mobile, 'to_alipay_dict'):
                params['bind_mobile'] = self.bind_mobile.to_alipay_dict()
            else:
                params['bind_mobile'] = self.bind_mobile
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.login_password:
            if hasattr(self.login_password, 'to_alipay_dict'):
                params['login_password'] = self.login_password.to_alipay_dict()
            else:
                params['login_password'] = self.login_password
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.need_supply:
            if hasattr(self.need_supply, 'to_alipay_dict'):
                params['need_supply'] = self.need_supply.to_alipay_dict()
            else:
                params['need_supply'] = self.need_supply
        if self.security_password:
            if hasattr(self.security_password, 'to_alipay_dict'):
                params['security_password'] = self.security_password.to_alipay_dict()
            else:
                params['security_password'] = self.security_password
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayUserAntpaasTokenCreateModel()
        if 'bind_mobile' in d:
            o.bind_mobile = d['bind_mobile']
        if 'country' in d:
            o.country = d['country']
        if 'login_password' in d:
            o.login_password = d['login_password']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'need_supply' in d:
            o.need_supply = d['need_supply']
        if 'security_password' in d:
            o.security_password = d['security_password']
        if 'source' in d:
            o.source = d['source']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


