#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignPlaysigninConfigQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._signin_play_id = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def signin_play_id(self):
        return self._signin_play_id

    @signin_play_id.setter
    def signin_play_id(self, value):
        self._signin_play_id = value
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
        if self.signin_play_id:
            if hasattr(self.signin_play_id, 'to_alipay_dict'):
                params['signin_play_id'] = self.signin_play_id.to_alipay_dict()
            else:
                params['signin_play_id'] = self.signin_play_id
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
        o = AlipayMarketingCampaignPlaysigninConfigQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'signin_play_id' in d:
            o.signin_play_id = d['signin_play_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


