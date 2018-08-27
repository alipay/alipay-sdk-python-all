#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditScoreGetResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditScoreGetResponse, self).__init__()
        self._biz_no = None
        self._zm_score = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def zm_score(self):
        return self._zm_score

    @zm_score.setter
    def zm_score(self, value):
        self._zm_score = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditScoreGetResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'zm_score' in response:
            self.zm_score = response['zm_score']
