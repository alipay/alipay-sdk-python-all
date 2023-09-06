#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ErrorInfoDTO import ErrorInfoDTO


class InputInvoiceCallbackOpenApiDTO(object):

    def __init__(self):
        self._callback_type = None
        self._error_info_dto = None
        self._invoice_id = None
        self._mq_key = None
        self._notify_succeeded = None
        self._platform_code = None
        self._request_no = None

    @property
    def callback_type(self):
        return self._callback_type

    @callback_type.setter
    def callback_type(self, value):
        self._callback_type = value
    @property
    def error_info_dto(self):
        return self._error_info_dto

    @error_info_dto.setter
    def error_info_dto(self, value):
        if isinstance(value, ErrorInfoDTO):
            self._error_info_dto = value
        else:
            self._error_info_dto = ErrorInfoDTO.from_alipay_dict(value)
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
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.callback_type:
            if hasattr(self.callback_type, 'to_alipay_dict'):
                params['callback_type'] = self.callback_type.to_alipay_dict()
            else:
                params['callback_type'] = self.callback_type
        if self.error_info_dto:
            if hasattr(self.error_info_dto, 'to_alipay_dict'):
                params['error_info_dto'] = self.error_info_dto.to_alipay_dict()
            else:
                params['error_info_dto'] = self.error_info_dto
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
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceCallbackOpenApiDTO()
        if 'callback_type' in d:
            o.callback_type = d['callback_type']
        if 'error_info_dto' in d:
            o.error_info_dto = d['error_info_dto']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'mq_key' in d:
            o.mq_key = d['mq_key']
        if 'notify_succeeded' in d:
            o.notify_succeeded = d['notify_succeeded']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'request_no' in d:
            o.request_no = d['request_no']
        return o


