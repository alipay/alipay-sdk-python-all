#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TradeFundBillDetail import TradeFundBillDetail
from alipay.aop.api.domain.TradeInfoDTO import TradeInfoDTO


class AlipayFundJointaccountTradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountTradeQueryResponse, self).__init__()
        self._buyer_id = None
        self._create_time = None
        self._total_amount = None
        self._trade_fund_bill_list = None
        self._trade_info_list = None
        self._trade_no = None
        self._trade_status = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_fund_bill_list(self):
        return self._trade_fund_bill_list

    @trade_fund_bill_list.setter
    def trade_fund_bill_list(self, value):
        if isinstance(value, list):
            self._trade_fund_bill_list = list()
            for i in value:
                if isinstance(i, TradeFundBillDetail):
                    self._trade_fund_bill_list.append(i)
                else:
                    self._trade_fund_bill_list.append(TradeFundBillDetail.from_alipay_dict(i))
    @property
    def trade_info_list(self):
        return self._trade_info_list

    @trade_info_list.setter
    def trade_info_list(self, value):
        if isinstance(value, list):
            self._trade_info_list = list()
            for i in value:
                if isinstance(i, TradeInfoDTO):
                    self._trade_info_list.append(i)
                else:
                    self._trade_info_list.append(TradeInfoDTO.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountTradeQueryResponse, self).parse_response_content(response_content)
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_fund_bill_list' in response:
            self.trade_fund_bill_list = response['trade_fund_bill_list']
        if 'trade_info_list' in response:
            self.trade_info_list = response['trade_info_list']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
