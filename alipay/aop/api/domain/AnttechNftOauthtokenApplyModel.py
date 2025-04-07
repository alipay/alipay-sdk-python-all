#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftOauthtokenApplyModel(object):

    def __init__(self):
        self._auth_code = None
        self._grant_type = None
        self._refresh_token = None
        self._req_msg_id = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def grant_type(self):
        return self._grant_type

    @grant_type.setter
    def grant_type(self, value):
        self._grant_type = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value
    @property
    def req_msg_id(self):
        return self._req_msg_id

    @req_msg_id.setter
    def req_msg_id(self, value):
        self._req_msg_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.grant_type:
            if hasattr(self.grant_type, 'to_alipay_dict'):
                params['grant_type'] = self.grant_type.to_alipay_dict()
            else:
                params['grant_type'] = self.grant_type
        if self.refresh_token:
            if hasattr(self.refresh_token, 'to_alipay_dict'):
                params['refresh_token'] = self.refresh_token.to_alipay_dict()
            else:
                params['refresh_token'] = self.refresh_token
        if self.req_msg_id:
            if hasattr(self.req_msg_id, 'to_alipay_dict'):
                params['req_msg_id'] = self.req_msg_id.to_alipay_dict()
            else:
                params['req_msg_id'] = self.req_msg_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftOauthtokenApplyModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'grant_type' in d:
            o.grant_type = d['grant_type']
        if 'refresh_token' in d:
            o.refresh_token = d['refresh_token']
        if 'req_msg_id' in d:
            o.req_msg_id = d['req_msg_id']
        return o


