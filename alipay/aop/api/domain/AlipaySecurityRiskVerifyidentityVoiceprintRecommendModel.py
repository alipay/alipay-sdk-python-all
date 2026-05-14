#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskVerifyidentityVoiceprintRecommendModel(object):

    def __init__(self):
        self._callback_url = None
        self._recommend_type = None
        self._user_id = None

    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def recommend_type(self):
        return self._recommend_type

    @recommend_type.setter
    def recommend_type(self, value):
        self._recommend_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.recommend_type:
            if hasattr(self.recommend_type, 'to_alipay_dict'):
                params['recommend_type'] = self.recommend_type.to_alipay_dict()
            else:
                params['recommend_type'] = self.recommend_type
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
        o = AlipaySecurityRiskVerifyidentityVoiceprintRecommendModel()
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'recommend_type' in d:
            o.recommend_type = d['recommend_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


