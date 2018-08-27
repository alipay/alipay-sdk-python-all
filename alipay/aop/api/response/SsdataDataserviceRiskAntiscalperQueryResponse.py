#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskAntiscalperQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskAntiscalperQueryResponse, self).__init__()
        self._infocode = None
        self._score = None
        self._unique_id = None

    @property
    def infocode(self):
        return self._infocode

    @infocode.setter
    def infocode(self, value):
        self._infocode = value
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
        response = super(SsdataDataserviceRiskAntiscalperQueryResponse, self).parse_response_content(response_content)
        if 'infocode' in response:
            self.infocode = response['infocode']
        if 'score' in response:
            self.score = response['score']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
