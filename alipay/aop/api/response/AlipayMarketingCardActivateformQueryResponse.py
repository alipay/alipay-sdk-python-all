#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCardActivateformQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardActivateformQueryResponse, self).__init__()
        self._infos = None

    @property
    def infos(self):
        return self._infos

    @infos.setter
    def infos(self, value):
        self._infos = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardActivateformQueryResponse, self).parse_response_content(response_content)
        if 'infos' in response:
            self.infos = response['infos']
