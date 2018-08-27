#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsDataAutoScoreQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataAutoScoreQueryResponse, self).__init__()
        self._bill_no = None
        self._exclusive_score = None
        self._ext_info = None
        self._score = None
        self._uuid = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def exclusive_score(self):
        return self._exclusive_score

    @exclusive_score.setter
    def exclusive_score(self, value):
        self._exclusive_score = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsDataAutoScoreQueryResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'exclusive_score' in response:
            self.exclusive_score = response['exclusive_score']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'score' in response:
            self.score = response['score']
        if 'uuid' in response:
            self.uuid = response['uuid']
