#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentBillOrderDetailDto import RentBillOrderDetailDto
from alipay.aop.api.domain.RentBillRoyaltyDetailDto import RentBillRoyaltyDetailDto


class AlipayCommerceRentOrderBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentOrderBillQueryResponse, self).__init__()
        self._biz_order_id = None
        self._order_detail_list = None
        self._royalty_detail_list = None
        self._total_actual_royalty_amount = None
        self._total_royalty_amount = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def order_detail_list(self):
        return self._order_detail_list

    @order_detail_list.setter
    def order_detail_list(self, value):
        if isinstance(value, list):
            self._order_detail_list = list()
            for i in value:
                if isinstance(i, RentBillOrderDetailDto):
                    self._order_detail_list.append(i)
                else:
                    self._order_detail_list.append(RentBillOrderDetailDto.from_alipay_dict(i))
    @property
    def royalty_detail_list(self):
        return self._royalty_detail_list

    @royalty_detail_list.setter
    def royalty_detail_list(self, value):
        if isinstance(value, list):
            self._royalty_detail_list = list()
            for i in value:
                if isinstance(i, RentBillRoyaltyDetailDto):
                    self._royalty_detail_list.append(i)
                else:
                    self._royalty_detail_list.append(RentBillRoyaltyDetailDto.from_alipay_dict(i))
    @property
    def total_actual_royalty_amount(self):
        return self._total_actual_royalty_amount

    @total_actual_royalty_amount.setter
    def total_actual_royalty_amount(self, value):
        self._total_actual_royalty_amount = value
    @property
    def total_royalty_amount(self):
        return self._total_royalty_amount

    @total_royalty_amount.setter
    def total_royalty_amount(self, value):
        self._total_royalty_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentOrderBillQueryResponse, self).parse_response_content(response_content)
        if 'biz_order_id' in response:
            self.biz_order_id = response['biz_order_id']
        if 'order_detail_list' in response:
            self.order_detail_list = response['order_detail_list']
        if 'royalty_detail_list' in response:
            self.royalty_detail_list = response['royalty_detail_list']
        if 'total_actual_royalty_amount' in response:
            self.total_actual_royalty_amount = response['total_actual_royalty_amount']
        if 'total_royalty_amount' in response:
            self.total_royalty_amount = response['total_royalty_amount']
