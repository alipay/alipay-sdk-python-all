#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbTicketUseDetail import KbTicketUseDetail


class KoubeiTradeTicketTicketcodeUseResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeTicketTicketcodeUseResponse, self).__init__()
        self._biz_code = None
        self._buyer_pay_amount = None
        self._current_price = None
        self._discount_amount = None
        self._invoice_amount = None
        self._item_alias = None
        self._item_id = None
        self._item_name = None
        self._koubei_subsidy_amount = None
        self._order_no = None
        self._original_price = None
        self._receipt_amount = None
        self._request_id = None
        self._ticket_code = None
        self._ticket_trans_id = None
        self._ticket_use_details = None
        self._tm_item_id = None
        self._use_date = None
        self._use_shop_id = None
        self._use_shop_name = None
        self._voucher_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def buyer_pay_amount(self):
        return self._buyer_pay_amount

    @buyer_pay_amount.setter
    def buyer_pay_amount(self, value):
        self._buyer_pay_amount = value
    @property
    def current_price(self):
        return self._current_price

    @current_price.setter
    def current_price(self, value):
        self._current_price = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def item_alias(self):
        return self._item_alias

    @item_alias.setter
    def item_alias(self, value):
        self._item_alias = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def koubei_subsidy_amount(self):
        return self._koubei_subsidy_amount

    @koubei_subsidy_amount.setter
    def koubei_subsidy_amount(self, value):
        self._koubei_subsidy_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def ticket_code(self):
        return self._ticket_code

    @ticket_code.setter
    def ticket_code(self, value):
        self._ticket_code = value
    @property
    def ticket_trans_id(self):
        return self._ticket_trans_id

    @ticket_trans_id.setter
    def ticket_trans_id(self, value):
        self._ticket_trans_id = value
    @property
    def ticket_use_details(self):
        return self._ticket_use_details

    @ticket_use_details.setter
    def ticket_use_details(self, value):
        if isinstance(value, list):
            self._ticket_use_details = list()
            for i in value:
                if isinstance(i, KbTicketUseDetail):
                    self._ticket_use_details.append(i)
                else:
                    self._ticket_use_details.append(KbTicketUseDetail.from_alipay_dict(i))
    @property
    def tm_item_id(self):
        return self._tm_item_id

    @tm_item_id.setter
    def tm_item_id(self, value):
        self._tm_item_id = value
    @property
    def use_date(self):
        return self._use_date

    @use_date.setter
    def use_date(self, value):
        self._use_date = value
    @property
    def use_shop_id(self):
        return self._use_shop_id

    @use_shop_id.setter
    def use_shop_id(self, value):
        self._use_shop_id = value
    @property
    def use_shop_name(self):
        return self._use_shop_name

    @use_shop_name.setter
    def use_shop_name(self, value):
        self._use_shop_name = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeTicketTicketcodeUseResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'buyer_pay_amount' in response:
            self.buyer_pay_amount = response['buyer_pay_amount']
        if 'current_price' in response:
            self.current_price = response['current_price']
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
        if 'invoice_amount' in response:
            self.invoice_amount = response['invoice_amount']
        if 'item_alias' in response:
            self.item_alias = response['item_alias']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'item_name' in response:
            self.item_name = response['item_name']
        if 'koubei_subsidy_amount' in response:
            self.koubei_subsidy_amount = response['koubei_subsidy_amount']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'original_price' in response:
            self.original_price = response['original_price']
        if 'receipt_amount' in response:
            self.receipt_amount = response['receipt_amount']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'ticket_code' in response:
            self.ticket_code = response['ticket_code']
        if 'ticket_trans_id' in response:
            self.ticket_trans_id = response['ticket_trans_id']
        if 'ticket_use_details' in response:
            self.ticket_use_details = response['ticket_use_details']
        if 'tm_item_id' in response:
            self.tm_item_id = response['tm_item_id']
        if 'use_date' in response:
            self.use_date = response['use_date']
        if 'use_shop_id' in response:
            self.use_shop_id = response['use_shop_id']
        if 'use_shop_name' in response:
            self.use_shop_name = response['use_shop_name']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
