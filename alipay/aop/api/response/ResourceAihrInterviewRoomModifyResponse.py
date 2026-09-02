#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ResourceAihrInterviewRoomModifyResponse(AlipayResponse):

    def __init__(self):
        super(ResourceAihrInterviewRoomModifyResponse, self).__init__()
        self._ai_interview_id = None

    @property
    def ai_interview_id(self):
        return self._ai_interview_id

    @ai_interview_id.setter
    def ai_interview_id(self, value):
        self._ai_interview_id = value

    def parse_response_content(self, response_content):
        response = super(ResourceAihrInterviewRoomModifyResponse, self).parse_response_content(response_content)
        if 'ai_interview_id' in response:
            self.ai_interview_id = response['ai_interview_id']
