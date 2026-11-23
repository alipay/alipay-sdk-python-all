#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiGreenBehaviorItem import OpenApiGreenBehaviorItem


class AlipayCommerceCarboninclusionGreenbehaviorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCarboninclusionGreenbehaviorQueryResponse, self).__init__()
        self._behavior_list = None
        self._next_page_token = None

    @property
    def behavior_list(self):
        return self._behavior_list

    @behavior_list.setter
    def behavior_list(self, value):
        if isinstance(value, list):
            self._behavior_list = list()
            for i in value:
                if isinstance(i, OpenApiGreenBehaviorItem):
                    self._behavior_list.append(i)
                else:
                    self._behavior_list.append(OpenApiGreenBehaviorItem.from_alipay_dict(i))
    @property
    def next_page_token(self):
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, value):
        self._next_page_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCarboninclusionGreenbehaviorQueryResponse, self).parse_response_content(response_content)
        if 'behavior_list' in response:
            self.behavior_list = response['behavior_list']
        if 'next_page_token' in response:
            self.next_page_token = response['next_page_token']
