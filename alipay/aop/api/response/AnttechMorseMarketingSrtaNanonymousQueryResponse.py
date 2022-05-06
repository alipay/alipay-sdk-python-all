#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseMarketingSrtaNanonymousQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingSrtaNanonymousQueryResponse, self).__init__()
        self._biz_no = None
        self._blind_signed_mobile_sha_256 = None
        self._result_cipher_list = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def blind_signed_mobile_sha_256(self):
        return self._blind_signed_mobile_sha_256

    @blind_signed_mobile_sha_256.setter
    def blind_signed_mobile_sha_256(self, value):
        self._blind_signed_mobile_sha_256 = value
    @property
    def result_cipher_list(self):
        return self._result_cipher_list

    @result_cipher_list.setter
    def result_cipher_list(self, value):
        self._result_cipher_list = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingSrtaNanonymousQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'blind_signed_mobile_sha_256' in response:
            self.blind_signed_mobile_sha_256 = response['blind_signed_mobile_sha_256']
        if 'result_cipher_list' in response:
            self.result_cipher_list = response['result_cipher_list']
