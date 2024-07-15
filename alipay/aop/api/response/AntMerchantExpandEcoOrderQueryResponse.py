#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetEcoOrderBillDetail import AssetEcoOrderBillDetail


class AntMerchantExpandEcoOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandEcoOrderQueryResponse, self).__init__()
        self._bill_date = None
        self._eco_order_bill_details = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def eco_order_bill_details(self):
        return self._eco_order_bill_details

    @eco_order_bill_details.setter
    def eco_order_bill_details(self, value):
        if isinstance(value, list):
            self._eco_order_bill_details = list()
            for i in value:
                if isinstance(i, AssetEcoOrderBillDetail):
                    self._eco_order_bill_details.append(i)
                else:
                    self._eco_order_bill_details.append(AssetEcoOrderBillDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandEcoOrderQueryResponse, self).parse_response_content(response_content)
        if 'bill_date' in response:
            self.bill_date = response['bill_date']
        if 'eco_order_bill_details' in response:
            self.eco_order_bill_details = response['eco_order_bill_details']
