#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantCard import MerchantCard
from alipay.aop.api.domain.PaidOuterCardExtraInfoDTO import PaidOuterCardExtraInfoDTO


class AlipayMarketingCardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardQueryResponse, self).__init__()
        self._card_info = None
        self._paid_outer_card_info = None
        self._pass_id = None
        self._schema_url = None

    @property
    def card_info(self):
        return self._card_info

    @card_info.setter
    def card_info(self, value):
        if isinstance(value, MerchantCard):
            self._card_info = value
        else:
            self._card_info = MerchantCard.from_alipay_dict(value)
    @property
    def paid_outer_card_info(self):
        return self._paid_outer_card_info

    @paid_outer_card_info.setter
    def paid_outer_card_info(self, value):
        if isinstance(value, PaidOuterCardExtraInfoDTO):
            self._paid_outer_card_info = value
        else:
            self._paid_outer_card_info = PaidOuterCardExtraInfoDTO.from_alipay_dict(value)
    @property
    def pass_id(self):
        return self._pass_id

    @pass_id.setter
    def pass_id(self, value):
        self._pass_id = value
    @property
    def schema_url(self):
        return self._schema_url

    @schema_url.setter
    def schema_url(self, value):
        self._schema_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardQueryResponse, self).parse_response_content(response_content)
        if 'card_info' in response:
            self.card_info = response['card_info']
        if 'paid_outer_card_info' in response:
            self.paid_outer_card_info = response['paid_outer_card_info']
        if 'pass_id' in response:
            self.pass_id = response['pass_id']
        if 'schema_url' in response:
            self.schema_url = response['schema_url']
