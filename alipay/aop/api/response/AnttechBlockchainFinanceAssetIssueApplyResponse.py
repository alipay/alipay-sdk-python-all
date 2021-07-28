#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceAssetIssueApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceAssetIssueApplyResponse, self).__init__()
        self._asset_id = None
        self._out_asset_id = None
        self._sign_data = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def out_asset_id(self):
        return self._out_asset_id

    @out_asset_id.setter
    def out_asset_id(self, value):
        self._out_asset_id = value
    @property
    def sign_data(self):
        return self._sign_data

    @sign_data.setter
    def sign_data(self, value):
        self._sign_data = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceAssetIssueApplyResponse, self).parse_response_content(response_content)
        if 'asset_id' in response:
            self.asset_id = response['asset_id']
        if 'out_asset_id' in response:
            self.out_asset_id = response['out_asset_id']
        if 'sign_data' in response:
            self.sign_data = response['sign_data']
