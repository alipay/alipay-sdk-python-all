#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditAntifraudScoreGetResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditAntifraudScoreGetResponse, self).__init__()
        self._biz_no = None
        self._decision_result = None
        self._score = None
        self._solution_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def decision_result(self):
        return self._decision_result

    @decision_result.setter
    def decision_result(self, value):
        self._decision_result = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditAntifraudScoreGetResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'decision_result' in response:
            self.decision_result = response['decision_result']
        if 'score' in response:
            self.score = response['score']
        if 'solution_id' in response:
            self.solution_id = response['solution_id']
