#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJobinterviewInterviewNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJobinterviewInterviewNotifyResponse, self).__init__()
        self._candidate_id = None
        self._manual_interview_result = None

    @property
    def candidate_id(self):
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, value):
        self._candidate_id = value
    @property
    def manual_interview_result(self):
        return self._manual_interview_result

    @manual_interview_result.setter
    def manual_interview_result(self, value):
        self._manual_interview_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJobinterviewInterviewNotifyResponse, self).parse_response_content(response_content)
        if 'candidate_id' in response:
            self.candidate_id = response['candidate_id']
        if 'manual_interview_result' in response:
            self.manual_interview_result = response['manual_interview_result']
