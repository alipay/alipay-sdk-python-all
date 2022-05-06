#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DepositBackInfo import DepositBackInfo
from alipay.aop.api.domain.EnterprisePayInfo import EnterprisePayInfo
from alipay.aop.api.domain.TradeFundBill import TradeFundBill
from alipay.aop.api.domain.RefundRoyaltyResult import RefundRoyaltyResult


class AlipayTradeFastpayRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeFastpayRefundQueryResponse, self).__init__()
        self._deposit_back_info = None
        self._enterprise_pay_info = None
        self._error_code = None
        self._gmt_refund_pay = None
        self._industry_sepc_detail = None
        self._out_request_no = None
        self._out_trade_no = None
        self._present_refund_buyer_amount = None
        self._present_refund_discount_amount = None
        self._present_refund_mdiscount_amount = None
        self._refund_amount = None
        self._refund_channel_list = None
        self._refund_channel_status = None
        self._refund_charge_amount = None
        self._refund_detail_item_list = None
        self._refund_reason = None
        self._refund_royaltys = None
        self._refund_settlement_id = None
        self._refund_status = None
        self._send_back_fee = None
        self._total_amount = None
        self._trade_no = None

    @property
    def deposit_back_info(self):
        return self._deposit_back_info

    @deposit_back_info.setter
    def deposit_back_info(self, value):
        if isinstance(value, DepositBackInfo):
            self._deposit_back_info = value
        else:
            self._deposit_back_info = DepositBackInfo.from_alipay_dict(value)
    @property
    def enterprise_pay_info(self):
        return self._enterprise_pay_info

    @enterprise_pay_info.setter
    def enterprise_pay_info(self, value):
        if isinstance(value, EnterprisePayInfo):
            self._enterprise_pay_info = value
        else:
            self._enterprise_pay_info = EnterprisePayInfo.from_alipay_dict(value)
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def gmt_refund_pay(self):
        return self._gmt_refund_pay

    @gmt_refund_pay.setter
    def gmt_refund_pay(self, value):
        self._gmt_refund_pay = value
    @property
    def industry_sepc_detail(self):
        return self._industry_sepc_detail

    @industry_sepc_detail.setter
    def industry_sepc_detail(self, value):
        self._industry_sepc_detail = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def present_refund_buyer_amount(self):
        return self._present_refund_buyer_amount

    @present_refund_buyer_amount.setter
    def present_refund_buyer_amount(self, value):
        self._present_refund_buyer_amount = value
    @property
    def present_refund_discount_amount(self):
        return self._present_refund_discount_amount

    @present_refund_discount_amount.setter
    def present_refund_discount_amount(self, value):
        self._present_refund_discount_amount = value
    @property
    def present_refund_mdiscount_amount(self):
        return self._present_refund_mdiscount_amount

    @present_refund_mdiscount_amount.setter
    def present_refund_mdiscount_amount(self, value):
        self._present_refund_mdiscount_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_channel_list(self):
        return self._refund_channel_list

    @refund_channel_list.setter
    def refund_channel_list(self, value):
        self._refund_channel_list = value
    @property
    def refund_channel_status(self):
        return self._refund_channel_status

    @refund_channel_status.setter
    def refund_channel_status(self, value):
        self._refund_channel_status = value
    @property
    def refund_charge_amount(self):
        return self._refund_charge_amount

    @refund_charge_amount.setter
    def refund_charge_amount(self, value):
        self._refund_charge_amount = value
    @property
    def refund_detail_item_list(self):
        return self._refund_detail_item_list

    @refund_detail_item_list.setter
    def refund_detail_item_list(self, value):
        if isinstance(value, list):
            self._refund_detail_item_list = list()
            for i in value:
                if isinstance(i, TradeFundBill):
                    self._refund_detail_item_list.append(i)
                else:
                    self._refund_detail_item_list.append(TradeFundBill.from_alipay_dict(i))
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_royaltys(self):
        return self._refund_royaltys

    @refund_royaltys.setter
    def refund_royaltys(self, value):
        if isinstance(value, list):
            self._refund_royaltys = list()
            for i in value:
                if isinstance(i, RefundRoyaltyResult):
                    self._refund_royaltys.append(i)
                else:
                    self._refund_royaltys.append(RefundRoyaltyResult.from_alipay_dict(i))
    @property
    def refund_settlement_id(self):
        return self._refund_settlement_id

    @refund_settlement_id.setter
    def refund_settlement_id(self, value):
        self._refund_settlement_id = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def send_back_fee(self):
        return self._send_back_fee

    @send_back_fee.setter
    def send_back_fee(self, value):
        self._send_back_fee = value
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
        response = super(AlipayTradeFastpayRefundQueryResponse, self).parse_response_content(response_content)
        if 'deposit_back_info' in response:
            self.deposit_back_info = response['deposit_back_info']
        if 'enterprise_pay_info' in response:
            self.enterprise_pay_info = response['enterprise_pay_info']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'gmt_refund_pay' in response:
            self.gmt_refund_pay = response['gmt_refund_pay']
        if 'industry_sepc_detail' in response:
            self.industry_sepc_detail = response['industry_sepc_detail']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'present_refund_buyer_amount' in response:
            self.present_refund_buyer_amount = response['present_refund_buyer_amount']
        if 'present_refund_discount_amount' in response:
            self.present_refund_discount_amount = response['present_refund_discount_amount']
        if 'present_refund_mdiscount_amount' in response:
            self.present_refund_mdiscount_amount = response['present_refund_mdiscount_amount']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_channel_list' in response:
            self.refund_channel_list = response['refund_channel_list']
        if 'refund_channel_status' in response:
            self.refund_channel_status = response['refund_channel_status']
        if 'refund_charge_amount' in response:
            self.refund_charge_amount = response['refund_charge_amount']
        if 'refund_detail_item_list' in response:
            self.refund_detail_item_list = response['refund_detail_item_list']
        if 'refund_reason' in response:
            self.refund_reason = response['refund_reason']
        if 'refund_royaltys' in response:
            self.refund_royaltys = response['refund_royaltys']
        if 'refund_settlement_id' in response:
            self.refund_settlement_id = response['refund_settlement_id']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
        if 'send_back_fee' in response:
            self.send_back_fee = response['send_back_fee']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
