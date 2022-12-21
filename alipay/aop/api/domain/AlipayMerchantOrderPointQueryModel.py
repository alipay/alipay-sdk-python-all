#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserIdentity import UserIdentity


class AlipayMerchantOrderPointQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._point_type = None
        self._user = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def point_type(self):
        return self._point_type

    @point_type.setter
    def point_type(self, value):
        self._point_type = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, UserIdentity):
            self._user = value
        else:
            self._user = UserIdentity.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.point_type:
            if hasattr(self.point_type, 'to_alipay_dict'):
                params['point_type'] = self.point_type.to_alipay_dict()
            else:
                params['point_type'] = self.point_type
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
        o = AlipayMerchantOrderPointQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'point_type' in d:
            o.point_type = d['point_type']
        if 'user' in d:
            o.user = d['user']
        return o


