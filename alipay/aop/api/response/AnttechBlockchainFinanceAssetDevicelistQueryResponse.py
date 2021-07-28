#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetDeviceRelation import AssetDeviceRelation


class AnttechBlockchainFinanceAssetDevicelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceAssetDevicelistQueryResponse, self).__init__()
        self._device_list = None

    @property
    def device_list(self):
        return self._device_list

    @device_list.setter
    def device_list(self, value):
        if isinstance(value, list):
            self._device_list = list()
            for i in value:
                if isinstance(i, AssetDeviceRelation):
                    self._device_list.append(i)
                else:
                    self._device_list.append(AssetDeviceRelation.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceAssetDevicelistQueryResponse, self).parse_response_content(response_content)
        if 'device_list' in response:
            self.device_list = response['device_list']
