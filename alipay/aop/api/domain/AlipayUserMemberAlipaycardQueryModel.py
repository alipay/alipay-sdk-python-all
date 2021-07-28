#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserMemberAlipaycardQueryModel(object):

    def __init__(self):
        self._available_cache = None
        self._user_id = None

    @property
    def available_cache(self):
        return self._available_cache

    @available_cache.setter
    def available_cache(self, value):
        self._available_cache = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_cache:
            if hasattr(self.available_cache, 'to_alipay_dict'):
                params['available_cache'] = self.available_cache.to_alipay_dict()
            else:
                params['available_cache'] = self.available_cache
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
        o = AlipayUserMemberAlipaycardQueryModel()
        if 'available_cache' in d:
            o.available_cache = d['available_cache']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


