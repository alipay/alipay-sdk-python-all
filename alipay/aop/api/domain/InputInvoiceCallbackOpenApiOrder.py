#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InputInvoiceCallbackOpenApiOrder(object):

    def __init__(self):
        self._error_info = None
        self._invoice_id = None
        self._mq_key = None
        self._notify_succeeded = None

    @property
    def error_info(self):
        return self._error_info

    @error_info.setter
    def error_info(self, value):
        self._error_info = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def mq_key(self):
        return self._mq_key

    @mq_key.setter
    def mq_key(self, value):
        self._mq_key = value
    @property
    def notify_succeeded(self):
        return self._notify_succeeded

    @notify_succeeded.setter
    def notify_succeeded(self, value):
        self._notify_succeeded = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_info:
            if hasattr(self.error_info, 'to_alipay_dict'):
                params['error_info'] = self.error_info.to_alipay_dict()
            else:
                params['error_info'] = self.error_info
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.mq_key:
            if hasattr(self.mq_key, 'to_alipay_dict'):
                params['mq_key'] = self.mq_key.to_alipay_dict()
            else:
                params['mq_key'] = self.mq_key
        if self.notify_succeeded:
            if hasattr(self.notify_succeeded, 'to_alipay_dict'):
                params['notify_succeeded'] = self.notify_succeeded.to_alipay_dict()
            else:
                params['notify_succeeded'] = self.notify_succeeded
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceCallbackOpenApiOrder()
        if 'error_info' in d:
            o.error_info = d['error_info']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'mq_key' in d:
            o.mq_key = d['mq_key']
        if 'notify_succeeded' in d:
            o.notify_succeeded = d['notify_succeeded']
        return o


