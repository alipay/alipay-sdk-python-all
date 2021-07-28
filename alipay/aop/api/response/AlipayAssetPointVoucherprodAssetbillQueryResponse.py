#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetBillInfo import AssetBillInfo


class AlipayAssetPointVoucherprodAssetbillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointVoucherprodAssetbillQueryResponse, self).__init__()
        self._asset_bill_info = None

    @property
    def asset_bill_info(self):
        return self._asset_bill_info

    @asset_bill_info.setter
    def asset_bill_info(self, value):
        if isinstance(value, list):
            self._asset_bill_info = list()
            for i in value:
                if isinstance(i, AssetBillInfo):
                    self._asset_bill_info.append(i)
                else:
                    self._asset_bill_info.append(AssetBillInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointVoucherprodAssetbillQueryResponse, self).parse_response_content(response_content)
        if 'asset_bill_info' in response:
            self.asset_bill_info = response['asset_bill_info']
