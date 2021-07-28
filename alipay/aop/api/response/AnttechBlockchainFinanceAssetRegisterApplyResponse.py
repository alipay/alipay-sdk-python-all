#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceAssetRegisterApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceAssetRegisterApplyResponse, self).__init__()
        self._apply_result = None
        self._asset_id = None
        self._out_asset_id = None

    @property
    def apply_result(self):
        return self._apply_result

    @apply_result.setter
    def apply_result(self, value):
        self._apply_result = value
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

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceAssetRegisterApplyResponse, self).parse_response_content(response_content)
        if 'apply_result' in response:
            self.apply_result = response['apply_result']
        if 'asset_id' in response:
            self.asset_id = response['asset_id']
        if 'out_asset_id' in response:
            self.out_asset_id = response['out_asset_id']
