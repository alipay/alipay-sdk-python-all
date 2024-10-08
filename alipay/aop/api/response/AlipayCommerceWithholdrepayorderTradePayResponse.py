#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndustryTradeFundBill import IndustryTradeFundBill
from alipay.aop.api.domain.IndustryVoucherDetail import IndustryVoucherDetail


class AlipayCommerceWithholdrepayorderTradePayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWithholdrepayorderTradePayResponse, self).__init__()
        self._advance_amount = None
        self._async_payment_mode = None
        self._buyer_logon_id = None
        self._buyer_open_id = None
        self._buyer_pay_amount = None
        self._buyer_user_id = None
        self._charge_flags = None
        self._discount_amount = None
        self._discount_goods_detail = None
        self._fund_bill_list = None
        self._gmt_payment = None
        self._invoice_amount = None
        self._mdiscount_amount = None
        self._out_trade_no = None
        self._point_amount = None
        self._receipt_amount = None
        self._store_name = None
        self._total_amount = None
        self._trade_no = None
        self._voucher_detail_list = None

    @property
    def advance_amount(self):
        return self._advance_amount

    @advance_amount.setter
    def advance_amount(self, value):
        self._advance_amount = value
    @property
    def async_payment_mode(self):
        return self._async_payment_mode

    @async_payment_mode.setter
    def async_payment_mode(self, value):
        self._async_payment_mode = value
    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def buyer_pay_amount(self):
        return self._buyer_pay_amount

    @buyer_pay_amount.setter
    def buyer_pay_amount(self, value):
        self._buyer_pay_amount = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def charge_flags(self):
        return self._charge_flags

    @charge_flags.setter
    def charge_flags(self, value):
        self._charge_flags = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_goods_detail(self):
        return self._discount_goods_detail

    @discount_goods_detail.setter
    def discount_goods_detail(self, value):
        self._discount_goods_detail = value
    @property
    def fund_bill_list(self):
        return self._fund_bill_list

    @fund_bill_list.setter
    def fund_bill_list(self, value):
        if isinstance(value, list):
            self._fund_bill_list = list()
            for i in value:
                if isinstance(i, IndustryTradeFundBill):
                    self._fund_bill_list.append(i)
                else:
                    self._fund_bill_list.append(IndustryTradeFundBill.from_alipay_dict(i))
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def mdiscount_amount(self):
        return self._mdiscount_amount

    @mdiscount_amount.setter
    def mdiscount_amount(self, value):
        self._mdiscount_amount = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def point_amount(self):
        return self._point_amount

    @point_amount.setter
    def point_amount(self, value):
        self._point_amount = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
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
    @property
    def voucher_detail_list(self):
        return self._voucher_detail_list

    @voucher_detail_list.setter
    def voucher_detail_list(self, value):
        if isinstance(value, list):
            self._voucher_detail_list = list()
            for i in value:
                if isinstance(i, IndustryVoucherDetail):
                    self._voucher_detail_list.append(i)
                else:
                    self._voucher_detail_list.append(IndustryVoucherDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWithholdrepayorderTradePayResponse, self).parse_response_content(response_content)
        if 'advance_amount' in response:
            self.advance_amount = response['advance_amount']
        if 'async_payment_mode' in response:
            self.async_payment_mode = response['async_payment_mode']
        if 'buyer_logon_id' in response:
            self.buyer_logon_id = response['buyer_logon_id']
        if 'buyer_open_id' in response:
            self.buyer_open_id = response['buyer_open_id']
        if 'buyer_pay_amount' in response:
            self.buyer_pay_amount = response['buyer_pay_amount']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'charge_flags' in response:
            self.charge_flags = response['charge_flags']
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
        if 'discount_goods_detail' in response:
            self.discount_goods_detail = response['discount_goods_detail']
        if 'fund_bill_list' in response:
            self.fund_bill_list = response['fund_bill_list']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'invoice_amount' in response:
            self.invoice_amount = response['invoice_amount']
        if 'mdiscount_amount' in response:
            self.mdiscount_amount = response['mdiscount_amount']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'point_amount' in response:
            self.point_amount = response['point_amount']
        if 'receipt_amount' in response:
            self.receipt_amount = response['receipt_amount']
        if 'store_name' in response:
            self.store_name = response['store_name']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'voucher_detail_list' in response:
            self.voucher_detail_list = response['voucher_detail_list']
