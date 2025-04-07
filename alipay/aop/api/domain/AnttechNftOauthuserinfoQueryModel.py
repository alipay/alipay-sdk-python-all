#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftOauthuserinfoQueryModel(object):

    def __init__(self):
        self._access_token = None
        self._req_msg_id = None
        self._scope = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def req_msg_id(self):
        return self._req_msg_id

    @req_msg_id.setter
    def req_msg_id(self, value):
        self._req_msg_id = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.req_msg_id:
            if hasattr(self.req_msg_id, 'to_alipay_dict'):
                params['req_msg_id'] = self.req_msg_id.to_alipay_dict()
            else:
                params['req_msg_id'] = self.req_msg_id
        if self.scope:
            if hasattr(self.scope, 'to_alipay_dict'):
                params['scope'] = self.scope.to_alipay_dict()
            else:
                params['scope'] = self.scope
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftOauthuserinfoQueryModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'req_msg_id' in d:
            o.req_msg_id = d['req_msg_id']
        if 'scope' in d:
            o.scope = d['scope']
        return o


