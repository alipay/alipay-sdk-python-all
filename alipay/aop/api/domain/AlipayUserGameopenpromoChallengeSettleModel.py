#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserGameopenpromoChallengeSettleModel(object):

    def __init__(self):
        self._challenge_begin_time = None
        self._challenge_biz_no = None
        self._challenge_prize_id = None
        self._open_id = None
        self._reward_prize = None
        self._user_id = None

    @property
    def challenge_begin_time(self):
        return self._challenge_begin_time

    @challenge_begin_time.setter
    def challenge_begin_time(self, value):
        self._challenge_begin_time = value
    @property
    def challenge_biz_no(self):
        return self._challenge_biz_no

    @challenge_biz_no.setter
    def challenge_biz_no(self, value):
        self._challenge_biz_no = value
    @property
    def challenge_prize_id(self):
        return self._challenge_prize_id

    @challenge_prize_id.setter
    def challenge_prize_id(self, value):
        self._challenge_prize_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def reward_prize(self):
        return self._reward_prize

    @reward_prize.setter
    def reward_prize(self, value):
        self._reward_prize = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.challenge_begin_time:
            if hasattr(self.challenge_begin_time, 'to_alipay_dict'):
                params['challenge_begin_time'] = self.challenge_begin_time.to_alipay_dict()
            else:
                params['challenge_begin_time'] = self.challenge_begin_time
        if self.challenge_biz_no:
            if hasattr(self.challenge_biz_no, 'to_alipay_dict'):
                params['challenge_biz_no'] = self.challenge_biz_no.to_alipay_dict()
            else:
                params['challenge_biz_no'] = self.challenge_biz_no
        if self.challenge_prize_id:
            if hasattr(self.challenge_prize_id, 'to_alipay_dict'):
                params['challenge_prize_id'] = self.challenge_prize_id.to_alipay_dict()
            else:
                params['challenge_prize_id'] = self.challenge_prize_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.reward_prize:
            if hasattr(self.reward_prize, 'to_alipay_dict'):
                params['reward_prize'] = self.reward_prize.to_alipay_dict()
            else:
                params['reward_prize'] = self.reward_prize
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
        o = AlipayUserGameopenpromoChallengeSettleModel()
        if 'challenge_begin_time' in d:
            o.challenge_begin_time = d['challenge_begin_time']
        if 'challenge_biz_no' in d:
            o.challenge_biz_no = d['challenge_biz_no']
        if 'challenge_prize_id' in d:
            o.challenge_prize_id = d['challenge_prize_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'reward_prize' in d:
            o.reward_prize = d['reward_prize']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


