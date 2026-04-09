#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAgentwhitelistGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAgentwhitelistGetResponse, self).__init__()
        self._white_list = None

    @property
    def white_list(self):
        return self._white_list

    @white_list.setter
    def white_list(self, value):
        if isinstance(value, list):
            self._white_list = list()
            for i in value:
                self._white_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAgentwhitelistGetResponse, self).parse_response_content(response_content)
        if 'white_list' in response:
            self.white_list = response['white_list']
