#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetPointVoucherprodBenefittemplateSettleResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointVoucherprodBenefittemplateSettleResponse, self).__init__()
        self._asset_id = None
        self._bill_no = None
        self._settle_amount = None
        self._status = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointVoucherprodBenefittemplateSettleResponse, self).parse_response_content(response_content)
        if 'asset_id' in response:
            self.asset_id = response['asset_id']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'settle_amount' in response:
            self.settle_amount = response['settle_amount']
        if 'status' in response:
            self.status = response['status']
