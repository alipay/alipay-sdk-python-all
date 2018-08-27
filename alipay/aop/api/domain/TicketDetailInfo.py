#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TicketDetailInfo(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.end_station:
            if hasattr(self.end_station, 'to_alipay_dict'):
                params['end_station'] = self.end_station.to_alipay_dict()
            else:
                params['end_station'] = self.end_station
        if self.end_station_name:
            if hasattr(self.end_station_name, 'to_alipay_dict'):
                params['end_station_name'] = self.end_station_name.to_alipay_dict()
            else:
                params['end_station_name'] = self.end_station_name
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.start_station:
            if hasattr(self.start_station, 'to_alipay_dict'):
                params['start_station'] = self.start_station.to_alipay_dict()
            else:
                params['start_station'] = self.start_station
        if self.start_station_name:
            if hasattr(self.start_station_name, 'to_alipay_dict'):
                params['start_station_name'] = self.start_station_name.to_alipay_dict()
            else:
                params['start_station_name'] = self.start_station_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.ticket_price:
            if hasattr(self.ticket_price, 'to_alipay_dict'):
                params['ticket_price'] = self.ticket_price.to_alipay_dict()
            else:
                params['ticket_price'] = self.ticket_price
        if self.ticket_type:
            if hasattr(self.ticket_type, 'to_alipay_dict'):
                params['ticket_type'] = self.ticket_type.to_alipay_dict()
            else:
                params['ticket_type'] = self.ticket_type
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TicketDetailInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'end_station' in d:
            o.end_station = d['end_station']
        if 'end_station_name' in d:
            o.end_station_name = d['end_station_name']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'start_station' in d:
            o.start_station = d['start_station']
        if 'start_station_name' in d:
            o.start_station_name = d['start_station_name']
        if 'status' in d:
            o.status = d['status']
        if 'ticket_price' in d:
            o.ticket_price = d['ticket_price']
        if 'ticket_type' in d:
            o.ticket_type = d['ticket_type']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


