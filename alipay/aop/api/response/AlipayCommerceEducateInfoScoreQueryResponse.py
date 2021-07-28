#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateInfoScoreQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateInfoScoreQueryResponse, self).__init__()
        self._score_evaluate = None
        self._score_type = None
        self._score_value = None

    @property
    def score_evaluate(self):
        return self._score_evaluate

    @score_evaluate.setter
    def score_evaluate(self, value):
        self._score_evaluate = value
    @property
    def score_type(self):
        return self._score_type

    @score_type.setter
    def score_type(self, value):
        self._score_type = value
    @property
    def score_value(self):
        return self._score_value

    @score_value.setter
    def score_value(self, value):
        self._score_value = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateInfoScoreQueryResponse, self).parse_response_content(response_content)
        if 'score_evaluate' in response:
            self.score_evaluate = response['score_evaluate']
        if 'score_type' in response:
            self.score_type = response['score_type']
        if 'score_value' in response:
            self.score_value = response['score_value']
