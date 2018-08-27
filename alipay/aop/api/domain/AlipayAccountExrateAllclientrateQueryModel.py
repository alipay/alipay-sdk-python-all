#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountExrateAllclientrateQueryModel(object):

    def __init__(self):
        self._client_id = None
        self._profile_id = None

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def profile_id(self):
        return self._profile_id

    @profile_id.setter
    def profile_id(self, value):
        self._profile_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.profile_id:
            if hasattr(self.profile_id, 'to_alipay_dict'):
                params['profile_id'] = self.profile_id.to_alipay_dict()
            else:
                params['profile_id'] = self.profile_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountExrateAllclientrateQueryModel()
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'profile_id' in d:
            o.profile_id = d['profile_id']
        return o


