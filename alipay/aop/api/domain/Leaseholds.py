#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Leaseholds(object):

    def __init__(self):
        self._daily_rent_price = None
        self._device_model_no = None
        self._expected_lease_quantity = None
        self._lease_asset_ids = None
        self._month_rent_price = None

    @property
    def daily_rent_price(self):
        return self._daily_rent_price

    @daily_rent_price.setter
    def daily_rent_price(self, value):
        self._daily_rent_price = value
    @property
    def device_model_no(self):
        return self._device_model_no

    @device_model_no.setter
    def device_model_no(self, value):
        self._device_model_no = value
    @property
    def expected_lease_quantity(self):
        return self._expected_lease_quantity

    @expected_lease_quantity.setter
    def expected_lease_quantity(self, value):
        self._expected_lease_quantity = value
    @property
    def lease_asset_ids(self):
        return self._lease_asset_ids

    @lease_asset_ids.setter
    def lease_asset_ids(self, value):
        if isinstance(value, list):
            self._lease_asset_ids = list()
            for i in value:
                self._lease_asset_ids.append(i)
    @property
    def month_rent_price(self):
        return self._month_rent_price

    @month_rent_price.setter
    def month_rent_price(self, value):
        self._month_rent_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.daily_rent_price:
            if hasattr(self.daily_rent_price, 'to_alipay_dict'):
                params['daily_rent_price'] = self.daily_rent_price.to_alipay_dict()
            else:
                params['daily_rent_price'] = self.daily_rent_price
        if self.device_model_no:
            if hasattr(self.device_model_no, 'to_alipay_dict'):
                params['device_model_no'] = self.device_model_no.to_alipay_dict()
            else:
                params['device_model_no'] = self.device_model_no
        if self.expected_lease_quantity:
            if hasattr(self.expected_lease_quantity, 'to_alipay_dict'):
                params['expected_lease_quantity'] = self.expected_lease_quantity.to_alipay_dict()
            else:
                params['expected_lease_quantity'] = self.expected_lease_quantity
        if self.lease_asset_ids:
            if isinstance(self.lease_asset_ids, list):
                for i in range(0, len(self.lease_asset_ids)):
                    element = self.lease_asset_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.lease_asset_ids[i] = element.to_alipay_dict()
            if hasattr(self.lease_asset_ids, 'to_alipay_dict'):
                params['lease_asset_ids'] = self.lease_asset_ids.to_alipay_dict()
            else:
                params['lease_asset_ids'] = self.lease_asset_ids
        if self.month_rent_price:
            if hasattr(self.month_rent_price, 'to_alipay_dict'):
                params['month_rent_price'] = self.month_rent_price.to_alipay_dict()
            else:
                params['month_rent_price'] = self.month_rent_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Leaseholds()
        if 'daily_rent_price' in d:
            o.daily_rent_price = d['daily_rent_price']
        if 'device_model_no' in d:
            o.device_model_no = d['device_model_no']
        if 'expected_lease_quantity' in d:
            o.expected_lease_quantity = d['expected_lease_quantity']
        if 'lease_asset_ids' in d:
            o.lease_asset_ids = d['lease_asset_ids']
        if 'month_rent_price' in d:
            o.month_rent_price = d['month_rent_price']
        return o


