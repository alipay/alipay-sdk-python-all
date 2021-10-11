#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsFacepayskinReceiveModel(object):

    def __init__(self):
        self._expire_date = None
        self._skin_id = None
        self._user_id = None

    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def skin_id(self):
        return self._skin_id

    @skin_id.setter
    def skin_id(self, value):
        self._skin_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.skin_id:
            if hasattr(self.skin_id, 'to_alipay_dict'):
                params['skin_id'] = self.skin_id.to_alipay_dict()
            else:
                params['skin_id'] = self.skin_id
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
        o = AlipayCommerceSportsFacepayskinReceiveModel()
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'skin_id' in d:
            o.skin_id = d['skin_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


