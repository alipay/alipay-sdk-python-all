#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FundBill import FundBill


class AlipayCommerceTransportVehicleownerSettlementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehicleownerSettlementQueryResponse, self).__init__()
        self._aquirer = None
        self._biz_ext_info = None
        self._buyer_id = None
        self._discount_amount = None
        self._fund_bill_list = None
        self._m_discount_amount = None
        self._out_trade_no = None
        self._plate_no = None
        self._send_pay_date = None
        self._status = None
        self._subject = None
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
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
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
    def m_discount_amount(self):
        return self._m_discount_amount

    @m_discount_amount.setter
    def m_discount_amount(self, value):
        self._m_discount_amount = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def send_pay_date(self):
        return self._send_pay_date

    @send_pay_date.setter
    def send_pay_date(self, value):
        self._send_pay_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
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
        response = super(AlipayCommerceTransportVehicleownerSettlementQueryResponse, self).parse_response_content(response_content)
        if 'aquirer' in response:
            self.aquirer = response['aquirer']
        if 'biz_ext_info' in response:
            self.biz_ext_info = response['biz_ext_info']
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
        if 'fund_bill_list' in response:
            self.fund_bill_list = response['fund_bill_list']
        if 'm_discount_amount' in response:
            self.m_discount_amount = response['m_discount_amount']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'plate_no' in response:
            self.plate_no = response['plate_no']
        if 'send_pay_date' in response:
            self.send_pay_date = response['send_pay_date']
        if 'status' in response:
            self.status = response['status']
        if 'subject' in response:
            self.subject = response['subject']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
