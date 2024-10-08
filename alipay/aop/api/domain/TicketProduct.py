#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupTicketSKU import GroupTicketSKU
from alipay.aop.api.domain.TicketSKU import TicketSKU


class TicketProduct(object):

    def __init__(self):
        self._group = None
        self._group_ticket_products = None
        self._ticket_products = None
        self._ticket_type = None

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value
    @property
    def group_ticket_products(self):
        return self._group_ticket_products

    @group_ticket_products.setter
    def group_ticket_products(self, value):
        if isinstance(value, list):
            self._group_ticket_products = list()
            for i in value:
                if isinstance(i, GroupTicketSKU):
                    self._group_ticket_products.append(i)
                else:
                    self._group_ticket_products.append(GroupTicketSKU.from_alipay_dict(i))
    @property
    def ticket_products(self):
        return self._ticket_products

    @ticket_products.setter
    def ticket_products(self, value):
        if isinstance(value, list):
            self._ticket_products = list()
            for i in value:
                if isinstance(i, TicketSKU):
                    self._ticket_products.append(i)
                else:
                    self._ticket_products.append(TicketSKU.from_alipay_dict(i))
    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        self._ticket_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.group:
            if hasattr(self.group, 'to_alipay_dict'):
                params['group'] = self.group.to_alipay_dict()
            else:
                params['group'] = self.group
        if self.group_ticket_products:
            if isinstance(self.group_ticket_products, list):
                for i in range(0, len(self.group_ticket_products)):
                    element = self.group_ticket_products[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_ticket_products[i] = element.to_alipay_dict()
            if hasattr(self.group_ticket_products, 'to_alipay_dict'):
                params['group_ticket_products'] = self.group_ticket_products.to_alipay_dict()
            else:
                params['group_ticket_products'] = self.group_ticket_products
        if self.ticket_products:
            if isinstance(self.ticket_products, list):
                for i in range(0, len(self.ticket_products)):
                    element = self.ticket_products[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ticket_products[i] = element.to_alipay_dict()
            if hasattr(self.ticket_products, 'to_alipay_dict'):
                params['ticket_products'] = self.ticket_products.to_alipay_dict()
            else:
                params['ticket_products'] = self.ticket_products
        if self.ticket_type:
            if hasattr(self.ticket_type, 'to_alipay_dict'):
                params['ticket_type'] = self.ticket_type.to_alipay_dict()
            else:
                params['ticket_type'] = self.ticket_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TicketProduct()
        if 'group' in d:
            o.group = d['group']
        if 'group_ticket_products' in d:
            o.group_ticket_products = d['group_ticket_products']
        if 'ticket_products' in d:
            o.ticket_products = d['ticket_products']
        if 'ticket_type' in d:
            o.ticket_type = d['ticket_type']
        return o


