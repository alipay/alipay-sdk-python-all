#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GameChallengePrizeVO import GameChallengePrizeVO


class AlipayUserGameopenpromoChallengeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGameopenpromoChallengeQueryResponse, self).__init__()
        self._challenge_prize_list = None
        self._end_date = None
        self._fuka_cost = None
        self._fuka_enough = None
        self._join_authority = None
        self._join_max_limit = None
        self._join_times = None
        self._start_date = None

    @property
    def challenge_prize_list(self):
        return self._challenge_prize_list

    @challenge_prize_list.setter
    def challenge_prize_list(self, value):
        if isinstance(value, list):
            self._challenge_prize_list = list()
            for i in value:
                if isinstance(i, GameChallengePrizeVO):
                    self._challenge_prize_list.append(i)
                else:
                    self._challenge_prize_list.append(GameChallengePrizeVO.from_alipay_dict(i))
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def fuka_cost(self):
        return self._fuka_cost

    @fuka_cost.setter
    def fuka_cost(self, value):
        self._fuka_cost = value
    @property
    def fuka_enough(self):
        return self._fuka_enough

    @fuka_enough.setter
    def fuka_enough(self, value):
        self._fuka_enough = value
    @property
    def join_authority(self):
        return self._join_authority

    @join_authority.setter
    def join_authority(self, value):
        self._join_authority = value
    @property
    def join_max_limit(self):
        return self._join_max_limit

    @join_max_limit.setter
    def join_max_limit(self, value):
        self._join_max_limit = value
    @property
    def join_times(self):
        return self._join_times

    @join_times.setter
    def join_times(self, value):
        self._join_times = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserGameopenpromoChallengeQueryResponse, self).parse_response_content(response_content)
        if 'challenge_prize_list' in response:
            self.challenge_prize_list = response['challenge_prize_list']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'fuka_cost' in response:
            self.fuka_cost = response['fuka_cost']
        if 'fuka_enough' in response:
            self.fuka_enough = response['fuka_enough']
        if 'join_authority' in response:
            self.join_authority = response['join_authority']
        if 'join_max_limit' in response:
            self.join_max_limit = response['join_max_limit']
        if 'join_times' in response:
            self.join_times = response['join_times']
        if 'start_date' in response:
            self.start_date = response['start_date']
