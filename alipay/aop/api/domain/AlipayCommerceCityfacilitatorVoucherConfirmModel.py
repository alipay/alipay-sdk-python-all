#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorVoucherConfirmModel(object):

    def __init__(self):
        self._amount = None
        self._biz_info_ext = None
        self._biz_request_id = None
        self._city_code = None
        self._end_station = None
        self._exchange_ids = None
        self._operate_time = None
        self._out_biz_no = None
        self._quantity = None
        self._seller_id = None
        self._start_station = None
        self._ticket_no = None
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
    def biz_info_ext(self):
        return self._biz_info_ext

    @biz_info_ext.setter
    def biz_info_ext(self, value):
        self._biz_info_ext = value
    @property
    def biz_request_id(self):
        return self._biz_request_id

    @biz_request_id.setter
    def biz_request_id(self, value):
        self._biz_request_id = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def end_station(self):
        return self._end_station

    @end_station.setter
    def end_station(self, value):
        self._end_station = value
    @property
    def exchange_ids(self):
        return self._exchange_ids

    @exchange_ids.setter
    def exchange_ids(self, value):
        self._exchange_ids = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def start_station(self):
        return self._start_station

    @start_station.setter
    def start_station(self, value):
        self._start_station = value
    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, value):
        self._ticket_no = value
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
        if self.biz_info_ext:
            if hasattr(self.biz_info_ext, 'to_alipay_dict'):
                params['biz_info_ext'] = self.biz_info_ext.to_alipay_dict()
            else:
                params['biz_info_ext'] = self.biz_info_ext
        if self.biz_request_id:
            if hasattr(self.biz_request_id, 'to_alipay_dict'):
                params['biz_request_id'] = self.biz_request_id.to_alipay_dict()
            else:
                params['biz_request_id'] = self.biz_request_id
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.end_station:
            if hasattr(self.end_station, 'to_alipay_dict'):
                params['end_station'] = self.end_station.to_alipay_dict()
            else:
                params['end_station'] = self.end_station
        if self.exchange_ids:
            if hasattr(self.exchange_ids, 'to_alipay_dict'):
                params['exchange_ids'] = self.exchange_ids.to_alipay_dict()
            else:
                params['exchange_ids'] = self.exchange_ids
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.start_station:
            if hasattr(self.start_station, 'to_alipay_dict'):
                params['start_station'] = self.start_station.to_alipay_dict()
            else:
                params['start_station'] = self.start_station
        if self.ticket_no:
            if hasattr(self.ticket_no, 'to_alipay_dict'):
                params['ticket_no'] = self.ticket_no.to_alipay_dict()
            else:
                params['ticket_no'] = self.ticket_no
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
        o = AlipayCommerceCityfacilitatorVoucherConfirmModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_info_ext' in d:
            o.biz_info_ext = d['biz_info_ext']
        if 'biz_request_id' in d:
            o.biz_request_id = d['biz_request_id']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'end_station' in d:
            o.end_station = d['end_station']
        if 'exchange_ids' in d:
            o.exchange_ids = d['exchange_ids']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'start_station' in d:
            o.start_station = d['start_station']
        if 'ticket_no' in d:
            o.ticket_no = d['ticket_no']
        if 'ticket_price' in d:
            o.ticket_price = d['ticket_price']
        if 'ticket_type' in d:
            o.ticket_type = d['ticket_type']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


