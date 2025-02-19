#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryBotQueryRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryBotQueryRecommendResponse, self).__init__()
        self._ask_more_list = None

    @property
    def ask_more_list(self):
        return self._ask_more_list

    @ask_more_list.setter
    def ask_more_list(self, value):
        if isinstance(value, list):
            self._ask_more_list = list()
            for i in value:
                self._ask_more_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryBotQueryRecommendResponse, self).parse_response_content(response_content)
        if 'ask_more_list' in response:
            self.ask_more_list = response['ask_more_list']
