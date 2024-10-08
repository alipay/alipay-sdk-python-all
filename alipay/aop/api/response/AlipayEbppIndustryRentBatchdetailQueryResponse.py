#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentPayQueryBillDetailListResponse import RentPayQueryBillDetailListResponse


class AlipayEbppIndustryRentBatchdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRentBatchdetailQueryResponse, self).__init__()
        self._bill_detail_list = None

    @property
    def bill_detail_list(self):
        return self._bill_detail_list

    @bill_detail_list.setter
    def bill_detail_list(self, value):
        if isinstance(value, list):
            self._bill_detail_list = list()
            for i in value:
                if isinstance(i, RentPayQueryBillDetailListResponse):
                    self._bill_detail_list.append(i)
                else:
                    self._bill_detail_list.append(RentPayQueryBillDetailListResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRentBatchdetailQueryResponse, self).parse_response_content(response_content)
        if 'bill_detail_list' in response:
            self.bill_detail_list = response['bill_detail_list']
