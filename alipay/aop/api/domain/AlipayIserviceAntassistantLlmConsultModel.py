#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceAntassistantLlmConsultModel(object):

    def __init__(self):
        self._query = None
        self._session_id = None
        self._user = None

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value


    def to_alipay_dict(self):
        params = dict()
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceAntassistantLlmConsultModel()
        if 'query' in d:
            o.query = d['query']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user' in d:
            o.user = d['user']
        return o


