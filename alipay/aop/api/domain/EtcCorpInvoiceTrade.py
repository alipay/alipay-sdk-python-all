#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EtcInoviceTradeList import EtcInoviceTradeList


class EtcCorpInvoiceTrade(object):

    def __init__(self):
        self._apply_id = None
        self._apply_status = None
        self._card_id = None
        self._end_address = None
        self._end_time = None
        self._highway_fee = None
        self._invoice_status = None
        self._plate_color = None
        self._plate_no = None
        self._start_address = None
        self._start_time = None
        self._trade_list = None
        self._waybill_fee = None
        self._waybill_no = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def end_address(self):
        return self._end_address

    @end_address.setter
    def end_address(self, value):
        self._end_address = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def highway_fee(self):
        return self._highway_fee

    @highway_fee.setter
    def highway_fee(self, value):
        self._highway_fee = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def start_address(self):
        return self._start_address

    @start_address.setter
    def start_address(self, value):
        self._start_address = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def trade_list(self):
        return self._trade_list

    @trade_list.setter
    def trade_list(self, value):
        if isinstance(value, list):
            self._trade_list = list()
            for i in value:
                if isinstance(i, EtcInoviceTradeList):
                    self._trade_list.append(i)
                else:
                    self._trade_list.append(EtcInoviceTradeList.from_alipay_dict(i))
    @property
    def waybill_fee(self):
        return self._waybill_fee

    @waybill_fee.setter
    def waybill_fee(self, value):
        self._waybill_fee = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.end_address:
            if hasattr(self.end_address, 'to_alipay_dict'):
                params['end_address'] = self.end_address.to_alipay_dict()
            else:
                params['end_address'] = self.end_address
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.highway_fee:
            if hasattr(self.highway_fee, 'to_alipay_dict'):
                params['highway_fee'] = self.highway_fee.to_alipay_dict()
            else:
                params['highway_fee'] = self.highway_fee
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.start_address:
            if hasattr(self.start_address, 'to_alipay_dict'):
                params['start_address'] = self.start_address.to_alipay_dict()
            else:
                params['start_address'] = self.start_address
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.trade_list:
            if isinstance(self.trade_list, list):
                for i in range(0, len(self.trade_list)):
                    element = self.trade_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_list, 'to_alipay_dict'):
                params['trade_list'] = self.trade_list.to_alipay_dict()
            else:
                params['trade_list'] = self.trade_list
        if self.waybill_fee:
            if hasattr(self.waybill_fee, 'to_alipay_dict'):
                params['waybill_fee'] = self.waybill_fee.to_alipay_dict()
            else:
                params['waybill_fee'] = self.waybill_fee
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcCorpInvoiceTrade()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'end_address' in d:
            o.end_address = d['end_address']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'highway_fee' in d:
            o.highway_fee = d['highway_fee']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'start_address' in d:
            o.start_address = d['start_address']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'trade_list' in d:
            o.trade_list = d['trade_list']
        if 'waybill_fee' in d:
            o.waybill_fee = d['waybill_fee']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


