#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChatHistory import ChatHistory


class AlipayCloudCloudpromoAichatHistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAichatHistoryQueryResponse, self).__init__()
        self._histories = None

    @property
    def histories(self):
        return self._histories

    @histories.setter
    def histories(self, value):
        if isinstance(value, ChatHistory):
            self._histories = value
        else:
            self._histories = ChatHistory.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAichatHistoryQueryResponse, self).parse_response_content(response_content)
        if 'histories' in response:
            self.histories = response['histories']
