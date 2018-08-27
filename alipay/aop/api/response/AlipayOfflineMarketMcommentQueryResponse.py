#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketMcommentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketMcommentQueryResponse, self).__init__()
        self._comment_id = None
        self._comment_status = None
        self._comment_time = None
        self._score = None

    @property
    def comment_id(self):
        return self._comment_id

    @comment_id.setter
    def comment_id(self, value):
        self._comment_id = value
    @property
    def comment_status(self):
        return self._comment_status

    @comment_status.setter
    def comment_status(self, value):
        self._comment_status = value
    @property
    def comment_time(self):
        return self._comment_time

    @comment_time.setter
    def comment_time(self, value):
        self._comment_time = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketMcommentQueryResponse, self).parse_response_content(response_content)
        if 'comment_id' in response:
            self.comment_id = response['comment_id']
        if 'comment_status' in response:
            self.comment_status = response['comment_status']
        if 'comment_time' in response:
            self.comment_time = response['comment_time']
        if 'score' in response:
            self.score = response['score']
