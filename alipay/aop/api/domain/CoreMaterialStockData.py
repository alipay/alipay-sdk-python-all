#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CoreMaterialStockData(object):

    def __init__(self):
        self._actual_count = None
        self._material_id = None
        self._material_name = None
        self._record_date = None
        self._transferring_count = None
        self._warehouse_id = None
        self._warehouse_name = None

    @property
    def actual_count(self):
        return self._actual_count

    @actual_count.setter
    def actual_count(self, value):
        self._actual_count = value
    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def material_name(self):
        return self._material_name

    @material_name.setter
    def material_name(self, value):
        self._material_name = value
    @property
    def record_date(self):
        return self._record_date

    @record_date.setter
    def record_date(self, value):
        self._record_date = value
    @property
    def transferring_count(self):
        return self._transferring_count

    @transferring_count.setter
    def transferring_count(self, value):
        self._transferring_count = value
    @property
    def warehouse_id(self):
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, value):
        self._warehouse_id = value
    @property
    def warehouse_name(self):
        return self._warehouse_name

    @warehouse_name.setter
    def warehouse_name(self, value):
        self._warehouse_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_count:
            if hasattr(self.actual_count, 'to_alipay_dict'):
                params['actual_count'] = self.actual_count.to_alipay_dict()
            else:
                params['actual_count'] = self.actual_count
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.material_name:
            if hasattr(self.material_name, 'to_alipay_dict'):
                params['material_name'] = self.material_name.to_alipay_dict()
            else:
                params['material_name'] = self.material_name
        if self.record_date:
            if hasattr(self.record_date, 'to_alipay_dict'):
                params['record_date'] = self.record_date.to_alipay_dict()
            else:
                params['record_date'] = self.record_date
        if self.transferring_count:
            if hasattr(self.transferring_count, 'to_alipay_dict'):
                params['transferring_count'] = self.transferring_count.to_alipay_dict()
            else:
                params['transferring_count'] = self.transferring_count
        if self.warehouse_id:
            if hasattr(self.warehouse_id, 'to_alipay_dict'):
                params['warehouse_id'] = self.warehouse_id.to_alipay_dict()
            else:
                params['warehouse_id'] = self.warehouse_id
        if self.warehouse_name:
            if hasattr(self.warehouse_name, 'to_alipay_dict'):
                params['warehouse_name'] = self.warehouse_name.to_alipay_dict()
            else:
                params['warehouse_name'] = self.warehouse_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CoreMaterialStockData()
        if 'actual_count' in d:
            o.actual_count = d['actual_count']
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'material_name' in d:
            o.material_name = d['material_name']
        if 'record_date' in d:
            o.record_date = d['record_date']
        if 'transferring_count' in d:
            o.transferring_count = d['transferring_count']
        if 'warehouse_id' in d:
            o.warehouse_id = d['warehouse_id']
        if 'warehouse_name' in d:
            o.warehouse_name = d['warehouse_name']
        return o


