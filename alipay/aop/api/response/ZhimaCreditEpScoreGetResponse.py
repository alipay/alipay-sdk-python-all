#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpScoreGetResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpScoreGetResponse, self).__init__()
        self._biz_no = None
        self._eval_date = None
        self._reason = None
        self._zm_score = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def eval_date(self):
        return self._eval_date

    @eval_date.setter
    def eval_date(self, value):
        self._eval_date = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def zm_score(self):
        return self._zm_score

    @zm_score.setter
    def zm_score(self, value):
        self._zm_score = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpScoreGetResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'eval_date' in response:
            self.eval_date = response['eval_date']
        if 'reason' in response:
            self.reason = response['reason']
        if 'zm_score' in response:
            self.zm_score = response['zm_score']
