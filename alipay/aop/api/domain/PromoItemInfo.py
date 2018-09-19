#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConstraintInfo import ConstraintInfo
from alipay.aop.api.domain.Voucher import Voucher


class PromoItemInfo(object):

    def __init__(self):
        self._constraint_info = None
        self._id = None
        self._sale_end_time = None
        self._sale_start_time = None
        self._total_inventory = None
        self._voucher = None

    @property
    def constraint_info(self):
        return self._constraint_info

    @constraint_info.setter
    def constraint_info(self, value):
        if isinstance(value, ConstraintInfo):
            self._constraint_info = value
        else:
            self._constraint_info = ConstraintInfo.from_alipay_dict(value)
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def sale_end_time(self):
        return self._sale_end_time

    @sale_end_time.setter
    def sale_end_time(self, value):
        self._sale_end_time = value
    @property
    def sale_start_time(self):
        return self._sale_start_time

    @sale_start_time.setter
    def sale_start_time(self, value):
        self._sale_start_time = value
    @property
    def total_inventory(self):
        return self._total_inventory

    @total_inventory.setter
    def total_inventory(self, value):
        self._total_inventory = value
    @property
    def voucher(self):
        return self._voucher

    @voucher.setter
    def voucher(self, value):
        if isinstance(value, Voucher):
            self._voucher = value
        else:
            self._voucher = Voucher.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.constraint_info:
            if hasattr(self.constraint_info, 'to_alipay_dict'):
                params['constraint_info'] = self.constraint_info.to_alipay_dict()
            else:
                params['constraint_info'] = self.constraint_info
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.sale_end_time:
            if hasattr(self.sale_end_time, 'to_alipay_dict'):
                params['sale_end_time'] = self.sale_end_time.to_alipay_dict()
            else:
                params['sale_end_time'] = self.sale_end_time
        if self.sale_start_time:
            if hasattr(self.sale_start_time, 'to_alipay_dict'):
                params['sale_start_time'] = self.sale_start_time.to_alipay_dict()
            else:
                params['sale_start_time'] = self.sale_start_time
        if self.total_inventory:
            if hasattr(self.total_inventory, 'to_alipay_dict'):
                params['total_inventory'] = self.total_inventory.to_alipay_dict()
            else:
                params['total_inventory'] = self.total_inventory
        if self.voucher:
            if hasattr(self.voucher, 'to_alipay_dict'):
                params['voucher'] = self.voucher.to_alipay_dict()
            else:
                params['voucher'] = self.voucher
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoItemInfo()
        if 'constraint_info' in d:
            o.constraint_info = d['constraint_info']
        if 'id' in d:
            o.id = d['id']
        if 'sale_end_time' in d:
            o.sale_end_time = d['sale_end_time']
        if 'sale_start_time' in d:
            o.sale_start_time = d['sale_start_time']
        if 'total_inventory' in d:
            o.total_inventory = d['total_inventory']
        if 'voucher' in d:
            o.voucher = d['voucher']
        return o


