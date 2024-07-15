#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetEcoBillDetail import AssetEcoBillDetail


class AntMerchantExpandEcoBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandEcoBillQueryResponse, self).__init__()
        self._bill_date = None
        self._eco_bill_details = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def eco_bill_details(self):
        return self._eco_bill_details

    @eco_bill_details.setter
    def eco_bill_details(self, value):
        if isinstance(value, list):
            self._eco_bill_details = list()
            for i in value:
                if isinstance(i, AssetEcoBillDetail):
                    self._eco_bill_details.append(i)
                else:
                    self._eco_bill_details.append(AssetEcoBillDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandEcoBillQueryResponse, self).parse_response_content(response_content)
        if 'bill_date' in response:
            self.bill_date = response['bill_date']
        if 'eco_bill_details' in response:
            self.eco_bill_details = response['eco_bill_details']
