#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TradeAwardDetail import TradeAwardDetail


class AlipayCommerceOperationPromoAwardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoAwardQueryResponse, self).__init__()
        self._award_amount = None
        self._page_num = None
        self._page_size = None
        self._sign_up_id = None
        self._total_awarded_amount = None
        self._total_page = None
        self._trade_award_details = None
        self._trade_count = None

    @property
    def award_amount(self):
        return self._award_amount

    @award_amount.setter
    def award_amount(self, value):
        self._award_amount = value
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
    def sign_up_id(self):
        return self._sign_up_id

    @sign_up_id.setter
    def sign_up_id(self, value):
        self._sign_up_id = value
    @property
    def total_awarded_amount(self):
        return self._total_awarded_amount

    @total_awarded_amount.setter
    def total_awarded_amount(self, value):
        self._total_awarded_amount = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value
    @property
    def trade_award_details(self):
        return self._trade_award_details

    @trade_award_details.setter
    def trade_award_details(self, value):
        if isinstance(value, list):
            self._trade_award_details = list()
            for i in value:
                if isinstance(i, TradeAwardDetail):
                    self._trade_award_details.append(i)
                else:
                    self._trade_award_details.append(TradeAwardDetail.from_alipay_dict(i))
    @property
    def trade_count(self):
        return self._trade_count

    @trade_count.setter
    def trade_count(self, value):
        self._trade_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoAwardQueryResponse, self).parse_response_content(response_content)
        if 'award_amount' in response:
            self.award_amount = response['award_amount']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'sign_up_id' in response:
            self.sign_up_id = response['sign_up_id']
        if 'total_awarded_amount' in response:
            self.total_awarded_amount = response['total_awarded_amount']
        if 'total_page' in response:
            self.total_page = response['total_page']
        if 'trade_award_details' in response:
            self.trade_award_details = response['trade_award_details']
        if 'trade_count' in response:
            self.trade_count = response['trade_count']
