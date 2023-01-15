#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthAppauthInviteCreateModel(object):

    def __init__(self):
        self._auth_app_id = None
        self._redirect_url = None
        self._state = None

    @property
    def auth_app_id(self):
        return self._auth_app_id

    @auth_app_id.setter
    def auth_app_id(self, value):
        self._auth_app_id = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_app_id:
            if hasattr(self.auth_app_id, 'to_alipay_dict'):
                params['auth_app_id'] = self.auth_app_id.to_alipay_dict()
            else:
                params['auth_app_id'] = self.auth_app_id
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthAppauthInviteCreateModel()
        if 'auth_app_id' in d:
            o.auth_app_id = d['auth_app_id']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'state' in d:
            o.state = d['state']
        return o


