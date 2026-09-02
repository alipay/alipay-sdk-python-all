#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ResourceAihrInterviewRoomCreateResponse(AlipayResponse):

    def __init__(self):
        super(ResourceAihrInterviewRoomCreateResponse, self).__init__()
        self._ai_interview_id = None
        self._ai_interview_url = None
        self._end_time = None

    @property
    def ai_interview_id(self):
        return self._ai_interview_id

    @ai_interview_id.setter
    def ai_interview_id(self, value):
        self._ai_interview_id = value
    @property
    def ai_interview_url(self):
        return self._ai_interview_url

    @ai_interview_url.setter
    def ai_interview_url(self, value):
        self._ai_interview_url = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value

    def parse_response_content(self, response_content):
        response = super(ResourceAihrInterviewRoomCreateResponse, self).parse_response_content(response_content)
        if 'ai_interview_id' in response:
            self.ai_interview_id = response['ai_interview_id']
        if 'ai_interview_url' in response:
            self.ai_interview_url = response['ai_interview_url']
        if 'end_time' in response:
            self.end_time = response['end_time']
