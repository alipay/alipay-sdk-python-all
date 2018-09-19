#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicPartnerMenuQueryModel(object):

    def __init__(self):
        self._public_id = None
        self._user_id = None

    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
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
        o = AlipayOpenPublicPartnerMenuQueryModel()
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


