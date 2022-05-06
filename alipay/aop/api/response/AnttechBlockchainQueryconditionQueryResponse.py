#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainQueryconditionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainQueryconditionQueryResponse, self).__init__()
        self._season = None

    @property
    def season(self):
        return self._season

    @season.setter
    def season(self, value):
        self._season = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainQueryconditionQueryResponse, self).parse_response_content(response_content)
        if 'season' in response:
            self.season = response['season']
