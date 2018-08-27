#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaDataFeedbackurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaDataFeedbackurlQueryResponse, self).__init__()
        self._feedback_url = None

    @property
    def feedback_url(self):
        return self._feedback_url

    @feedback_url.setter
    def feedback_url(self, value):
        self._feedback_url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaDataFeedbackurlQueryResponse, self).parse_response_content(response_content)
        if 'feedback_url' in response:
            self.feedback_url = response['feedback_url']
