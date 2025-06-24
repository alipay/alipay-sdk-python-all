#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHdfaitransferConclusionGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHdfaitransferConclusionGenerateResponse, self).__init__()
        self._conclusion_summary = None

    @property
    def conclusion_summary(self):
        return self._conclusion_summary

    @conclusion_summary.setter
    def conclusion_summary(self, value):
        self._conclusion_summary = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHdfaitransferConclusionGenerateResponse, self).parse_response_content(response_content)
        if 'conclusion_summary' in response:
            self.conclusion_summary = response['conclusion_summary']
