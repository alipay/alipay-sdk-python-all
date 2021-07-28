#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KmsBakingInventoryDTO(object):

    def __init__(self):
        self._accumulate_inventory = None
        self._data_id = None
        self._ending_inventory = None
        self._ending_position = None
        self._opening_inventory = None
        self._operation_name = None
        self._operation_num = None
        self._operation_time = None
        self._operator = None
        self._sku_batch = None
        self._sku_id = None
        self._starting_position = None

    @property
    def accumulate_inventory(self):
        return self._accumulate_inventory

    @accumulate_inventory.setter
    def accumulate_inventory(self, value):
        self._accumulate_inventory = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def ending_inventory(self):
        return self._ending_inventory

    @ending_inventory.setter
    def ending_inventory(self, value):
        self._ending_inventory = value
    @property
    def ending_position(self):
        return self._ending_position

    @ending_position.setter
    def ending_position(self, value):
        self._ending_position = value
    @property
    def opening_inventory(self):
        return self._opening_inventory

    @opening_inventory.setter
    def opening_inventory(self, value):
        self._opening_inventory = value
    @property
    def operation_name(self):
        return self._operation_name

    @operation_name.setter
    def operation_name(self, value):
        self._operation_name = value
    @property
    def operation_num(self):
        return self._operation_num

    @operation_num.setter
    def operation_num(self, value):
        self._operation_num = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def sku_batch(self):
        return self._sku_batch

    @sku_batch.setter
    def sku_batch(self, value):
        self._sku_batch = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def starting_position(self):
        return self._starting_position

    @starting_position.setter
    def starting_position(self, value):
        self._starting_position = value


    def to_alipay_dict(self):
        params = dict()
        if self.accumulate_inventory:
            if hasattr(self.accumulate_inventory, 'to_alipay_dict'):
                params['accumulate_inventory'] = self.accumulate_inventory.to_alipay_dict()
            else:
                params['accumulate_inventory'] = self.accumulate_inventory
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.ending_inventory:
            if hasattr(self.ending_inventory, 'to_alipay_dict'):
                params['ending_inventory'] = self.ending_inventory.to_alipay_dict()
            else:
                params['ending_inventory'] = self.ending_inventory
        if self.ending_position:
            if hasattr(self.ending_position, 'to_alipay_dict'):
                params['ending_position'] = self.ending_position.to_alipay_dict()
            else:
                params['ending_position'] = self.ending_position
        if self.opening_inventory:
            if hasattr(self.opening_inventory, 'to_alipay_dict'):
                params['opening_inventory'] = self.opening_inventory.to_alipay_dict()
            else:
                params['opening_inventory'] = self.opening_inventory
        if self.operation_name:
            if hasattr(self.operation_name, 'to_alipay_dict'):
                params['operation_name'] = self.operation_name.to_alipay_dict()
            else:
                params['operation_name'] = self.operation_name
        if self.operation_num:
            if hasattr(self.operation_num, 'to_alipay_dict'):
                params['operation_num'] = self.operation_num.to_alipay_dict()
            else:
                params['operation_num'] = self.operation_num
        if self.operation_time:
            if hasattr(self.operation_time, 'to_alipay_dict'):
                params['operation_time'] = self.operation_time.to_alipay_dict()
            else:
                params['operation_time'] = self.operation_time
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.sku_batch:
            if hasattr(self.sku_batch, 'to_alipay_dict'):
                params['sku_batch'] = self.sku_batch.to_alipay_dict()
            else:
                params['sku_batch'] = self.sku_batch
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.starting_position:
            if hasattr(self.starting_position, 'to_alipay_dict'):
                params['starting_position'] = self.starting_position.to_alipay_dict()
            else:
                params['starting_position'] = self.starting_position
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KmsBakingInventoryDTO()
        if 'accumulate_inventory' in d:
            o.accumulate_inventory = d['accumulate_inventory']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'ending_inventory' in d:
            o.ending_inventory = d['ending_inventory']
        if 'ending_position' in d:
            o.ending_position = d['ending_position']
        if 'opening_inventory' in d:
            o.opening_inventory = d['opening_inventory']
        if 'operation_name' in d:
            o.operation_name = d['operation_name']
        if 'operation_num' in d:
            o.operation_num = d['operation_num']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'operator' in d:
            o.operator = d['operator']
        if 'sku_batch' in d:
            o.sku_batch = d['sku_batch']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'starting_position' in d:
            o.starting_position = d['starting_position']
        return o


