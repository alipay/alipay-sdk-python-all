#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DTAgentChatResult import DTAgentChatResult
from alipay.aop.api.domain.DTAgentChatStream import DTAgentChatStream
from alipay.aop.api.domain.DTAgentTagInfo import DTAgentTagInfo


class AnttechAiAgentChatQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiAgentChatQueryResponse, self).__init__()
        self._chat_result = None
        self._process_status = None
        self._stream = None
        self._tags = None

    @property
    def chat_result(self):
        return self._chat_result

    @chat_result.setter
    def chat_result(self, value):
        if isinstance(value, DTAgentChatResult):
            self._chat_result = value
        else:
            self._chat_result = DTAgentChatResult.from_alipay_dict(value)
    @property
    def process_status(self):
        return self._process_status

    @process_status.setter
    def process_status(self, value):
        self._process_status = value
    @property
    def stream(self):
        return self._stream

    @stream.setter
    def stream(self, value):
        if isinstance(value, DTAgentChatStream):
            self._stream = value
        else:
            self._stream = DTAgentChatStream.from_alipay_dict(value)
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                if isinstance(i, DTAgentTagInfo):
                    self._tags.append(i)
                else:
                    self._tags.append(DTAgentTagInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechAiAgentChatQueryResponse, self).parse_response_content(response_content)
        if 'chat_result' in response:
            self.chat_result = response['chat_result']
        if 'process_status' in response:
            self.process_status = response['process_status']
        if 'stream' in response:
            self.stream = response['stream']
        if 'tags' in response:
            self.tags = response['tags']
