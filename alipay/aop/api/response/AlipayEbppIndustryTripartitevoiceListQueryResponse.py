#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TripartiteVoice import TripartiteVoice


class AlipayEbppIndustryTripartitevoiceListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryTripartitevoiceListQueryResponse, self).__init__()
        self._total_count = None
        self._voice_list = None

    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def voice_list(self):
        return self._voice_list

    @voice_list.setter
    def voice_list(self, value):
        if isinstance(value, list):
            self._voice_list = list()
            for i in value:
                if isinstance(i, TripartiteVoice):
                    self._voice_list.append(i)
                else:
                    self._voice_list.append(TripartiteVoice.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryTripartitevoiceListQueryResponse, self).parse_response_content(response_content)
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'voice_list' in response:
            self.voice_list = response['voice_list']
