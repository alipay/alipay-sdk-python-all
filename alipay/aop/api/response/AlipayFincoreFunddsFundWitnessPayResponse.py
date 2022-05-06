#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FdsPayFundItemDTO import FdsPayFundItemDTO


class AlipayFincoreFunddsFundWitnessPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreFunddsFundWitnessPayResponse, self).__init__()
        self._fds_no = None
        self._gmt_create = None
        self._out_request_no = None
        self._pay_fund_item_list = None
        self._total_amount = None

    @property
    def fds_no(self):
        return self._fds_no

    @fds_no.setter
    def fds_no(self, value):
        self._fds_no = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pay_fund_item_list(self):
        return self._pay_fund_item_list

    @pay_fund_item_list.setter
    def pay_fund_item_list(self, value):
        if isinstance(value, list):
            self._pay_fund_item_list = list()
            for i in value:
                if isinstance(i, FdsPayFundItemDTO):
                    self._pay_fund_item_list.append(i)
                else:
                    self._pay_fund_item_list.append(FdsPayFundItemDTO.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreFunddsFundWitnessPayResponse, self).parse_response_content(response_content)
        if 'fds_no' in response:
            self.fds_no = response['fds_no']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'pay_fund_item_list' in response:
            self.pay_fund_item_list = response['pay_fund_item_list']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
