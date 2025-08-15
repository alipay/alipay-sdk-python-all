#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalNpsScoreSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalNpsScoreSubmitResponse, self).__init__()
        self._deal_info = None

    @property
    def deal_info(self):
        return self._deal_info

    @deal_info.setter
    def deal_info(self, value):
        self._deal_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalNpsScoreSubmitResponse, self).parse_response_content(response_content)
        if 'deal_info' in response:
            self.deal_info = response['deal_info']
