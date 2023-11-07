#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CardDetailInfo import CardDetailInfo


class AlipayFundMbpcardCardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundMbpcardCardQueryResponse, self).__init__()
        self._mbp_card_list = None

    @property
    def mbp_card_list(self):
        return self._mbp_card_list

    @mbp_card_list.setter
    def mbp_card_list(self, value):
        if isinstance(value, CardDetailInfo):
            self._mbp_card_list = value
        else:
            self._mbp_card_list = CardDetailInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFundMbpcardCardQueryResponse, self).parse_response_content(response_content)
        if 'mbp_card_list' in response:
            self.mbp_card_list = response['mbp_card_list']
