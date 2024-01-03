#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GameChallengePrizeVO import GameChallengePrizeVO


class AlipayUserGameopenpromoChallengeSettleResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGameopenpromoChallengeSettleResponse, self).__init__()
        self._settle_prize_info = None
        self._settle_status = None

    @property
    def settle_prize_info(self):
        return self._settle_prize_info

    @settle_prize_info.setter
    def settle_prize_info(self, value):
        if isinstance(value, GameChallengePrizeVO):
            self._settle_prize_info = value
        else:
            self._settle_prize_info = GameChallengePrizeVO.from_alipay_dict(value)
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserGameopenpromoChallengeSettleResponse, self).parse_response_content(response_content)
        if 'settle_prize_info' in response:
            self.settle_prize_info = response['settle_prize_info']
        if 'settle_status' in response:
            self.settle_status = response['settle_status']
