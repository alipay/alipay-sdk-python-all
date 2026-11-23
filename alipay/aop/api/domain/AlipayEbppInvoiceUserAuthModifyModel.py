#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceUserAuthModifyModel(object):

    def __init__(self):
        self._auth_action = None
        self._open_id = None
        self._source_tag = None
        self._user_id = None

    @property
    def auth_action(self):
        return self._auth_action

    @auth_action.setter
    def auth_action(self, value):
        self._auth_action = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def source_tag(self):
        return self._source_tag

    @source_tag.setter
    def source_tag(self, value):
        self._source_tag = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_action:
            if hasattr(self.auth_action, 'to_alipay_dict'):
                params['auth_action'] = self.auth_action.to_alipay_dict()
            else:
                params['auth_action'] = self.auth_action
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.source_tag:
            if hasattr(self.source_tag, 'to_alipay_dict'):
                params['source_tag'] = self.source_tag.to_alipay_dict()
            else:
                params['source_tag'] = self.source_tag
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
        o = AlipayEbppInvoiceUserAuthModifyModel()
        if 'auth_action' in d:
            o.auth_action = d['auth_action']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'source_tag' in d:
            o.source_tag = d['source_tag']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


