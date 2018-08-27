#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingSharetokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingSharetokenCreateResponse, self).__init__()
        self._expire_date = None
        self._guider_str_1 = None
        self._guider_str_2 = None
        self._share_token = None
        self._start_date = None

    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def guider_str_1(self):
        return self._guider_str_1

    @guider_str_1.setter
    def guider_str_1(self, value):
        self._guider_str_1 = value
    @property
    def guider_str_2(self):
        return self._guider_str_2

    @guider_str_2.setter
    def guider_str_2(self, value):
        self._guider_str_2 = value
    @property
    def share_token(self):
        return self._share_token

    @share_token.setter
    def share_token(self, value):
        self._share_token = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, list):
            self._start_date = list()
            for i in value:
                self._start_date.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingSharetokenCreateResponse, self).parse_response_content(response_content)
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'guider_str_1' in response:
            self.guider_str_1 = response['guider_str_1']
        if 'guider_str_2' in response:
            self.guider_str_2 = response['guider_str_2']
        if 'share_token' in response:
            self.share_token = response['share_token']
        if 'start_date' in response:
            self.start_date = response['start_date']
