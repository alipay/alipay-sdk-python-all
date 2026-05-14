#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftSkuCustomizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftSkuCustomizeQueryResponse, self).__init__()
        self._distribution_status = None
        self._fail_reason = None
        self._nft_id = None

    @property
    def distribution_status(self):
        return self._distribution_status

    @distribution_status.setter
    def distribution_status(self, value):
        self._distribution_status = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftSkuCustomizeQueryResponse, self).parse_response_content(response_content)
        if 'distribution_status' in response:
            self.distribution_status = response['distribution_status']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'nft_id' in response:
            self.nft_id = response['nft_id']
