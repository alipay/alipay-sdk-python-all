#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LeaseIndustryBean(object):

    def __init__(self):
        self._available_city_list = None
        self._deposit_amount = None
        self._fresh_degree = None
        self._rental_date = None
        self._rental_free = None
        self._shipment_rate = None
        self._shipments = None

    @property
    def available_city_list(self):
        return self._available_city_list

    @available_city_list.setter
    def available_city_list(self, value):
        if isinstance(value, list):
            self._available_city_list = list()
            for i in value:
                self._available_city_list.append(i)
    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def fresh_degree(self):
        return self._fresh_degree

    @fresh_degree.setter
    def fresh_degree(self, value):
        self._fresh_degree = value
    @property
    def rental_date(self):
        return self._rental_date

    @rental_date.setter
    def rental_date(self, value):
        self._rental_date = value
    @property
    def rental_free(self):
        return self._rental_free

    @rental_free.setter
    def rental_free(self, value):
        self._rental_free = value
    @property
    def shipment_rate(self):
        return self._shipment_rate

    @shipment_rate.setter
    def shipment_rate(self, value):
        self._shipment_rate = value
    @property
    def shipments(self):
        return self._shipments

    @shipments.setter
    def shipments(self, value):
        self._shipments = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_city_list:
            if isinstance(self.available_city_list, list):
                for i in range(0, len(self.available_city_list)):
                    element = self.available_city_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_city_list[i] = element.to_alipay_dict()
            if hasattr(self.available_city_list, 'to_alipay_dict'):
                params['available_city_list'] = self.available_city_list.to_alipay_dict()
            else:
                params['available_city_list'] = self.available_city_list
        if self.deposit_amount:
            if hasattr(self.deposit_amount, 'to_alipay_dict'):
                params['deposit_amount'] = self.deposit_amount.to_alipay_dict()
            else:
                params['deposit_amount'] = self.deposit_amount
        if self.fresh_degree:
            if hasattr(self.fresh_degree, 'to_alipay_dict'):
                params['fresh_degree'] = self.fresh_degree.to_alipay_dict()
            else:
                params['fresh_degree'] = self.fresh_degree
        if self.rental_date:
            if hasattr(self.rental_date, 'to_alipay_dict'):
                params['rental_date'] = self.rental_date.to_alipay_dict()
            else:
                params['rental_date'] = self.rental_date
        if self.rental_free:
            if hasattr(self.rental_free, 'to_alipay_dict'):
                params['rental_free'] = self.rental_free.to_alipay_dict()
            else:
                params['rental_free'] = self.rental_free
        if self.shipment_rate:
            if hasattr(self.shipment_rate, 'to_alipay_dict'):
                params['shipment_rate'] = self.shipment_rate.to_alipay_dict()
            else:
                params['shipment_rate'] = self.shipment_rate
        if self.shipments:
            if hasattr(self.shipments, 'to_alipay_dict'):
                params['shipments'] = self.shipments.to_alipay_dict()
            else:
                params['shipments'] = self.shipments
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LeaseIndustryBean()
        if 'available_city_list' in d:
            o.available_city_list = d['available_city_list']
        if 'deposit_amount' in d:
            o.deposit_amount = d['deposit_amount']
        if 'fresh_degree' in d:
            o.fresh_degree = d['fresh_degree']
        if 'rental_date' in d:
            o.rental_date = d['rental_date']
        if 'rental_free' in d:
            o.rental_free = d['rental_free']
        if 'shipment_rate' in d:
            o.shipment_rate = d['shipment_rate']
        if 'shipments' in d:
            o.shipments = d['shipments']
        return o


