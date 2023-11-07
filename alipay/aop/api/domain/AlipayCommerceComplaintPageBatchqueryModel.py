#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceComplaintPageBatchqueryModel(object):

    def __init__(self):
        self._complaint_status = None
        self._complaint_type = None
        self._merchant_name = None
        self._page_num = None
        self._page_size = None

    @property
    def complaint_status(self):
        return self._complaint_status

    @complaint_status.setter
    def complaint_status(self, value):
        self._complaint_status = value
    @property
    def complaint_type(self):
        return self._complaint_type

    @complaint_type.setter
    def complaint_type(self, value):
        self._complaint_type = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.complaint_status:
            if hasattr(self.complaint_status, 'to_alipay_dict'):
                params['complaint_status'] = self.complaint_status.to_alipay_dict()
            else:
                params['complaint_status'] = self.complaint_status
        if self.complaint_type:
            if hasattr(self.complaint_type, 'to_alipay_dict'):
                params['complaint_type'] = self.complaint_type.to_alipay_dict()
            else:
                params['complaint_type'] = self.complaint_type
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceComplaintPageBatchqueryModel()
        if 'complaint_status' in d:
            o.complaint_status = d['complaint_status']
        if 'complaint_type' in d:
            o.complaint_type = d['complaint_type']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


