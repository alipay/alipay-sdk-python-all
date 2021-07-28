#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Money import Money


class TuitionInremitOrder(object):

    def __init__(self):
        self._alipay_payment_id = None
        self._isv_payment_id = None
        self._order_created = None
        self._order_modified = None
        self._order_status = None
        self._order_status_desc = None
        self._payment_amount = None
        self._payment_item_code = None
        self._school_pid = None
        self._student_id = None

    @property
    def alipay_payment_id(self):
        return self._alipay_payment_id

    @alipay_payment_id.setter
    def alipay_payment_id(self, value):
        self._alipay_payment_id = value
    @property
    def isv_payment_id(self):
        return self._isv_payment_id

    @isv_payment_id.setter
    def isv_payment_id(self, value):
        self._isv_payment_id = value
    @property
    def order_created(self):
        return self._order_created

    @order_created.setter
    def order_created(self, value):
        self._order_created = value
    @property
    def order_modified(self):
        return self._order_modified

    @order_modified.setter
    def order_modified(self, value):
        self._order_modified = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_status_desc(self):
        return self._order_status_desc

    @order_status_desc.setter
    def order_status_desc(self, value):
        self._order_status_desc = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        if isinstance(value, Money):
            self._payment_amount = value
        else:
            self._payment_amount = Money.from_alipay_dict(value)
    @property
    def payment_item_code(self):
        return self._payment_item_code

    @payment_item_code.setter
    def payment_item_code(self, value):
        self._payment_item_code = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_payment_id:
            if hasattr(self.alipay_payment_id, 'to_alipay_dict'):
                params['alipay_payment_id'] = self.alipay_payment_id.to_alipay_dict()
            else:
                params['alipay_payment_id'] = self.alipay_payment_id
        if self.isv_payment_id:
            if hasattr(self.isv_payment_id, 'to_alipay_dict'):
                params['isv_payment_id'] = self.isv_payment_id.to_alipay_dict()
            else:
                params['isv_payment_id'] = self.isv_payment_id
        if self.order_created:
            if hasattr(self.order_created, 'to_alipay_dict'):
                params['order_created'] = self.order_created.to_alipay_dict()
            else:
                params['order_created'] = self.order_created
        if self.order_modified:
            if hasattr(self.order_modified, 'to_alipay_dict'):
                params['order_modified'] = self.order_modified.to_alipay_dict()
            else:
                params['order_modified'] = self.order_modified
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_status_desc:
            if hasattr(self.order_status_desc, 'to_alipay_dict'):
                params['order_status_desc'] = self.order_status_desc.to_alipay_dict()
            else:
                params['order_status_desc'] = self.order_status_desc
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_item_code:
            if hasattr(self.payment_item_code, 'to_alipay_dict'):
                params['payment_item_code'] = self.payment_item_code.to_alipay_dict()
            else:
                params['payment_item_code'] = self.payment_item_code
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        if self.student_id:
            if hasattr(self.student_id, 'to_alipay_dict'):
                params['student_id'] = self.student_id.to_alipay_dict()
            else:
                params['student_id'] = self.student_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionInremitOrder()
        if 'alipay_payment_id' in d:
            o.alipay_payment_id = d['alipay_payment_id']
        if 'isv_payment_id' in d:
            o.isv_payment_id = d['isv_payment_id']
        if 'order_created' in d:
            o.order_created = d['order_created']
        if 'order_modified' in d:
            o.order_modified = d['order_modified']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_status_desc' in d:
            o.order_status_desc = d['order_status_desc']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_item_code' in d:
            o.payment_item_code = d['payment_item_code']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        if 'student_id' in d:
            o.student_id = d['student_id']
        return o


