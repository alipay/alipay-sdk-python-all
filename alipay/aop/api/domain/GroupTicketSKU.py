#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TicketSKU import TicketSKU


class GroupTicketSKU(object):

    def __init__(self):
        self._category_name = None
        self._ticket_products = None

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupTicketSKU()
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'ticket_products' in d:
            o.ticket_products = d['ticket_products']
        return o


