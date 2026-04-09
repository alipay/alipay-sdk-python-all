#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TourTicketInfo(object):

    def __init__(self):
        self._ticket_name = None
        self._ticket_price = None
        self._ticket_target_audience = None

    @property
    def ticket_name(self):
        return self._ticket_name

    @ticket_name.setter
    def ticket_name(self, value):
        self._ticket_name = value
    @property
    def ticket_price(self):
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        self._ticket_price = value
    @property
    def ticket_target_audience(self):
        return self._ticket_target_audience

    @ticket_target_audience.setter
    def ticket_target_audience(self, value):
        self._ticket_target_audience = value


    def to_alipay_dict(self):
        params = dict()
        if self.ticket_name:
            if hasattr(self.ticket_name, 'to_alipay_dict'):
                params['ticket_name'] = self.ticket_name.to_alipay_dict()
            else:
                params['ticket_name'] = self.ticket_name
        if self.ticket_price:
            if hasattr(self.ticket_price, 'to_alipay_dict'):
                params['ticket_price'] = self.ticket_price.to_alipay_dict()
            else:
                params['ticket_price'] = self.ticket_price
        if self.ticket_target_audience:
            if hasattr(self.ticket_target_audience, 'to_alipay_dict'):
                params['ticket_target_audience'] = self.ticket_target_audience.to_alipay_dict()
            else:
                params['ticket_target_audience'] = self.ticket_target_audience
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TourTicketInfo()
        if 'ticket_name' in d:
            o.ticket_name = d['ticket_name']
        if 'ticket_price' in d:
            o.ticket_price = d['ticket_price']
        if 'ticket_target_audience' in d:
            o.ticket_target_audience = d['ticket_target_audience']
        return o


