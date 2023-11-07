#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundMbpcardGencardCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundMbpcardGencardCreateResponse, self).__init__()
        self._gen_card_no = None
        self._status = None

    @property
    def gen_card_no(self):
        return self._gen_card_no

    @gen_card_no.setter
    def gen_card_no(self, value):
        self._gen_card_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundMbpcardGencardCreateResponse, self).parse_response_content(response_content)
        if 'gen_card_no' in response:
            self.gen_card_no = response['gen_card_no']
        if 'status' in response:
            self.status = response['status']
