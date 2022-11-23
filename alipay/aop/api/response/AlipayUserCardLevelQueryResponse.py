#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CardLevelConfigDTO import CardLevelConfigDTO


class AlipayUserCardLevelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCardLevelQueryResponse, self).__init__()
        self._card_level_configs = None

    @property
    def card_level_configs(self):
        return self._card_level_configs

    @card_level_configs.setter
    def card_level_configs(self, value):
        if isinstance(value, list):
            self._card_level_configs = list()
            for i in value:
                if isinstance(i, CardLevelConfigDTO):
                    self._card_level_configs.append(i)
                else:
                    self._card_level_configs.append(CardLevelConfigDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserCardLevelQueryResponse, self).parse_response_content(response_content)
        if 'card_level_configs' in response:
            self.card_level_configs = response['card_level_configs']
