#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncInputinvoiceInvoiceNotifyModel(object):

    def __init__(self):
        self._error_code = None
        self._error_msg = None
        self._id = None
        self._invoice_code = None
        self._invoice_no = None
        self._mq_key = None
        self._process_result = None
        self._process_type = None
        self._related_order = None
        self._task_id = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def mq_key(self):
        return self._mq_key

    @mq_key.setter
    def mq_key(self, value):
        self._mq_key = value
    @property
    def process_result(self):
        return self._process_result

    @process_result.setter
    def process_result(self, value):
        self._process_result = value
    @property
    def process_type(self):
        return self._process_type

    @process_type.setter
    def process_type(self, value):
        self._process_type = value
    @property
    def related_order(self):
        return self._related_order

    @related_order.setter
    def related_order(self, value):
        self._related_order = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.mq_key:
            if hasattr(self.mq_key, 'to_alipay_dict'):
                params['mq_key'] = self.mq_key.to_alipay_dict()
            else:
                params['mq_key'] = self.mq_key
        if self.process_result:
            if hasattr(self.process_result, 'to_alipay_dict'):
                params['process_result'] = self.process_result.to_alipay_dict()
            else:
                params['process_result'] = self.process_result
        if self.process_type:
            if hasattr(self.process_type, 'to_alipay_dict'):
                params['process_type'] = self.process_type.to_alipay_dict()
            else:
                params['process_type'] = self.process_type
        if self.related_order:
            if hasattr(self.related_order, 'to_alipay_dict'):
                params['related_order'] = self.related_order.to_alipay_dict()
            else:
                params['related_order'] = self.related_order
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInputinvoiceInvoiceNotifyModel()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'id' in d:
            o.id = d['id']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'mq_key' in d:
            o.mq_key = d['mq_key']
        if 'process_result' in d:
            o.process_result = d['process_result']
        if 'process_type' in d:
            o.process_type = d['process_type']
        if 'related_order' in d:
            o.related_order = d['related_order']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


