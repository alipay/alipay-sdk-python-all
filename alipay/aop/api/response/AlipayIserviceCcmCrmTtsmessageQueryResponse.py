#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AsrTtsSlsMessage import AsrTtsSlsMessage


class AlipayIserviceCcmCrmTtsmessageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmCrmTtsmessageQueryResponse, self).__init__()
        self._tts_message_list = None

    @property
    def tts_message_list(self):
        return self._tts_message_list

    @tts_message_list.setter
    def tts_message_list(self, value):
        if isinstance(value, list):
            self._tts_message_list = list()
            for i in value:
                if isinstance(i, AsrTtsSlsMessage):
                    self._tts_message_list.append(i)
                else:
                    self._tts_message_list.append(AsrTtsSlsMessage.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmCrmTtsmessageQueryResponse, self).parse_response_content(response_content)
        if 'tts_message_list' in response:
            self.tts_message_list = response['tts_message_list']
