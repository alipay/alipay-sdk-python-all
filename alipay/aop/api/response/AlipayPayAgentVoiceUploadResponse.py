#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAgentVoiceUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAgentVoiceUploadResponse, self).__init__()
        self._agent_voice_sid = None
        self._stream_voice_init_info = None

    @property
    def agent_voice_sid(self):
        return self._agent_voice_sid

    @agent_voice_sid.setter
    def agent_voice_sid(self, value):
        self._agent_voice_sid = value
    @property
    def stream_voice_init_info(self):
        return self._stream_voice_init_info

    @stream_voice_init_info.setter
    def stream_voice_init_info(self, value):
        self._stream_voice_init_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAgentVoiceUploadResponse, self).parse_response_content(response_content)
        if 'agent_voice_sid' in response:
            self.agent_voice_sid = response['agent_voice_sid']
        if 'stream_voice_init_info' in response:
            self.stream_voice_init_info = response['stream_voice_init_info']
