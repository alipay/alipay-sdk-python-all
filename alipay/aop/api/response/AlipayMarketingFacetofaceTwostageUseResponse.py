#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingFacetofaceTwostageUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingFacetofaceTwostageUseResponse, self).__init__()
        self._biz_data = None
        self._havana_id = None
        self._otp_verify = None
        self._user_id = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def otp_verify(self):
        return self._otp_verify

    @otp_verify.setter
    def otp_verify(self, value):
        self._otp_verify = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingFacetofaceTwostageUseResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']
        if 'havana_id' in response:
            self.havana_id = response['havana_id']
        if 'otp_verify' in response:
            self.otp_verify = response['otp_verify']
        if 'user_id' in response:
            self.user_id = response['user_id']
