#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ThirdPartyRefundExceptionOrderList(object):

    def __init__(self):
        self._certificate_id_list = None
        self._failure_reason = None
        self._gmt_create = None
        self._merchant_order_no = None
        self._platform_order_no = None
        self._product_name = None
        self._refund_amount = None
        self._refund_apply_time = None
        self._status = None
        self._task_id = None
        self._trade_no = None

    @property
    def certificate_id_list(self):
        return self._certificate_id_list

    @certificate_id_list.setter
    def certificate_id_list(self, value):
        if isinstance(value, list):
            self._certificate_id_list = list()
            for i in value:
                self._certificate_id_list.append(i)
    @property
    def failure_reason(self):
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, value):
        self._failure_reason = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def platform_order_no(self):
        return self._platform_order_no

    @platform_order_no.setter
    def platform_order_no(self, value):
        self._platform_order_no = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_apply_time(self):
        return self._refund_apply_time

    @refund_apply_time.setter
    def refund_apply_time(self, value):
        self._refund_apply_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id_list:
            if isinstance(self.certificate_id_list, list):
                for i in range(0, len(self.certificate_id_list)):
                    element = self.certificate_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certificate_id_list[i] = element.to_alipay_dict()
            if hasattr(self.certificate_id_list, 'to_alipay_dict'):
                params['certificate_id_list'] = self.certificate_id_list.to_alipay_dict()
            else:
                params['certificate_id_list'] = self.certificate_id_list
        if self.failure_reason:
            if hasattr(self.failure_reason, 'to_alipay_dict'):
                params['failure_reason'] = self.failure_reason.to_alipay_dict()
            else:
                params['failure_reason'] = self.failure_reason
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.platform_order_no:
            if hasattr(self.platform_order_no, 'to_alipay_dict'):
                params['platform_order_no'] = self.platform_order_no.to_alipay_dict()
            else:
                params['platform_order_no'] = self.platform_order_no
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_apply_time:
            if hasattr(self.refund_apply_time, 'to_alipay_dict'):
                params['refund_apply_time'] = self.refund_apply_time.to_alipay_dict()
            else:
                params['refund_apply_time'] = self.refund_apply_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ThirdPartyRefundExceptionOrderList()
        if 'certificate_id_list' in d:
            o.certificate_id_list = d['certificate_id_list']
        if 'failure_reason' in d:
            o.failure_reason = d['failure_reason']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'platform_order_no' in d:
            o.platform_order_no = d['platform_order_no']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_apply_time' in d:
            o.refund_apply_time = d['refund_apply_time']
        if 'status' in d:
            o.status = d['status']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


