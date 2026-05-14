#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CoreMaterialPoData(object):

    def __init__(self):
        self._delivered_count = None
        self._material_id = None
        self._material_name = None
        self._memo = None
        self._order_time = None
        self._out_po_no = None
        self._out_supplier_id = None
        self._out_supplier_name = None
        self._po_status = None
        self._total_count = None
        self._transferring_count = None

    @property
    def delivered_count(self):
        return self._delivered_count

    @delivered_count.setter
    def delivered_count(self, value):
        self._delivered_count = value
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
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def out_po_no(self):
        return self._out_po_no

    @out_po_no.setter
    def out_po_no(self, value):
        self._out_po_no = value
    @property
    def out_supplier_id(self):
        return self._out_supplier_id

    @out_supplier_id.setter
    def out_supplier_id(self, value):
        self._out_supplier_id = value
    @property
    def out_supplier_name(self):
        return self._out_supplier_name

    @out_supplier_name.setter
    def out_supplier_name(self, value):
        self._out_supplier_name = value
    @property
    def po_status(self):
        return self._po_status

    @po_status.setter
    def po_status(self, value):
        self._po_status = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def transferring_count(self):
        return self._transferring_count

    @transferring_count.setter
    def transferring_count(self, value):
        self._transferring_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivered_count:
            if hasattr(self.delivered_count, 'to_alipay_dict'):
                params['delivered_count'] = self.delivered_count.to_alipay_dict()
            else:
                params['delivered_count'] = self.delivered_count
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
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.out_po_no:
            if hasattr(self.out_po_no, 'to_alipay_dict'):
                params['out_po_no'] = self.out_po_no.to_alipay_dict()
            else:
                params['out_po_no'] = self.out_po_no
        if self.out_supplier_id:
            if hasattr(self.out_supplier_id, 'to_alipay_dict'):
                params['out_supplier_id'] = self.out_supplier_id.to_alipay_dict()
            else:
                params['out_supplier_id'] = self.out_supplier_id
        if self.out_supplier_name:
            if hasattr(self.out_supplier_name, 'to_alipay_dict'):
                params['out_supplier_name'] = self.out_supplier_name.to_alipay_dict()
            else:
                params['out_supplier_name'] = self.out_supplier_name
        if self.po_status:
            if hasattr(self.po_status, 'to_alipay_dict'):
                params['po_status'] = self.po_status.to_alipay_dict()
            else:
                params['po_status'] = self.po_status
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.transferring_count:
            if hasattr(self.transferring_count, 'to_alipay_dict'):
                params['transferring_count'] = self.transferring_count.to_alipay_dict()
            else:
                params['transferring_count'] = self.transferring_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CoreMaterialPoData()
        if 'delivered_count' in d:
            o.delivered_count = d['delivered_count']
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'material_name' in d:
            o.material_name = d['material_name']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'out_po_no' in d:
            o.out_po_no = d['out_po_no']
        if 'out_supplier_id' in d:
            o.out_supplier_id = d['out_supplier_id']
        if 'out_supplier_name' in d:
            o.out_supplier_name = d['out_supplier_name']
        if 'po_status' in d:
            o.po_status = d['po_status']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'transferring_count' in d:
            o.transferring_count = d['transferring_count']
        return o


