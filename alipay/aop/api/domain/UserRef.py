#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserRef(object):

    def __init__(self):
        self._hdf_user = None
        self._health_user = None

    @property
    def hdf_user(self):
        return self._hdf_user

    @hdf_user.setter
    def hdf_user(self, value):
        self._hdf_user = value
    @property
    def health_user(self):
        return self._health_user

    @health_user.setter
    def health_user(self, value):
        self._health_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.hdf_user:
            if hasattr(self.hdf_user, 'to_alipay_dict'):
                params['hdf_user'] = self.hdf_user.to_alipay_dict()
            else:
                params['hdf_user'] = self.hdf_user
        if self.health_user:
            if hasattr(self.health_user, 'to_alipay_dict'):
                params['health_user'] = self.health_user.to_alipay_dict()
            else:
                params['health_user'] = self.health_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserRef()
        if 'hdf_user' in d:
            o.hdf_user = d['hdf_user']
        if 'health_user' in d:
            o.health_user = d['health_user']
        return o


