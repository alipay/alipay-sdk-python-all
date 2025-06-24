#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TinyGameRes import TinyGameRes


class AlipayDataDataserviceAdcampaignTinygameQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignTinygameQueryResponse, self).__init__()
        self._tiny_game_list = None

    @property
    def tiny_game_list(self):
        return self._tiny_game_list

    @tiny_game_list.setter
    def tiny_game_list(self, value):
        if isinstance(value, list):
            self._tiny_game_list = list()
            for i in value:
                if isinstance(i, TinyGameRes):
                    self._tiny_game_list.append(i)
                else:
                    self._tiny_game_list.append(TinyGameRes.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignTinygameQueryResponse, self).parse_response_content(response_content)
        if 'tiny_game_list' in response:
            self.tiny_game_list = response['tiny_game_list']
