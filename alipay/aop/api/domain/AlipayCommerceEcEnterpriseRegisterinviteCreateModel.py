#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnterpriseProfilesDTO import EnterpriseProfilesDTO


class AlipayCommerceEcEnterpriseRegisterinviteCreateModel(object):

    def __init__(self):
        self._identity = None
        self._identity_open_id = None
        self._identity_type = None
        self._out_biz_no = None
        self._profiles = None
        self._register_mode = None
        self._sign_fund_way = None

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_open_id(self):
        return self._identity_open_id

    @identity_open_id.setter
    def identity_open_id(self, value):
        self._identity_open_id = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def profiles(self):
        return self._profiles

    @profiles.setter
    def profiles(self, value):
        if isinstance(value, EnterpriseProfilesDTO):
            self._profiles = value
        else:
            self._profiles = EnterpriseProfilesDTO.from_alipay_dict(value)
    @property
    def register_mode(self):
        return self._register_mode

    @register_mode.setter
    def register_mode(self, value):
        self._register_mode = value
    @property
    def sign_fund_way(self):
        return self._sign_fund_way

    @sign_fund_way.setter
    def sign_fund_way(self, value):
        self._sign_fund_way = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_open_id:
            if hasattr(self.identity_open_id, 'to_alipay_dict'):
                params['identity_open_id'] = self.identity_open_id.to_alipay_dict()
            else:
                params['identity_open_id'] = self.identity_open_id
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.profiles:
            if hasattr(self.profiles, 'to_alipay_dict'):
                params['profiles'] = self.profiles.to_alipay_dict()
            else:
                params['profiles'] = self.profiles
        if self.register_mode:
            if hasattr(self.register_mode, 'to_alipay_dict'):
                params['register_mode'] = self.register_mode.to_alipay_dict()
            else:
                params['register_mode'] = self.register_mode
        if self.sign_fund_way:
            if hasattr(self.sign_fund_way, 'to_alipay_dict'):
                params['sign_fund_way'] = self.sign_fund_way.to_alipay_dict()
            else:
                params['sign_fund_way'] = self.sign_fund_way
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEnterpriseRegisterinviteCreateModel()
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_open_id' in d:
            o.identity_open_id = d['identity_open_id']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'profiles' in d:
            o.profiles = d['profiles']
        if 'register_mode' in d:
            o.register_mode = d['register_mode']
        if 'sign_fund_way' in d:
            o.sign_fund_way = d['sign_fund_way']
        return o


