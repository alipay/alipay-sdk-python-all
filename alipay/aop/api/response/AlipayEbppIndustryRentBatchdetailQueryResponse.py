#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentPayQueryBillDetailListResponse import RentPayQueryBillDetailListResponse


class AlipayEbppIndustryRentBatchdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRentBatchdetailQueryResponse, self).__init__()
        self._bill_detail_list = None
        self._page_num = None
        self._page_size = None
        self._total_count = None
        self._total_page = None

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
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRentBatchdetailQueryResponse, self).parse_response_content(response_content)
        if 'bill_detail_list' in response:
            self.bill_detail_list = response['bill_detail_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_page' in response:
            self.total_page = response['total_page']
