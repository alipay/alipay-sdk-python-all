#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserSportshealthAccountDepositResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSportshealthAccountDepositResponse, self).__init__()
        self._award_amount = None

    @property
    def award_amount(self):
        return self._award_amount

    @award_amount.setter
    def award_amount(self, value):
        self._award_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserSportshealthAccountDepositResponse, self).parse_response_content(response_content)
        if 'award_amount' in response:
            self.award_amount = response['award_amount']
