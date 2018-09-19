#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarDialogonlineAnswerPushResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarDialogonlineAnswerPushResponse, self).__init__()
        self._answer_id = None

    @property
    def answer_id(self):
        return self._answer_id

    @answer_id.setter
    def answer_id(self, value):
        self._answer_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarDialogonlineAnswerPushResponse, self).parse_response_content(response_content)
        if 'answer_id' in response:
            self.answer_id = response['answer_id']
