#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCityfacilitatorVoucherConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorVoucherConfirmResponse, self).__init__()
        self._amount = None
        self._end_station = None
        self._end_station_name = None
        self._quantity = None
        self._start_station = None
        self._start_station_name = None
        self._status = None
        self._ticket_price = None
        self._ticket_type = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def end_station(self):
        return self._end_station

    @end_station.setter
    def end_station(self, value):
        self._end_station = value
    @property
    def end_station_name(self):
        return self._end_station_name

    @end_station_name.setter
    def end_station_name(self, value):
        self._end_station_name = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def start_station(self):
        return self._start_station

    @start_station.setter
    def start_station(self, value):
        self._start_station = value
    @property
    def start_station_name(self):
        return self._start_station_name

    @start_station_name.setter
    def start_station_name(self, value):
        self._start_station_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def ticket_price(self):
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        self._ticket_price = value
    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        self._ticket_type = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorVoucherConfirmResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'end_station' in response:
            self.end_station = response['end_station']
        if 'end_station_name' in response:
            self.end_station_name = response['end_station_name']
        if 'quantity' in response:
            self.quantity = response['quantity']
        if 'start_station' in response:
            self.start_station = response['start_station']
        if 'start_station_name' in response:
            self.start_station_name = response['start_station_name']
        if 'status' in response:
            self.status = response['status']
        if 'ticket_price' in response:
            self.ticket_price = response['ticket_price']
        if 'ticket_type' in response:
            self.ticket_type = response['ticket_type']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
