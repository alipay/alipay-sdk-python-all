#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskAntifraudscoreQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskAntifraudscoreQueryResponse, self).__init__()
        self._biz_no = None
        self._score = None
        self._unique_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskAntifraudscoreQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'score' in response:
            self.score = response['score']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
