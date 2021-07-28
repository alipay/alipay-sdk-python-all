#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskVerifyidentityCommonQueryModel(object):

    def __init__(self):
        self._cq_type = None
        self._env_data = None
        self._user_id = None

    @property
    def cq_type(self):
        return self._cq_type

    @cq_type.setter
    def cq_type(self, value):
        self._cq_type = value
    @property
    def env_data(self):
        return self._env_data

    @env_data.setter
    def env_data(self, value):
        self._env_data = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cq_type:
            if hasattr(self.cq_type, 'to_alipay_dict'):
                params['cq_type'] = self.cq_type.to_alipay_dict()
            else:
                params['cq_type'] = self.cq_type
        if self.env_data:
            if hasattr(self.env_data, 'to_alipay_dict'):
                params['env_data'] = self.env_data.to_alipay_dict()
            else:
                params['env_data'] = self.env_data
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
        o = AlipaySecurityRiskVerifyidentityCommonQueryModel()
        if 'cq_type' in d:
            o.cq_type = d['cq_type']
        if 'env_data' in d:
            o.env_data = d['env_data']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


