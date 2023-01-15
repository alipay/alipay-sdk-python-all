#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantChargeInfo import MerchantChargeInfo


class DatadigitalFincloudGeneralsaasFaceFeeQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasFaceFeeQueryResponse, self).__init__()
        self._fee_info = None

    @property
    def fee_info(self):
        return self._fee_info

    @fee_info.setter
    def fee_info(self, value):
        if isinstance(value, list):
            self._fee_info = list()
            for i in value:
                if isinstance(i, MerchantChargeInfo):
                    self._fee_info.append(i)
                else:
                    self._fee_info.append(MerchantChargeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasFaceFeeQueryResponse, self).parse_response_content(response_content)
        if 'fee_info' in response:
            self.fee_info = response['fee_info']
