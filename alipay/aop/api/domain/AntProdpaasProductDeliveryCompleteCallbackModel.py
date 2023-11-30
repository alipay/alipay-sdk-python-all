#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SupplierDeliveryBatch import SupplierDeliveryBatch
from alipay.aop.api.domain.SupplierItemAttrField import SupplierItemAttrField
from alipay.aop.api.domain.SupplierLogisticsInfo import SupplierLogisticsInfo


class AntProdpaasProductDeliveryCompleteCallbackModel(object):

    def __init__(self):
        self._abnormal_feedback = None
        self._abnormal_reason = None
        self._actual_amount = None
        self._batch_no = None
        self._batchs = None
        self._delivery_order_code = None
        self._expire_date = None
        self._extend_pros = None
        self._logistics_info = None
        self._plan_amount = None
        self._produce_code = None
        self._product_date = None
        self._warehouse_code = None

    @property
    def abnormal_feedback(self):
        return self._abnormal_feedback

    @abnormal_feedback.setter
    def abnormal_feedback(self, value):
        self._abnormal_feedback = value
    @property
    def abnormal_reason(self):
        return self._abnormal_reason

    @abnormal_reason.setter
    def abnormal_reason(self, value):
        self._abnormal_reason = value
    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batchs(self):
        return self._batchs

    @batchs.setter
    def batchs(self, value):
        if isinstance(value, list):
            self._batchs = list()
            for i in value:
                if isinstance(i, SupplierDeliveryBatch):
                    self._batchs.append(i)
                else:
                    self._batchs.append(SupplierDeliveryBatch.from_alipay_dict(i))
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
        if isinstance(value, SupplierItemAttrField):
            self._extend_pros = value
        else:
            self._extend_pros = SupplierItemAttrField.from_alipay_dict(value)
    @property
    def logistics_info(self):
        return self._logistics_info

    @logistics_info.setter
    def logistics_info(self, value):
        if isinstance(value, list):
            self._logistics_info = list()
            for i in value:
                if isinstance(i, SupplierLogisticsInfo):
                    self._logistics_info.append(i)
                else:
                    self._logistics_info.append(SupplierLogisticsInfo.from_alipay_dict(i))
    @property
    def plan_amount(self):
        return self._plan_amount

    @plan_amount.setter
    def plan_amount(self, value):
        self._plan_amount = value
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
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.abnormal_feedback:
            if hasattr(self.abnormal_feedback, 'to_alipay_dict'):
                params['abnormal_feedback'] = self.abnormal_feedback.to_alipay_dict()
            else:
                params['abnormal_feedback'] = self.abnormal_feedback
        if self.abnormal_reason:
            if hasattr(self.abnormal_reason, 'to_alipay_dict'):
                params['abnormal_reason'] = self.abnormal_reason.to_alipay_dict()
            else:
                params['abnormal_reason'] = self.abnormal_reason
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.batchs:
            if isinstance(self.batchs, list):
                for i in range(0, len(self.batchs)):
                    element = self.batchs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.batchs[i] = element.to_alipay_dict()
            if hasattr(self.batchs, 'to_alipay_dict'):
                params['batchs'] = self.batchs.to_alipay_dict()
            else:
                params['batchs'] = self.batchs
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
            if hasattr(self.extend_pros, 'to_alipay_dict'):
                params['extend_pros'] = self.extend_pros.to_alipay_dict()
            else:
                params['extend_pros'] = self.extend_pros
        if self.logistics_info:
            if isinstance(self.logistics_info, list):
                for i in range(0, len(self.logistics_info)):
                    element = self.logistics_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_info[i] = element.to_alipay_dict()
            if hasattr(self.logistics_info, 'to_alipay_dict'):
                params['logistics_info'] = self.logistics_info.to_alipay_dict()
            else:
                params['logistics_info'] = self.logistics_info
        if self.plan_amount:
            if hasattr(self.plan_amount, 'to_alipay_dict'):
                params['plan_amount'] = self.plan_amount.to_alipay_dict()
            else:
                params['plan_amount'] = self.plan_amount
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
        o = AntProdpaasProductDeliveryCompleteCallbackModel()
        if 'abnormal_feedback' in d:
            o.abnormal_feedback = d['abnormal_feedback']
        if 'abnormal_reason' in d:
            o.abnormal_reason = d['abnormal_reason']
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'batchs' in d:
            o.batchs = d['batchs']
        if 'delivery_order_code' in d:
            o.delivery_order_code = d['delivery_order_code']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'extend_pros' in d:
            o.extend_pros = d['extend_pros']
        if 'logistics_info' in d:
            o.logistics_info = d['logistics_info']
        if 'plan_amount' in d:
            o.plan_amount = d['plan_amount']
        if 'produce_code' in d:
            o.produce_code = d['produce_code']
        if 'product_date' in d:
            o.product_date = d['product_date']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


