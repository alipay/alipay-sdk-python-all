#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TicketInfo(object):

    def __init__(self):
        self._address = None
        self._end_time = None
        self._resv_type = None
        self._shop = None
        self._ticket_no = None
        self._time = None
        self._type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def resv_type(self):
        return self._resv_type

    @resv_type.setter
    def resv_type(self, value):
        self._resv_type = value
    @property
    def shop(self):
        return self._shop

    @shop.setter
    def shop(self, value):
        self._shop = value
    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, value):
        self._ticket_no = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.resv_type:
            if hasattr(self.resv_type, 'to_alipay_dict'):
                params['resv_type'] = self.resv_type.to_alipay_dict()
            else:
                params['resv_type'] = self.resv_type
        if self.shop:
            if hasattr(self.shop, 'to_alipay_dict'):
                params['shop'] = self.shop.to_alipay_dict()
            else:
                params['shop'] = self.shop
        if self.ticket_no:
            if hasattr(self.ticket_no, 'to_alipay_dict'):
                params['ticket_no'] = self.ticket_no.to_alipay_dict()
            else:
                params['ticket_no'] = self.ticket_no
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TicketInfo()
        if 'address' in d:
            o.address = d['address']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'resv_type' in d:
            o.resv_type = d['resv_type']
        if 'shop' in d:
            o.shop = d['shop']
        if 'ticket_no' in d:
            o.ticket_no = d['ticket_no']
        if 'time' in d:
            o.time = d['time']
        if 'type' in d:
            o.type = d['type']
        return o


