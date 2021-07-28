#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TicketTransInfo(object):

    def __init__(self):
        self._create_time = None
        self._last_modify_time = None
        self._quantity = None
        self._ticket_trans_id = None
        self._ticket_trans_type = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def last_modify_time(self):
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, value):
        self._last_modify_time = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def ticket_trans_id(self):
        return self._ticket_trans_id

    @ticket_trans_id.setter
    def ticket_trans_id(self, value):
        self._ticket_trans_id = value
    @property
    def ticket_trans_type(self):
        return self._ticket_trans_type

    @ticket_trans_type.setter
    def ticket_trans_type(self, value):
        self._ticket_trans_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.last_modify_time:
            if hasattr(self.last_modify_time, 'to_alipay_dict'):
                params['last_modify_time'] = self.last_modify_time.to_alipay_dict()
            else:
                params['last_modify_time'] = self.last_modify_time
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.ticket_trans_id:
            if hasattr(self.ticket_trans_id, 'to_alipay_dict'):
                params['ticket_trans_id'] = self.ticket_trans_id.to_alipay_dict()
            else:
                params['ticket_trans_id'] = self.ticket_trans_id
        if self.ticket_trans_type:
            if hasattr(self.ticket_trans_type, 'to_alipay_dict'):
                params['ticket_trans_type'] = self.ticket_trans_type.to_alipay_dict()
            else:
                params['ticket_trans_type'] = self.ticket_trans_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TicketTransInfo()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'last_modify_time' in d:
            o.last_modify_time = d['last_modify_time']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'ticket_trans_id' in d:
            o.ticket_trans_id = d['ticket_trans_id']
        if 'ticket_trans_type' in d:
            o.ticket_trans_type = d['ticket_trans_type']
        return o


