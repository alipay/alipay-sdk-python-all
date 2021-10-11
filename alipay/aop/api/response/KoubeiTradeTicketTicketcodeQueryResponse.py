#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TicketTransInfo import TicketTransInfo


class KoubeiTradeTicketTicketcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeTicketTicketcodeQueryResponse, self).__init__()
        self._available_quantity = None
        self._current_price = None
        self._effect_date = None
        self._expire_date = None
        self._item_alias = None
        self._item_id = None
        self._item_name = None
        self._order_no = None
        self._original_price = None
        self._ticket_code = None
        self._ticket_status = None
        self._ticket_status_desc = None
        self._ticket_trans_info_list = None
        self._time_cards = None
        self._tm_item_id = None
        self._total_quantity = None
        self._voucher_id = None

    @property
    def available_quantity(self):
        return self._available_quantity

    @available_quantity.setter
    def available_quantity(self, value):
        self._available_quantity = value
    @property
    def current_price(self):
        return self._current_price

    @current_price.setter
    def current_price(self, value):
        self._current_price = value
    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
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
    def ticket_code(self):
        return self._ticket_code

    @ticket_code.setter
    def ticket_code(self, value):
        self._ticket_code = value
    @property
    def ticket_status(self):
        return self._ticket_status

    @ticket_status.setter
    def ticket_status(self, value):
        self._ticket_status = value
    @property
    def ticket_status_desc(self):
        return self._ticket_status_desc

    @ticket_status_desc.setter
    def ticket_status_desc(self, value):
        self._ticket_status_desc = value
    @property
    def ticket_trans_info_list(self):
        return self._ticket_trans_info_list

    @ticket_trans_info_list.setter
    def ticket_trans_info_list(self, value):
        if isinstance(value, list):
            self._ticket_trans_info_list = list()
            for i in value:
                if isinstance(i, TicketTransInfo):
                    self._ticket_trans_info_list.append(i)
                else:
                    self._ticket_trans_info_list.append(TicketTransInfo.from_alipay_dict(i))
    @property
    def time_cards(self):
        return self._time_cards

    @time_cards.setter
    def time_cards(self, value):
        self._time_cards = value
    @property
    def tm_item_id(self):
        return self._tm_item_id

    @tm_item_id.setter
    def tm_item_id(self, value):
        self._tm_item_id = value
    @property
    def total_quantity(self):
        return self._total_quantity

    @total_quantity.setter
    def total_quantity(self, value):
        self._total_quantity = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeTicketTicketcodeQueryResponse, self).parse_response_content(response_content)
        if 'available_quantity' in response:
            self.available_quantity = response['available_quantity']
        if 'current_price' in response:
            self.current_price = response['current_price']
        if 'effect_date' in response:
            self.effect_date = response['effect_date']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'item_alias' in response:
            self.item_alias = response['item_alias']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'item_name' in response:
            self.item_name = response['item_name']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'original_price' in response:
            self.original_price = response['original_price']
        if 'ticket_code' in response:
            self.ticket_code = response['ticket_code']
        if 'ticket_status' in response:
            self.ticket_status = response['ticket_status']
        if 'ticket_status_desc' in response:
            self.ticket_status_desc = response['ticket_status_desc']
        if 'ticket_trans_info_list' in response:
            self.ticket_trans_info_list = response['ticket_trans_info_list']
        if 'time_cards' in response:
            self.time_cards = response['time_cards']
        if 'tm_item_id' in response:
            self.tm_item_id = response['tm_item_id']
        if 'total_quantity' in response:
            self.total_quantity = response['total_quantity']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
