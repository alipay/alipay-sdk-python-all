#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetCardTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetCardTransferResponse, self).__init__()
        self._asset_order_id = None

    @property
    def asset_order_id(self):
        return self._asset_order_id

    @asset_order_id.setter
    def asset_order_id(self, value):
        self._asset_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetCardTransferResponse, self).parse_response_content(response_content)
        if 'asset_order_id' in response:
            self.asset_order_id = response['asset_order_id']
