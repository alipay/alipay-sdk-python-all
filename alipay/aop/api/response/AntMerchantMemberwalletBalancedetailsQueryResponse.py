#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberWalletBalanceDetailVO import MemberWalletBalanceDetailVO


class AntMerchantMemberwalletBalancedetailsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantMemberwalletBalancedetailsQueryResponse, self).__init__()
        self._balance_detail_list = None
        self._page_no = None
        self._page_size = None
        self._row_count = None

    @property
    def balance_detail_list(self):
        return self._balance_detail_list

    @balance_detail_list.setter
    def balance_detail_list(self, value):
        if isinstance(value, list):
            self._balance_detail_list = list()
            for i in value:
                if isinstance(i, MemberWalletBalanceDetailVO):
                    self._balance_detail_list.append(i)
                else:
                    self._balance_detail_list.append(MemberWalletBalanceDetailVO.from_alipay_dict(i))
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def row_count(self):
        return self._row_count

    @row_count.setter
    def row_count(self, value):
        self._row_count = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantMemberwalletBalancedetailsQueryResponse, self).parse_response_content(response_content)
        if 'balance_detail_list' in response:
            self.balance_detail_list = response['balance_detail_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'row_count' in response:
            self.row_count = response['row_count']
