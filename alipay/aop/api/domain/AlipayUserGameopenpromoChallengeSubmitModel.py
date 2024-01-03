#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserGameopenpromoChallengeSubmitModel(object):

    def __init__(self):
        self._challenge_biz_no = None
        self._open_id = None
        self._user_id = None

    @property
    def challenge_biz_no(self):
        return self._challenge_biz_no

    @challenge_biz_no.setter
    def challenge_biz_no(self, value):
        self._challenge_biz_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.challenge_biz_no:
            if hasattr(self.challenge_biz_no, 'to_alipay_dict'):
                params['challenge_biz_no'] = self.challenge_biz_no.to_alipay_dict()
            else:
                params['challenge_biz_no'] = self.challenge_biz_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayUserGameopenpromoChallengeSubmitModel()
        if 'challenge_biz_no' in d:
            o.challenge_biz_no = d['challenge_biz_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


