#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceUsersQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._query_token = None
        self._relation_type = None
        self._uid = None
        self._user_token = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def query_token(self):
        return self._query_token

    @query_token.setter
    def query_token(self, value):
        self._query_token = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def user_token(self):
        return self._user_token

    @user_token.setter
    def user_token(self, value):
        self._user_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.query_token:
            if hasattr(self.query_token, 'to_alipay_dict'):
                params['query_token'] = self.query_token.to_alipay_dict()
            else:
                params['query_token'] = self.query_token
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.user_token:
            if hasattr(self.user_token, 'to_alipay_dict'):
                params['user_token'] = self.user_token.to_alipay_dict()
            else:
                params['user_token'] = self.user_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceUsersQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query_token' in d:
            o.query_token = d['query_token']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        if 'uid' in d:
            o.uid = d['uid']
        if 'user_token' in d:
            o.user_token = d['user_token']
        return o


