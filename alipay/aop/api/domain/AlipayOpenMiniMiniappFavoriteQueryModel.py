#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniMiniappFavoriteQueryModel(object):

    def __init__(self):
        self._designated_app_id = None
        self._user_id = None

    @property
    def designated_app_id(self):
        return self._designated_app_id

    @designated_app_id.setter
    def designated_app_id(self, value):
        self._designated_app_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.designated_app_id:
            if hasattr(self.designated_app_id, 'to_alipay_dict'):
                params['designated_app_id'] = self.designated_app_id.to_alipay_dict()
            else:
                params['designated_app_id'] = self.designated_app_id
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
        o = AlipayOpenMiniMiniappFavoriteQueryModel()
        if 'designated_app_id' in d:
            o.designated_app_id = d['designated_app_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


