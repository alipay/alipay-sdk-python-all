#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GameChallengePrizeVO(object):

    def __init__(self):
        self._challenge_prize_amount = None
        self._challenge_prize_id = None
        self._challenge_prize_level = None
        self._challenge_prize_name = None
        self._challenge_prize_unit = None

    @property
    def challenge_prize_amount(self):
        return self._challenge_prize_amount

    @challenge_prize_amount.setter
    def challenge_prize_amount(self, value):
        self._challenge_prize_amount = value
    @property
    def challenge_prize_id(self):
        return self._challenge_prize_id

    @challenge_prize_id.setter
    def challenge_prize_id(self, value):
        self._challenge_prize_id = value
    @property
    def challenge_prize_level(self):
        return self._challenge_prize_level

    @challenge_prize_level.setter
    def challenge_prize_level(self, value):
        self._challenge_prize_level = value
    @property
    def challenge_prize_name(self):
        return self._challenge_prize_name

    @challenge_prize_name.setter
    def challenge_prize_name(self, value):
        self._challenge_prize_name = value
    @property
    def challenge_prize_unit(self):
        return self._challenge_prize_unit

    @challenge_prize_unit.setter
    def challenge_prize_unit(self, value):
        self._challenge_prize_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.challenge_prize_amount:
            if hasattr(self.challenge_prize_amount, 'to_alipay_dict'):
                params['challenge_prize_amount'] = self.challenge_prize_amount.to_alipay_dict()
            else:
                params['challenge_prize_amount'] = self.challenge_prize_amount
        if self.challenge_prize_id:
            if hasattr(self.challenge_prize_id, 'to_alipay_dict'):
                params['challenge_prize_id'] = self.challenge_prize_id.to_alipay_dict()
            else:
                params['challenge_prize_id'] = self.challenge_prize_id
        if self.challenge_prize_level:
            if hasattr(self.challenge_prize_level, 'to_alipay_dict'):
                params['challenge_prize_level'] = self.challenge_prize_level.to_alipay_dict()
            else:
                params['challenge_prize_level'] = self.challenge_prize_level
        if self.challenge_prize_name:
            if hasattr(self.challenge_prize_name, 'to_alipay_dict'):
                params['challenge_prize_name'] = self.challenge_prize_name.to_alipay_dict()
            else:
                params['challenge_prize_name'] = self.challenge_prize_name
        if self.challenge_prize_unit:
            if hasattr(self.challenge_prize_unit, 'to_alipay_dict'):
                params['challenge_prize_unit'] = self.challenge_prize_unit.to_alipay_dict()
            else:
                params['challenge_prize_unit'] = self.challenge_prize_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GameChallengePrizeVO()
        if 'challenge_prize_amount' in d:
            o.challenge_prize_amount = d['challenge_prize_amount']
        if 'challenge_prize_id' in d:
            o.challenge_prize_id = d['challenge_prize_id']
        if 'challenge_prize_level' in d:
            o.challenge_prize_level = d['challenge_prize_level']
        if 'challenge_prize_name' in d:
            o.challenge_prize_name = d['challenge_prize_name']
        if 'challenge_prize_unit' in d:
            o.challenge_prize_unit = d['challenge_prize_unit']
        return o


