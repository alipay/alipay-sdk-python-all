#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceTaskInfo(object):

    def __init__(self):
        self._finish_date = None
        self._finish_invoice_amount = None
        self._invoice_amount = None
        self._merchant_id = None
        self._merchant_name = None
        self._period_begin_date = None
        self._period_end_date = None
        self._task_id = None
        self._task_name = None
        self._task_status = None
        self._total_pay_amount = None
        self._total_refund_amount = None

    @property
    def finish_date(self):
        return self._finish_date

    @finish_date.setter
    def finish_date(self, value):
        self._finish_date = value
    @property
    def finish_invoice_amount(self):
        return self._finish_invoice_amount

    @finish_invoice_amount.setter
    def finish_invoice_amount(self, value):
        self._finish_invoice_amount = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def period_begin_date(self):
        return self._period_begin_date

    @period_begin_date.setter
    def period_begin_date(self, value):
        self._period_begin_date = value
    @property
    def period_end_date(self):
        return self._period_end_date

    @period_end_date.setter
    def period_end_date(self, value):
        self._period_end_date = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def total_pay_amount(self):
        return self._total_pay_amount

    @total_pay_amount.setter
    def total_pay_amount(self, value):
        self._total_pay_amount = value
    @property
    def total_refund_amount(self):
        return self._total_refund_amount

    @total_refund_amount.setter
    def total_refund_amount(self, value):
        self._total_refund_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.finish_date:
            if hasattr(self.finish_date, 'to_alipay_dict'):
                params['finish_date'] = self.finish_date.to_alipay_dict()
            else:
                params['finish_date'] = self.finish_date
        if self.finish_invoice_amount:
            if hasattr(self.finish_invoice_amount, 'to_alipay_dict'):
                params['finish_invoice_amount'] = self.finish_invoice_amount.to_alipay_dict()
            else:
                params['finish_invoice_amount'] = self.finish_invoice_amount
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.period_begin_date:
            if hasattr(self.period_begin_date, 'to_alipay_dict'):
                params['period_begin_date'] = self.period_begin_date.to_alipay_dict()
            else:
                params['period_begin_date'] = self.period_begin_date
        if self.period_end_date:
            if hasattr(self.period_end_date, 'to_alipay_dict'):
                params['period_end_date'] = self.period_end_date.to_alipay_dict()
            else:
                params['period_end_date'] = self.period_end_date
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.total_pay_amount:
            if hasattr(self.total_pay_amount, 'to_alipay_dict'):
                params['total_pay_amount'] = self.total_pay_amount.to_alipay_dict()
            else:
                params['total_pay_amount'] = self.total_pay_amount
        if self.total_refund_amount:
            if hasattr(self.total_refund_amount, 'to_alipay_dict'):
                params['total_refund_amount'] = self.total_refund_amount.to_alipay_dict()
            else:
                params['total_refund_amount'] = self.total_refund_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceTaskInfo()
        if 'finish_date' in d:
            o.finish_date = d['finish_date']
        if 'finish_invoice_amount' in d:
            o.finish_invoice_amount = d['finish_invoice_amount']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'period_begin_date' in d:
            o.period_begin_date = d['period_begin_date']
        if 'period_end_date' in d:
            o.period_end_date = d['period_end_date']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'total_pay_amount' in d:
            o.total_pay_amount = d['total_pay_amount']
        if 'total_refund_amount' in d:
            o.total_refund_amount = d['total_refund_amount']
        return o


