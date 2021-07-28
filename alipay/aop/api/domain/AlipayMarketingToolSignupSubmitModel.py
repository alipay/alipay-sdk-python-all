#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingToolSignupSubmitModel(object):

    def __init__(self):
        self._play_id = None
        self._user_id = None

    @property
    def play_id(self):
        return self._play_id

    @play_id.setter
    def play_id(self, value):
        self._play_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.play_id:
            if hasattr(self.play_id, 'to_alipay_dict'):
                params['play_id'] = self.play_id.to_alipay_dict()
            else:
                params['play_id'] = self.play_id
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
        o = AlipayMarketingToolSignupSubmitModel()
        if 'play_id' in d:
            o.play_id = d['play_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


