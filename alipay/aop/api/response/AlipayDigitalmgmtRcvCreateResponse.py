#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtRcvCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtRcvCreateResponse, self).__init__()
        self._rcv_number_list = None

    @property
    def rcv_number_list(self):
        return self._rcv_number_list

    @rcv_number_list.setter
    def rcv_number_list(self, value):
        if isinstance(value, list):
            self._rcv_number_list = list()
            for i in value:
                self._rcv_number_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtRcvCreateResponse, self).parse_response_content(response_content)
        if 'rcv_number_list' in response:
            self.rcv_number_list = response['rcv_number_list']
