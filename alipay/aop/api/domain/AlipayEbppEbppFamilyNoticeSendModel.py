#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppFamilyNoticeSendModel(object):

    def __init__(self):
        self._msg_type = None
        self._msg_vars = None
        self._open_id = None
        self._sku = None
        self._user_id = None

    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def msg_vars(self):
        return self._msg_vars

    @msg_vars.setter
    def msg_vars(self, value):
        self._msg_vars = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, value):
        self._sku = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.msg_vars:
            if hasattr(self.msg_vars, 'to_alipay_dict'):
                params['msg_vars'] = self.msg_vars.to_alipay_dict()
            else:
                params['msg_vars'] = self.msg_vars
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.sku:
            if hasattr(self.sku, 'to_alipay_dict'):
                params['sku'] = self.sku.to_alipay_dict()
            else:
                params['sku'] = self.sku
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
        o = AlipayEbppEbppFamilyNoticeSendModel()
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'msg_vars' in d:
            o.msg_vars = d['msg_vars']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'sku' in d:
            o.sku = d['sku']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


