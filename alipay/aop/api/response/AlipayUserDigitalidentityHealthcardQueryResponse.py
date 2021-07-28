#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HealthCardInfo import HealthCardInfo


class AlipayUserDigitalidentityHealthcardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDigitalidentityHealthcardQueryResponse, self).__init__()
        self._health_card_info = None

    @property
    def health_card_info(self):
        return self._health_card_info

    @health_card_info.setter
    def health_card_info(self, value):
        if isinstance(value, HealthCardInfo):
            self._health_card_info = value
        else:
            self._health_card_info = HealthCardInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserDigitalidentityHealthcardQueryResponse, self).parse_response_content(response_content)
        if 'health_card_info' in response:
            self.health_card_info = response['health_card_info']
