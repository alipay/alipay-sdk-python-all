#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotServicemodelServicelistQueryModel(object):

    def __init__(self):
        self._service_key = None
        self._user_id = None

    @property
    def service_key(self):
        return self._service_key

    @service_key.setter
    def service_key(self, value):
        self._service_key = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_key:
            if hasattr(self.service_key, 'to_alipay_dict'):
                params['service_key'] = self.service_key.to_alipay_dict()
            else:
                params['service_key'] = self.service_key
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
        o = AlipayCommerceIotServicemodelServicelistQueryModel()
        if 'service_key' in d:
            o.service_key = d['service_key']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


