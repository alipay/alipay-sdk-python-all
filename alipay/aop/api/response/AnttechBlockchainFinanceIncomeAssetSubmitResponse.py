#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceIncomeAssetSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceIncomeAssetSubmitResponse, self).__init__()
        self._asset_id = None
        self._biz_no = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceIncomeAssetSubmitResponse, self).parse_response_content(response_content)
        if 'asset_id' in response:
            self.asset_id = response['asset_id']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
