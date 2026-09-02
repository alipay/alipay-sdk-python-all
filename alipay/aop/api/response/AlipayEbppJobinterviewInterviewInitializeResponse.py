#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJobinterviewInterviewInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJobinterviewInterviewInitializeResponse, self).__init__()
        self._candidate_id = None
        self._interview_url = None
        self._room_expire_time = None
        self._status = None

    @property
    def candidate_id(self):
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, value):
        self._candidate_id = value
    @property
    def interview_url(self):
        return self._interview_url

    @interview_url.setter
    def interview_url(self, value):
        self._interview_url = value
    @property
    def room_expire_time(self):
        return self._room_expire_time

    @room_expire_time.setter
    def room_expire_time(self, value):
        self._room_expire_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJobinterviewInterviewInitializeResponse, self).parse_response_content(response_content)
        if 'candidate_id' in response:
            self.candidate_id = response['candidate_id']
        if 'interview_url' in response:
            self.interview_url = response['interview_url']
        if 'room_expire_time' in response:
            self.room_expire_time = response['room_expire_time']
        if 'status' in response:
            self.status = response['status']
