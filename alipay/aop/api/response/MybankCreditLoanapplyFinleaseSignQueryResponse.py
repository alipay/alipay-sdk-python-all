#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyFinleaseSignQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyFinleaseSignQueryResponse, self).__init__()
        self._msg_content = None

    @property
    def msg_content(self):
        return self._msg_content

    @msg_content.setter
    def msg_content(self, value):
        self._msg_content = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyFinleaseSignQueryResponse, self).parse_response_content(response_content)
        if 'msg_content' in response:
            self.msg_content = response['msg_content']
