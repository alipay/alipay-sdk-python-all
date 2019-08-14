#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FundBill import FundBill


class AlipayCommerceTransportVehicleownerSettlementApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehicleownerSettlementApplyResponse, self).__init__()
        self._aquirer = None
        self._biz_ext_info = None
        self._buyer_id = None
        self._fund_bill_list = None
        self._gmt_payment = None
        self._out_trade_no = None
        self._pay_amount = None
        self._plate_no = None
        self._status = None
        self._total_amount = None
        self._trade_no = None

    @property
    def aquirer(self):
        return self._aquirer

    @aquirer.setter
    def aquirer(self, value):
        self._aquirer = value
    @property
    def biz_ext_info(self):
        return self._biz_ext_info

    @biz_ext_info.setter
    def biz_ext_info(self, value):
        self._biz_ext_info = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def fund_bill_list(self):
        return self._fund_bill_list

    @fund_bill_list.setter
    def fund_bill_list(self, value):
        if isinstance(value, list):
            self._fund_bill_list = list()
            for i in value:
                if isinstance(i, FundBill):
                    self._fund_bill_list.append(i)
                else:
                    self._fund_bill_list.append(FundBill.from_alipay_dict(i))
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehicleownerSettlementApplyResponse, self).parse_response_content(response_content)
        if 'aquirer' in response:
            self.aquirer = response['aquirer']
        if 'biz_ext_info' in response:
            self.biz_ext_info = response['biz_ext_info']
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'fund_bill_list' in response:
            self.fund_bill_list = response['fund_bill_list']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'plate_no' in response:
            self.plate_no = response['plate_no']
        if 'status' in response:
            self.status = response['status']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
