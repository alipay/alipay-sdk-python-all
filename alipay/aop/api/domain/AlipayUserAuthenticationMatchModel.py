#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAuthenticationMatchModel(object):

    def __init__(self):
        self._user_id_1 = None
        self._user_id_2 = None

    @property
    def user_id_1(self):
        return self._user_id_1

    @user_id_1.setter
    def user_id_1(self, value):
        self._user_id_1 = value
    @property
    def user_id_2(self):
        return self._user_id_2

    @user_id_2.setter
    def user_id_2(self, value):
        self._user_id_2 = value


    def to_alipay_dict(self):
        params = dict()
        if self.user_id_1:
            if hasattr(self.user_id_1, 'to_alipay_dict'):
                params['user_id_1'] = self.user_id_1.to_alipay_dict()
            else:
                params['user_id_1'] = self.user_id_1
        if self.user_id_2:
            if hasattr(self.user_id_2, 'to_alipay_dict'):
                params['user_id_2'] = self.user_id_2.to_alipay_dict()
            else:
                params['user_id_2'] = self.user_id_2
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAuthenticationMatchModel()
        if 'user_id_1' in d:
            o.user_id_1 = d['user_id_1']
        if 'user_id_2' in d:
            o.user_id_2 = d['user_id_2']
        return o


