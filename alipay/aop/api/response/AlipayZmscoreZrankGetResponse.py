#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayZmScoreZrankResult import AlipayZmScoreZrankResult


class AlipayZmscoreZrankGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayZmscoreZrankGetResponse, self).__init__()
        self._zm_score_zrank = None

    @property
    def zm_score_zrank(self):
        return self._zm_score_zrank

    @zm_score_zrank.setter
    def zm_score_zrank(self, value):
        if isinstance(value, AlipayZmScoreZrankResult):
            self._zm_score_zrank = value
        else:
            self._zm_score_zrank = AlipayZmScoreZrankResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayZmscoreZrankGetResponse, self).parse_response_content(response_content)
        if 'zm_score_zrank' in response:
            self.zm_score_zrank = response['zm_score_zrank']
