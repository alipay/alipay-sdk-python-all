#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTourUserinfoQueryModel(object):

    def __init__(self):
        self._code_token = None
        self._identity_type_list = None
        self._open_id = None
        self._scenic_id = None
        self._user_id = None

    @property
    def code_token(self):
        return self._code_token

    @code_token.setter
    def code_token(self, value):
        self._code_token = value
    @property
    def identity_type_list(self):
        return self._identity_type_list

    @identity_type_list.setter
    def identity_type_list(self, value):
        if isinstance(value, list):
            self._identity_type_list = list()
            for i in value:
                self._identity_type_list.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_token:
            if hasattr(self.code_token, 'to_alipay_dict'):
                params['code_token'] = self.code_token.to_alipay_dict()
            else:
                params['code_token'] = self.code_token
        if self.identity_type_list:
            if isinstance(self.identity_type_list, list):
                for i in range(0, len(self.identity_type_list)):
                    element = self.identity_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.identity_type_list[i] = element.to_alipay_dict()
            if hasattr(self.identity_type_list, 'to_alipay_dict'):
                params['identity_type_list'] = self.identity_type_list.to_alipay_dict()
            else:
                params['identity_type_list'] = self.identity_type_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.scenic_id:
            if hasattr(self.scenic_id, 'to_alipay_dict'):
                params['scenic_id'] = self.scenic_id.to_alipay_dict()
            else:
                params['scenic_id'] = self.scenic_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTourUserinfoQueryModel()
        if 'code_token' in d:
            o.code_token = d['code_token']
        if 'identity_type_list' in d:
            o.identity_type_list = d['identity_type_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'scenic_id' in d:
            o.scenic_id = d['scenic_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


