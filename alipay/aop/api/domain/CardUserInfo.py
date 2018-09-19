#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardUserInfo(object):

    def __init__(self):
        self._user_uni_id = None
        self._user_uni_id_type = None

    @property
    def user_uni_id(self):
        return self._user_uni_id

    @user_uni_id.setter
    def user_uni_id(self, value):
        self._user_uni_id = value
    @property
    def user_uni_id_type(self):
        return self._user_uni_id_type

    @user_uni_id_type.setter
    def user_uni_id_type(self, value):
        self._user_uni_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.user_uni_id:
            if hasattr(self.user_uni_id, 'to_alipay_dict'):
                params['user_uni_id'] = self.user_uni_id.to_alipay_dict()
            else:
                params['user_uni_id'] = self.user_uni_id
        if self.user_uni_id_type:
            if hasattr(self.user_uni_id_type, 'to_alipay_dict'):
                params['user_uni_id_type'] = self.user_uni_id_type.to_alipay_dict()
            else:
                params['user_uni_id_type'] = self.user_uni_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardUserInfo()
        if 'user_uni_id' in d:
            o.user_uni_id = d['user_uni_id']
        if 'user_uni_id_type' in d:
            o.user_uni_id_type = d['user_uni_id_type']
        return o


