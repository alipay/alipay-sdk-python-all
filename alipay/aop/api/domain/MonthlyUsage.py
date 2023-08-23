#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MonthlyUsage(object):

    def __init__(self):
        self._excess_usage = None
        self._fee_item_code = None
        self._fee_item_name = None
        self._fee_item_unit = None
        self._free_usage = None
        self._month = None
        self._resource_package_usage = None
        self._total_usage = None

    @property
    def excess_usage(self):
        return self._excess_usage

    @excess_usage.setter
    def excess_usage(self, value):
        self._excess_usage = value
    @property
    def fee_item_code(self):
        return self._fee_item_code

    @fee_item_code.setter
    def fee_item_code(self, value):
        self._fee_item_code = value
    @property
    def fee_item_name(self):
        return self._fee_item_name

    @fee_item_name.setter
    def fee_item_name(self, value):
        self._fee_item_name = value
    @property
    def fee_item_unit(self):
        return self._fee_item_unit

    @fee_item_unit.setter
    def fee_item_unit(self, value):
        self._fee_item_unit = value
    @property
    def free_usage(self):
        return self._free_usage

    @free_usage.setter
    def free_usage(self, value):
        self._free_usage = value
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
    @property
    def resource_package_usage(self):
        return self._resource_package_usage

    @resource_package_usage.setter
    def resource_package_usage(self, value):
        self._resource_package_usage = value
    @property
    def total_usage(self):
        return self._total_usage

    @total_usage.setter
    def total_usage(self, value):
        self._total_usage = value


    def to_alipay_dict(self):
        params = dict()
        if self.excess_usage:
            if hasattr(self.excess_usage, 'to_alipay_dict'):
                params['excess_usage'] = self.excess_usage.to_alipay_dict()
            else:
                params['excess_usage'] = self.excess_usage
        if self.fee_item_code:
            if hasattr(self.fee_item_code, 'to_alipay_dict'):
                params['fee_item_code'] = self.fee_item_code.to_alipay_dict()
            else:
                params['fee_item_code'] = self.fee_item_code
        if self.fee_item_name:
            if hasattr(self.fee_item_name, 'to_alipay_dict'):
                params['fee_item_name'] = self.fee_item_name.to_alipay_dict()
            else:
                params['fee_item_name'] = self.fee_item_name
        if self.fee_item_unit:
            if hasattr(self.fee_item_unit, 'to_alipay_dict'):
                params['fee_item_unit'] = self.fee_item_unit.to_alipay_dict()
            else:
                params['fee_item_unit'] = self.fee_item_unit
        if self.free_usage:
            if hasattr(self.free_usage, 'to_alipay_dict'):
                params['free_usage'] = self.free_usage.to_alipay_dict()
            else:
                params['free_usage'] = self.free_usage
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.resource_package_usage:
            if hasattr(self.resource_package_usage, 'to_alipay_dict'):
                params['resource_package_usage'] = self.resource_package_usage.to_alipay_dict()
            else:
                params['resource_package_usage'] = self.resource_package_usage
        if self.total_usage:
            if hasattr(self.total_usage, 'to_alipay_dict'):
                params['total_usage'] = self.total_usage.to_alipay_dict()
            else:
                params['total_usage'] = self.total_usage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MonthlyUsage()
        if 'excess_usage' in d:
            o.excess_usage = d['excess_usage']
        if 'fee_item_code' in d:
            o.fee_item_code = d['fee_item_code']
        if 'fee_item_name' in d:
            o.fee_item_name = d['fee_item_name']
        if 'fee_item_unit' in d:
            o.fee_item_unit = d['fee_item_unit']
        if 'free_usage' in d:
            o.free_usage = d['free_usage']
        if 'month' in d:
            o.month = d['month']
        if 'resource_package_usage' in d:
            o.resource_package_usage = d['resource_package_usage']
        if 'total_usage' in d:
            o.total_usage = d['total_usage']
        return o


