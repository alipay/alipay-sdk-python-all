#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarbonCopies(object):

    def __init__(self):
        self._email = None
        self._name = None
        self._recipient_id = None
        self._routing_order = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def recipient_id(self):
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, value):
        self._recipient_id = value
    @property
    def routing_order(self):
        return self._routing_order

    @routing_order.setter
    def routing_order(self, value):
        self._routing_order = value


    def to_alipay_dict(self):
        params = dict()
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.recipient_id:
            if hasattr(self.recipient_id, 'to_alipay_dict'):
                params['recipient_id'] = self.recipient_id.to_alipay_dict()
            else:
                params['recipient_id'] = self.recipient_id
        if self.routing_order:
            if hasattr(self.routing_order, 'to_alipay_dict'):
                params['routing_order'] = self.routing_order.to_alipay_dict()
            else:
                params['routing_order'] = self.routing_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarbonCopies()
        if 'email' in d:
            o.email = d['email']
        if 'name' in d:
            o.name = d['name']
        if 'recipient_id' in d:
            o.recipient_id = d['recipient_id']
        if 'routing_order' in d:
            o.routing_order = d['routing_order']
        return o


