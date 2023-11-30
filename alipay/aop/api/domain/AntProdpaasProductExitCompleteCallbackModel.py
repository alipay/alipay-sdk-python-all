#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SupplierItemAttrField import SupplierItemAttrField
from alipay.aop.api.domain.SupplierLogisticsInfo import SupplierLogisticsInfo


class AntProdpaasProductExitCompleteCallbackModel(object):

    def __init__(self):
        self._actual_qty = None
        self._batch_no = None
        self._confirm_type = None
        self._delivery_order_code = None
        self._expire_date = None
        self._extend_pros = None
        self._item_code = None
        self._logistics_info = None
        self._order_type = None
        self._plan_qty = None
        self._produce_code = None
        self._product_date = None
        self._status = None
        self._warehouse_code = None

    @property
    def actual_qty(self):
        return self._actual_qty

    @actual_qty.setter
    def actual_qty(self, value):
        self._actual_qty = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def confirm_type(self):
        return self._confirm_type

    @confirm_type.setter
    def confirm_type(self, value):
        self._confirm_type = value
    @property
    def delivery_order_code(self):
        return self._delivery_order_code

    @delivery_order_code.setter
    def delivery_order_code(self, value):
        self._delivery_order_code = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def extend_pros(self):
        return self._extend_pros

    @extend_pros.setter
    def extend_pros(self, value):
        if isinstance(value, list):
            self._extend_pros = list()
            for i in value:
                if isinstance(i, SupplierItemAttrField):
                    self._extend_pros.append(i)
                else:
                    self._extend_pros.append(SupplierItemAttrField.from_alipay_dict(i))
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def logistics_info(self):
        return self._logistics_info

    @logistics_info.setter
    def logistics_info(self, value):
        if isinstance(value, SupplierLogisticsInfo):
            self._logistics_info = value
        else:
            self._logistics_info = SupplierLogisticsInfo.from_alipay_dict(value)
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def plan_qty(self):
        return self._plan_qty

    @plan_qty.setter
    def plan_qty(self, value):
        self._plan_qty = value
    @property
    def produce_code(self):
        return self._produce_code

    @produce_code.setter
    def produce_code(self, value):
        self._produce_code = value
    @property
    def product_date(self):
        return self._product_date

    @product_date.setter
    def product_date(self, value):
        self._product_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_qty:
            if hasattr(self.actual_qty, 'to_alipay_dict'):
                params['actual_qty'] = self.actual_qty.to_alipay_dict()
            else:
                params['actual_qty'] = self.actual_qty
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.confirm_type:
            if hasattr(self.confirm_type, 'to_alipay_dict'):
                params['confirm_type'] = self.confirm_type.to_alipay_dict()
            else:
                params['confirm_type'] = self.confirm_type
        if self.delivery_order_code:
            if hasattr(self.delivery_order_code, 'to_alipay_dict'):
                params['delivery_order_code'] = self.delivery_order_code.to_alipay_dict()
            else:
                params['delivery_order_code'] = self.delivery_order_code
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.extend_pros:
            if isinstance(self.extend_pros, list):
                for i in range(0, len(self.extend_pros)):
                    element = self.extend_pros[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_pros[i] = element.to_alipay_dict()
            if hasattr(self.extend_pros, 'to_alipay_dict'):
                params['extend_pros'] = self.extend_pros.to_alipay_dict()
            else:
                params['extend_pros'] = self.extend_pros
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.logistics_info:
            if hasattr(self.logistics_info, 'to_alipay_dict'):
                params['logistics_info'] = self.logistics_info.to_alipay_dict()
            else:
                params['logistics_info'] = self.logistics_info
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.plan_qty:
            if hasattr(self.plan_qty, 'to_alipay_dict'):
                params['plan_qty'] = self.plan_qty.to_alipay_dict()
            else:
                params['plan_qty'] = self.plan_qty
        if self.produce_code:
            if hasattr(self.produce_code, 'to_alipay_dict'):
                params['produce_code'] = self.produce_code.to_alipay_dict()
            else:
                params['produce_code'] = self.produce_code
        if self.product_date:
            if hasattr(self.product_date, 'to_alipay_dict'):
                params['product_date'] = self.product_date.to_alipay_dict()
            else:
                params['product_date'] = self.product_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AntProdpaasProductExitCompleteCallbackModel()
        if 'actual_qty' in d:
            o.actual_qty = d['actual_qty']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'confirm_type' in d:
            o.confirm_type = d['confirm_type']
        if 'delivery_order_code' in d:
            o.delivery_order_code = d['delivery_order_code']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'extend_pros' in d:
            o.extend_pros = d['extend_pros']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'logistics_info' in d:
            o.logistics_info = d['logistics_info']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'plan_qty' in d:
            o.plan_qty = d['plan_qty']
        if 'produce_code' in d:
            o.produce_code = d['produce_code']
        if 'product_date' in d:
            o.product_date = d['product_date']
        if 'status' in d:
            o.status = d['status']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


