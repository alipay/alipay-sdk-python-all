#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PhoneCardNumberModel import PhoneCardNumberModel


class AlipayCommerceAcommunicationDistributionPhonecardnoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDistributionPhonecardnoQueryResponse, self).__init__()
        self._phone_card_number_list = None

    @property
    def phone_card_number_list(self):
        return self._phone_card_number_list

    @phone_card_number_list.setter
    def phone_card_number_list(self, value):
        if isinstance(value, list):
            self._phone_card_number_list = list()
            for i in value:
                if isinstance(i, PhoneCardNumberModel):
                    self._phone_card_number_list.append(i)
                else:
                    self._phone_card_number_list.append(PhoneCardNumberModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDistributionPhonecardnoQueryResponse, self).parse_response_content(response_content)
        if 'phone_card_number_list' in response:
            self.phone_card_number_list = response['phone_card_number_list']
