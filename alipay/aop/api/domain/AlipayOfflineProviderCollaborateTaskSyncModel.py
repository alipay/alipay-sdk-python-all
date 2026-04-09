#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderCollaborateTaskSyncModel(object):

    def __init__(self):
        self._delivery_completed = None
        self._delivery_completion_date = None
        self._first_sales_date = None
        self._order_transaction = None
        self._out_merchant_id = None
        self._printer_connected = None
        self._shop_id = None
        self._task_id = None
        self._uploaded_product_count = None

    @property
    def delivery_completed(self):
        return self._delivery_completed

    @delivery_completed.setter
    def delivery_completed(self, value):
        self._delivery_completed = value
    @property
    def delivery_completion_date(self):
        return self._delivery_completion_date

    @delivery_completion_date.setter
    def delivery_completion_date(self, value):
        self._delivery_completion_date = value
    @property
    def first_sales_date(self):
        return self._first_sales_date

    @first_sales_date.setter
    def first_sales_date(self, value):
        self._first_sales_date = value
    @property
    def order_transaction(self):
        return self._order_transaction

    @order_transaction.setter
    def order_transaction(self, value):
        self._order_transaction = value
    @property
    def out_merchant_id(self):
        return self._out_merchant_id

    @out_merchant_id.setter
    def out_merchant_id(self, value):
        self._out_merchant_id = value
    @property
    def printer_connected(self):
        return self._printer_connected

    @printer_connected.setter
    def printer_connected(self, value):
        self._printer_connected = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def uploaded_product_count(self):
        return self._uploaded_product_count

    @uploaded_product_count.setter
    def uploaded_product_count(self, value):
        self._uploaded_product_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_completed:
            if hasattr(self.delivery_completed, 'to_alipay_dict'):
                params['delivery_completed'] = self.delivery_completed.to_alipay_dict()
            else:
                params['delivery_completed'] = self.delivery_completed
        if self.delivery_completion_date:
            if hasattr(self.delivery_completion_date, 'to_alipay_dict'):
                params['delivery_completion_date'] = self.delivery_completion_date.to_alipay_dict()
            else:
                params['delivery_completion_date'] = self.delivery_completion_date
        if self.first_sales_date:
            if hasattr(self.first_sales_date, 'to_alipay_dict'):
                params['first_sales_date'] = self.first_sales_date.to_alipay_dict()
            else:
                params['first_sales_date'] = self.first_sales_date
        if self.order_transaction:
            if hasattr(self.order_transaction, 'to_alipay_dict'):
                params['order_transaction'] = self.order_transaction.to_alipay_dict()
            else:
                params['order_transaction'] = self.order_transaction
        if self.out_merchant_id:
            if hasattr(self.out_merchant_id, 'to_alipay_dict'):
                params['out_merchant_id'] = self.out_merchant_id.to_alipay_dict()
            else:
                params['out_merchant_id'] = self.out_merchant_id
        if self.printer_connected:
            if hasattr(self.printer_connected, 'to_alipay_dict'):
                params['printer_connected'] = self.printer_connected.to_alipay_dict()
            else:
                params['printer_connected'] = self.printer_connected
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.uploaded_product_count:
            if hasattr(self.uploaded_product_count, 'to_alipay_dict'):
                params['uploaded_product_count'] = self.uploaded_product_count.to_alipay_dict()
            else:
                params['uploaded_product_count'] = self.uploaded_product_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderCollaborateTaskSyncModel()
        if 'delivery_completed' in d:
            o.delivery_completed = d['delivery_completed']
        if 'delivery_completion_date' in d:
            o.delivery_completion_date = d['delivery_completion_date']
        if 'first_sales_date' in d:
            o.first_sales_date = d['first_sales_date']
        if 'order_transaction' in d:
            o.order_transaction = d['order_transaction']
        if 'out_merchant_id' in d:
            o.out_merchant_id = d['out_merchant_id']
        if 'printer_connected' in d:
            o.printer_connected = d['printer_connected']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'uploaded_product_count' in d:
            o.uploaded_product_count = d['uploaded_product_count']
        return o


