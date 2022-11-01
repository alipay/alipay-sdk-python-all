#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseMarketingRtaAuthResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingRtaAuthResponse, self).__init__()
        self._auth_campaign_ids = None
        self._biz_no = None

    @property
    def auth_campaign_ids(self):
        return self._auth_campaign_ids

    @auth_campaign_ids.setter
    def auth_campaign_ids(self, value):
        if isinstance(value, list):
            self._auth_campaign_ids = list()
            for i in value:
                self._auth_campaign_ids.append(i)
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingRtaAuthResponse, self).parse_response_content(response_content)
        if 'auth_campaign_ids' in response:
            self.auth_campaign_ids = response['auth_campaign_ids']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
