#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QAChatDetail import QAChatDetail


class AlipayIserviceCcmRobotChatQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmRobotChatQueryResponse, self).__init__()
        self._qa_chats = None
        self._session_id = None

    @property
    def qa_chats(self):
        return self._qa_chats

    @qa_chats.setter
    def qa_chats(self, value):
        if isinstance(value, list):
            self._qa_chats = list()
            for i in value:
                if isinstance(i, QAChatDetail):
                    self._qa_chats.append(i)
                else:
                    self._qa_chats.append(QAChatDetail.from_alipay_dict(i))
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmRobotChatQueryResponse, self).parse_response_content(response_content)
        if 'qa_chats' in response:
            self.qa_chats = response['qa_chats']
        if 'session_id' in response:
            self.session_id = response['session_id']
