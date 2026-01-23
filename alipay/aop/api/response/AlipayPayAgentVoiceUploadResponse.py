#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAgentVoiceUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAgentVoiceUploadResponse, self).__init__()
        self._agent_voice_sid = None

    @property
    def agent_voice_sid(self):
        return self._agent_voice_sid

    @agent_voice_sid.setter
    def agent_voice_sid(self, value):
        self._agent_voice_sid = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAgentVoiceUploadResponse, self).parse_response_content(response_content)
        if 'agent_voice_sid' in response:
            self.agent_voice_sid = response['agent_voice_sid']
