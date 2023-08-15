#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TextProduceStatus import TextProduceStatus


class AlipayDigitalopUcdpApecreativeTextprocessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalopUcdpApecreativeTextprocessQueryResponse, self).__init__()
        self._text_produce_status_list = None

    @property
    def text_produce_status_list(self):
        return self._text_produce_status_list

    @text_produce_status_list.setter
    def text_produce_status_list(self, value):
        if isinstance(value, list):
            self._text_produce_status_list = list()
            for i in value:
                if isinstance(i, TextProduceStatus):
                    self._text_produce_status_list.append(i)
                else:
                    self._text_produce_status_list.append(TextProduceStatus.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalopUcdpApecreativeTextprocessQueryResponse, self).parse_response_content(response_content)
        if 'text_produce_status_list' in response:
            self.text_produce_status_list = response['text_produce_status_list']
