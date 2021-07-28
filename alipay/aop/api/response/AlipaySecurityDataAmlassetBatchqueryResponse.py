#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmlAssetRecord import AmlAssetRecord


class AlipaySecurityDataAmlassetBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataAmlassetBatchqueryResponse, self).__init__()
        self._asset_records = None

    @property
    def asset_records(self):
        return self._asset_records

    @asset_records.setter
    def asset_records(self, value):
        if isinstance(value, list):
            self._asset_records = list()
            for i in value:
                if isinstance(i, AmlAssetRecord):
                    self._asset_records.append(i)
                else:
                    self._asset_records.append(AmlAssetRecord.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataAmlassetBatchqueryResponse, self).parse_response_content(response_content)
        if 'asset_records' in response:
            self.asset_records = response['asset_records']
