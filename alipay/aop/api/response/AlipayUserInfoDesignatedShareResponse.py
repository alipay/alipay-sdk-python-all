#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserDebitCardInfo import UserDebitCardInfo


class AlipayUserInfoDesignatedShareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserInfoDesignatedShareResponse, self).__init__()
        self._debit_card_info = None

    @property
    def debit_card_info(self):
        return self._debit_card_info

    @debit_card_info.setter
    def debit_card_info(self, value):
        if isinstance(value, UserDebitCardInfo):
            self._debit_card_info = value
        else:
            self._debit_card_info = UserDebitCardInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserInfoDesignatedShareResponse, self).parse_response_content(response_content)
        if 'debit_card_info' in response:
            self.debit_card_info = response['debit_card_info']
