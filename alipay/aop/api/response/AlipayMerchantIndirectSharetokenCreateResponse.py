#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectSharetokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectSharetokenCreateResponse, self).__init__()
        self._biz_token = None
        self._expire_date = None
        self._guide_text_1 = None
        self._guide_text_2 = None
        self._share_token = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def guide_text_1(self):
        return self._guide_text_1

    @guide_text_1.setter
    def guide_text_1(self, value):
        self._guide_text_1 = value
    @property
    def guide_text_2(self):
        return self._guide_text_2

    @guide_text_2.setter
    def guide_text_2(self, value):
        self._guide_text_2 = value
    @property
    def share_token(self):
        return self._share_token

    @share_token.setter
    def share_token(self, value):
        self._share_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectSharetokenCreateResponse, self).parse_response_content(response_content)
        if 'biz_token' in response:
            self.biz_token = response['biz_token']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'guide_text_1' in response:
            self.guide_text_1 = response['guide_text_1']
        if 'guide_text_2' in response:
            self.guide_text_2 = response['guide_text_2']
        if 'share_token' in response:
            self.share_token = response['share_token']
