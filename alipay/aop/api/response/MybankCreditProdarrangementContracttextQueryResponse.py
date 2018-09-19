#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditProdarrangementContracttextQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditProdarrangementContracttextQueryResponse, self).__init__()
        self._text = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditProdarrangementContracttextQueryResponse, self).parse_response_content(response_content)
        if 'text' in response:
            self.text = response['text']
