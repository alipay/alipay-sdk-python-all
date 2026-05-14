#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketingResultpageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketingResultpageQueryResponse, self).__init__()
        self._biztid = None
        self._result_page_content = None
        self._trade_no = None
        self._voice_text = None

    @property
    def biztid(self):
        return self._biztid

    @biztid.setter
    def biztid(self, value):
        self._biztid = value
    @property
    def result_page_content(self):
        return self._result_page_content

    @result_page_content.setter
    def result_page_content(self, value):
        self._result_page_content = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def voice_text(self):
        return self._voice_text

    @voice_text.setter
    def voice_text(self, value):
        self._voice_text = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketingResultpageQueryResponse, self).parse_response_content(response_content)
        if 'biztid' in response:
            self.biztid = response['biztid']
        if 'result_page_content' in response:
            self.result_page_content = response['result_page_content']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'voice_text' in response:
            self.voice_text = response['voice_text']
