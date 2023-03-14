#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsTokenInfoQueryModel(object):

    def __init__(self):
        self._info_token = None
        self._open_id = None
        self._user_id = None

    @property
    def info_token(self):
        return self._info_token

    @info_token.setter
    def info_token(self, value):
        self._info_token = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.info_token:
            if hasattr(self.info_token, 'to_alipay_dict'):
                params['info_token'] = self.info_token.to_alipay_dict()
            else:
                params['info_token'] = self.info_token
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayCommerceLogisticsTokenInfoQueryModel()
        if 'info_token' in d:
            o.info_token = d['info_token']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


