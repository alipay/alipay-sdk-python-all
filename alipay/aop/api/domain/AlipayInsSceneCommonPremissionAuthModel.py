#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO


class AlipayInsSceneCommonPremissionAuthModel(object):

    def __init__(self):
        self._auth_type = None
        self._holder = None
        self._insureds = None
        self._login_user_id = None
        self._out_session_id = None
        self._partner_org_id = None

    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def holder(self):
        return self._holder

    @holder.setter
    def holder(self, value):
        if isinstance(value, InsOpenUserDTO):
            self._holder = value
        else:
            self._holder = InsOpenUserDTO.from_alipay_dict(value)
    @property
    def insureds(self):
        return self._insureds

    @insureds.setter
    def insureds(self, value):
        if isinstance(value, list):
            self._insureds = list()
            for i in value:
                if isinstance(i, InsOpenUserDTO):
                    self._insureds.append(i)
                else:
                    self._insureds.append(InsOpenUserDTO.from_alipay_dict(i))
    @property
    def login_user_id(self):
        return self._login_user_id

    @login_user_id.setter
    def login_user_id(self, value):
        self._login_user_id = value
    @property
    def out_session_id(self):
        return self._out_session_id

    @out_session_id.setter
    def out_session_id(self, value):
        self._out_session_id = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.holder:
            if hasattr(self.holder, 'to_alipay_dict'):
                params['holder'] = self.holder.to_alipay_dict()
            else:
                params['holder'] = self.holder
        if self.insureds:
            if isinstance(self.insureds, list):
                for i in range(0, len(self.insureds)):
                    element = self.insureds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.insureds[i] = element.to_alipay_dict()
            if hasattr(self.insureds, 'to_alipay_dict'):
                params['insureds'] = self.insureds.to_alipay_dict()
            else:
                params['insureds'] = self.insureds
        if self.login_user_id:
            if hasattr(self.login_user_id, 'to_alipay_dict'):
                params['login_user_id'] = self.login_user_id.to_alipay_dict()
            else:
                params['login_user_id'] = self.login_user_id
        if self.out_session_id:
            if hasattr(self.out_session_id, 'to_alipay_dict'):
                params['out_session_id'] = self.out_session_id.to_alipay_dict()
            else:
                params['out_session_id'] = self.out_session_id
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneCommonPremissionAuthModel()
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'holder' in d:
            o.holder = d['holder']
        if 'insureds' in d:
            o.insureds = d['insureds']
        if 'login_user_id' in d:
            o.login_user_id = d['login_user_id']
        if 'out_session_id' in d:
            o.out_session_id = d['out_session_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        return o


