#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TradeFundBill import TradeFundBill
from alipay.aop.api.domain.TradeSettleInfo import TradeSettleInfo
from alipay.aop.api.domain.VoucherDetail import VoucherDetail


class AlipayTradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeQueryResponse, self).__init__()
        self._alipay_store_id = None
        self._alipay_sub_merchant_id = None
        self._auth_trade_pay_mode = None
        self._body = None
        self._buyer_logon_id = None
        self._buyer_pay_amount = None
        self._buyer_user_id = None
        self._buyer_user_name = None
        self._buyer_user_type = None
        self._charge_amount = None
        self._charge_flags = None
        self._discount_amount = None
        self._discount_goods_detail = None
        self._ext_infos = None
        self._fund_bill_list = None
        self._industry_sepc_detail = None
        self._invoice_amount = None
        self._mdiscount_amount = None
        self._open_id = None
        self._out_trade_no = None
        self._pay_amount = None
        self._pay_currency = None
        self._point_amount = None
        self._receipt_amount = None
        self._send_pay_date = None
        self._settle_amount = None
        self._settle_currency = None
        self._settle_trans_rate = None
        self._settlement_id = None
        self._store_id = None
        self._store_name = None
        self._subject = None
        self._terminal_id = None
        self._total_amount = None
        self._trade_no = None
        self._trade_settle_info = None
        self._trade_status = None
        self._trans_currency = None
        self._trans_pay_rate = None
        self._voucher_detail_list = None

    @property
    def alipay_store_id(self):
        return self._alipay_store_id

    @alipay_store_id.setter
    def alipay_store_id(self, value):
        self._alipay_store_id = value
    @property
    def alipay_sub_merchant_id(self):
        return self._alipay_sub_merchant_id

    @alipay_sub_merchant_id.setter
    def alipay_sub_merchant_id(self, value):
        self._alipay_sub_merchant_id = value
    @property
    def auth_trade_pay_mode(self):
        return self._auth_trade_pay_mode

    @auth_trade_pay_mode.setter
    def auth_trade_pay_mode(self, value):
        self._auth_trade_pay_mode = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
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
    def buyer_user_name(self):
        return self._buyer_user_name

    @buyer_user_name.setter
    def buyer_user_name(self, value):
        self._buyer_user_name = value
    @property
    def buyer_user_type(self):
        return self._buyer_user_type

    @buyer_user_type.setter
    def buyer_user_type(self, value):
        self._buyer_user_type = value
    @property
    def charge_amount(self):
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, value):
        self._charge_amount = value
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
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def fund_bill_list(self):
        return self._fund_bill_list

    @fund_bill_list.setter
    def fund_bill_list(self, value):
        if isinstance(value, list):
            self._fund_bill_list = list()
            for i in value:
                if isinstance(i, TradeFundBill):
                    self._fund_bill_list.append(i)
                else:
                    self._fund_bill_list.append(TradeFundBill.from_alipay_dict(i))
    @property
    def industry_sepc_detail(self):
        return self._industry_sepc_detail

    @industry_sepc_detail.setter
    def industry_sepc_detail(self, value):
        self._industry_sepc_detail = value
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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def pay_currency(self):
        return self._pay_currency

    @pay_currency.setter
    def pay_currency(self, value):
        self._pay_currency = value
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
    def send_pay_date(self):
        return self._send_pay_date

    @send_pay_date.setter
    def send_pay_date(self, value):
        self._send_pay_date = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def settle_currency(self):
        return self._settle_currency

    @settle_currency.setter
    def settle_currency(self, value):
        self._settle_currency = value
    @property
    def settle_trans_rate(self):
        return self._settle_trans_rate

    @settle_trans_rate.setter
    def settle_trans_rate(self, value):
        self._settle_trans_rate = value
    @property
    def settlement_id(self):
        return self._settlement_id

    @settlement_id.setter
    def settlement_id(self, value):
        self._settlement_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value
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
    def trade_settle_info(self):
        return self._trade_settle_info

    @trade_settle_info.setter
    def trade_settle_info(self, value):
        if isinstance(value, TradeSettleInfo):
            self._trade_settle_info = value
        else:
            self._trade_settle_info = TradeSettleInfo.from_alipay_dict(value)
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value
    @property
    def trans_pay_rate(self):
        return self._trans_pay_rate

    @trans_pay_rate.setter
    def trans_pay_rate(self, value):
        self._trans_pay_rate = value
    @property
    def voucher_detail_list(self):
        return self._voucher_detail_list

    @voucher_detail_list.setter
    def voucher_detail_list(self, value):
        if isinstance(value, list):
            self._voucher_detail_list = list()
            for i in value:
                if isinstance(i, VoucherDetail):
                    self._voucher_detail_list.append(i)
                else:
                    self._voucher_detail_list.append(VoucherDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeQueryResponse, self).parse_response_content(response_content)
        if 'alipay_store_id' in response:
            self.alipay_store_id = response['alipay_store_id']
        if 'alipay_sub_merchant_id' in response:
            self.alipay_sub_merchant_id = response['alipay_sub_merchant_id']
        if 'auth_trade_pay_mode' in response:
            self.auth_trade_pay_mode = response['auth_trade_pay_mode']
        if 'body' in response:
            self.body = response['body']
        if 'buyer_logon_id' in response:
            self.buyer_logon_id = response['buyer_logon_id']
        if 'buyer_pay_amount' in response:
            self.buyer_pay_amount = response['buyer_pay_amount']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'buyer_user_name' in response:
            self.buyer_user_name = response['buyer_user_name']
        if 'buyer_user_type' in response:
            self.buyer_user_type = response['buyer_user_type']
        if 'charge_amount' in response:
            self.charge_amount = response['charge_amount']
        if 'charge_flags' in response:
            self.charge_flags = response['charge_flags']
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
        if 'discount_goods_detail' in response:
            self.discount_goods_detail = response['discount_goods_detail']
        if 'ext_infos' in response:
            self.ext_infos = response['ext_infos']
        if 'fund_bill_list' in response:
            self.fund_bill_list = response['fund_bill_list']
        if 'industry_sepc_detail' in response:
            self.industry_sepc_detail = response['industry_sepc_detail']
        if 'invoice_amount' in response:
            self.invoice_amount = response['invoice_amount']
        if 'mdiscount_amount' in response:
            self.mdiscount_amount = response['mdiscount_amount']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pay_currency' in response:
            self.pay_currency = response['pay_currency']
        if 'point_amount' in response:
            self.point_amount = response['point_amount']
        if 'receipt_amount' in response:
            self.receipt_amount = response['receipt_amount']
        if 'send_pay_date' in response:
            self.send_pay_date = response['send_pay_date']
        if 'settle_amount' in response:
            self.settle_amount = response['settle_amount']
        if 'settle_currency' in response:
            self.settle_currency = response['settle_currency']
        if 'settle_trans_rate' in response:
            self.settle_trans_rate = response['settle_trans_rate']
        if 'settlement_id' in response:
            self.settlement_id = response['settlement_id']
        if 'store_id' in response:
            self.store_id = response['store_id']
        if 'store_name' in response:
            self.store_name = response['store_name']
        if 'subject' in response:
            self.subject = response['subject']
        if 'terminal_id' in response:
            self.terminal_id = response['terminal_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_settle_info' in response:
            self.trade_settle_info = response['trade_settle_info']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
        if 'trans_currency' in response:
            self.trans_currency = response['trans_currency']
        if 'trans_pay_rate' in response:
            self.trans_pay_rate = response['trans_pay_rate']
        if 'voucher_detail_list' in response:
            self.voucher_detail_list = response['voucher_detail_list']
