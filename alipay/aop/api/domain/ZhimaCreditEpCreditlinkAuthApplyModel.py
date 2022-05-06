#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TaxReceiptOnceInfo import TaxReceiptOnceInfo


class ZhimaCreditEpCreditlinkAuthApplyModel(object):

    def __init__(self):
        self._auth_callback_path = None
        self._auth_merchant_id = None
        self._auth_notify_path = None
        self._cognizant_cert_no = None
        self._cognizant_name = None
        self._data_type = None
        self._ep_cert_no = None
        self._ep_name = None
        self._link_type = None
        self._merchant_context = None
        self._merchant_request_id = None
        self._tax_receipt_once_info = None

    @property
    def auth_callback_path(self):
        return self._auth_callback_path

    @auth_callback_path.setter
    def auth_callback_path(self, value):
        self._auth_callback_path = value
    @property
    def auth_merchant_id(self):
        return self._auth_merchant_id

    @auth_merchant_id.setter
    def auth_merchant_id(self, value):
        self._auth_merchant_id = value
    @property
    def auth_notify_path(self):
        return self._auth_notify_path

    @auth_notify_path.setter
    def auth_notify_path(self, value):
        self._auth_notify_path = value
    @property
    def cognizant_cert_no(self):
        return self._cognizant_cert_no

    @cognizant_cert_no.setter
    def cognizant_cert_no(self, value):
        self._cognizant_cert_no = value
    @property
    def cognizant_name(self):
        return self._cognizant_name

    @cognizant_name.setter
    def cognizant_name(self, value):
        self._cognizant_name = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def link_type(self):
        return self._link_type

    @link_type.setter
    def link_type(self, value):
        self._link_type = value
    @property
    def merchant_context(self):
        return self._merchant_context

    @merchant_context.setter
    def merchant_context(self, value):
        self._merchant_context = value
    @property
    def merchant_request_id(self):
        return self._merchant_request_id

    @merchant_request_id.setter
    def merchant_request_id(self, value):
        self._merchant_request_id = value
    @property
    def tax_receipt_once_info(self):
        return self._tax_receipt_once_info

    @tax_receipt_once_info.setter
    def tax_receipt_once_info(self, value):
        if isinstance(value, TaxReceiptOnceInfo):
            self._tax_receipt_once_info = value
        else:
            self._tax_receipt_once_info = TaxReceiptOnceInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.auth_callback_path:
            if hasattr(self.auth_callback_path, 'to_alipay_dict'):
                params['auth_callback_path'] = self.auth_callback_path.to_alipay_dict()
            else:
                params['auth_callback_path'] = self.auth_callback_path
        if self.auth_merchant_id:
            if hasattr(self.auth_merchant_id, 'to_alipay_dict'):
                params['auth_merchant_id'] = self.auth_merchant_id.to_alipay_dict()
            else:
                params['auth_merchant_id'] = self.auth_merchant_id
        if self.auth_notify_path:
            if hasattr(self.auth_notify_path, 'to_alipay_dict'):
                params['auth_notify_path'] = self.auth_notify_path.to_alipay_dict()
            else:
                params['auth_notify_path'] = self.auth_notify_path
        if self.cognizant_cert_no:
            if hasattr(self.cognizant_cert_no, 'to_alipay_dict'):
                params['cognizant_cert_no'] = self.cognizant_cert_no.to_alipay_dict()
            else:
                params['cognizant_cert_no'] = self.cognizant_cert_no
        if self.cognizant_name:
            if hasattr(self.cognizant_name, 'to_alipay_dict'):
                params['cognizant_name'] = self.cognizant_name.to_alipay_dict()
            else:
                params['cognizant_name'] = self.cognizant_name
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.link_type:
            if hasattr(self.link_type, 'to_alipay_dict'):
                params['link_type'] = self.link_type.to_alipay_dict()
            else:
                params['link_type'] = self.link_type
        if self.merchant_context:
            if hasattr(self.merchant_context, 'to_alipay_dict'):
                params['merchant_context'] = self.merchant_context.to_alipay_dict()
            else:
                params['merchant_context'] = self.merchant_context
        if self.merchant_request_id:
            if hasattr(self.merchant_request_id, 'to_alipay_dict'):
                params['merchant_request_id'] = self.merchant_request_id.to_alipay_dict()
            else:
                params['merchant_request_id'] = self.merchant_request_id
        if self.tax_receipt_once_info:
            if hasattr(self.tax_receipt_once_info, 'to_alipay_dict'):
                params['tax_receipt_once_info'] = self.tax_receipt_once_info.to_alipay_dict()
            else:
                params['tax_receipt_once_info'] = self.tax_receipt_once_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCreditlinkAuthApplyModel()
        if 'auth_callback_path' in d:
            o.auth_callback_path = d['auth_callback_path']
        if 'auth_merchant_id' in d:
            o.auth_merchant_id = d['auth_merchant_id']
        if 'auth_notify_path' in d:
            o.auth_notify_path = d['auth_notify_path']
        if 'cognizant_cert_no' in d:
            o.cognizant_cert_no = d['cognizant_cert_no']
        if 'cognizant_name' in d:
            o.cognizant_name = d['cognizant_name']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'link_type' in d:
            o.link_type = d['link_type']
        if 'merchant_context' in d:
            o.merchant_context = d['merchant_context']
        if 'merchant_request_id' in d:
            o.merchant_request_id = d['merchant_request_id']
        if 'tax_receipt_once_info' in d:
            o.tax_receipt_once_info = d['tax_receipt_once_info']
        return o


