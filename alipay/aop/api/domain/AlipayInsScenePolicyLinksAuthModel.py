#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsScenePolicyLinksAuthModel(object):

    def __init__(self):
        self._login_user_id = None
        self._out_order_id = None
        self._out_session_expiration = None
        self._out_session_id = None
        self._partner_org_id = None
        self._policy_nos = None
        self._user_client = None

    @property
    def login_user_id(self):
        return self._login_user_id

    @login_user_id.setter
    def login_user_id(self, value):
        self._login_user_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_session_expiration(self):
        return self._out_session_expiration

    @out_session_expiration.setter
    def out_session_expiration(self, value):
        self._out_session_expiration = value
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
    @property
    def policy_nos(self):
        return self._policy_nos

    @policy_nos.setter
    def policy_nos(self, value):
        if isinstance(value, list):
            self._policy_nos = list()
            for i in value:
                self._policy_nos.append(i)
    @property
    def user_client(self):
        return self._user_client

    @user_client.setter
    def user_client(self, value):
        self._user_client = value


    def to_alipay_dict(self):
        params = dict()
        if self.login_user_id:
            if hasattr(self.login_user_id, 'to_alipay_dict'):
                params['login_user_id'] = self.login_user_id.to_alipay_dict()
            else:
                params['login_user_id'] = self.login_user_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_session_expiration:
            if hasattr(self.out_session_expiration, 'to_alipay_dict'):
                params['out_session_expiration'] = self.out_session_expiration.to_alipay_dict()
            else:
                params['out_session_expiration'] = self.out_session_expiration
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
        if self.policy_nos:
            if isinstance(self.policy_nos, list):
                for i in range(0, len(self.policy_nos)):
                    element = self.policy_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.policy_nos[i] = element.to_alipay_dict()
            if hasattr(self.policy_nos, 'to_alipay_dict'):
                params['policy_nos'] = self.policy_nos.to_alipay_dict()
            else:
                params['policy_nos'] = self.policy_nos
        if self.user_client:
            if hasattr(self.user_client, 'to_alipay_dict'):
                params['user_client'] = self.user_client.to_alipay_dict()
            else:
                params['user_client'] = self.user_client
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsScenePolicyLinksAuthModel()
        if 'login_user_id' in d:
            o.login_user_id = d['login_user_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_session_expiration' in d:
            o.out_session_expiration = d['out_session_expiration']
        if 'out_session_id' in d:
            o.out_session_id = d['out_session_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'policy_nos' in d:
            o.policy_nos = d['policy_nos']
        if 'user_client' in d:
            o.user_client = d['user_client']
        return o


