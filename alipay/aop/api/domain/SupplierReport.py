#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplierReport(object):

    def __init__(self):
        self._channel = None
        self._operator_id = None
        self._operator_type = None
        self._order_date = None
        self._remark = None
        self._state = None
        self._supplier_id = None
        self._supplier_report_id = None
        self._unique_id = None
        self._warehouse_code = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    def order_date(self, value):
        self._order_date = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def supplier_report_id(self):
        return self._supplier_report_id

    @supplier_report_id.setter
    def supplier_report_id(self, value):
        self._supplier_report_id = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.order_date:
            if hasattr(self.order_date, 'to_alipay_dict'):
                params['order_date'] = self.order_date.to_alipay_dict()
            else:
                params['order_date'] = self.order_date
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.supplier_report_id:
            if hasattr(self.supplier_report_id, 'to_alipay_dict'):
                params['supplier_report_id'] = self.supplier_report_id.to_alipay_dict()
            else:
                params['supplier_report_id'] = self.supplier_report_id
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplierReport()
        if 'channel' in d:
            o.channel = d['channel']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'order_date' in d:
            o.order_date = d['order_date']
        if 'remark' in d:
            o.remark = d['remark']
        if 'state' in d:
            o.state = d['state']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'supplier_report_id' in d:
            o.supplier_report_id = d['supplier_report_id']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


