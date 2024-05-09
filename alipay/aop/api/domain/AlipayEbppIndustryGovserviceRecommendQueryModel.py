#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryGovserviceRecommendQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._recommend_token = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def recommend_token(self):
        return self._recommend_token

    @recommend_token.setter
    def recommend_token(self, value):
        self._recommend_token = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.recommend_token:
            if hasattr(self.recommend_token, 'to_alipay_dict'):
                params['recommend_token'] = self.recommend_token.to_alipay_dict()
            else:
                params['recommend_token'] = self.recommend_token
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
        o = AlipayEbppIndustryGovserviceRecommendQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'recommend_token' in d:
            o.recommend_token = d['recommend_token']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o

