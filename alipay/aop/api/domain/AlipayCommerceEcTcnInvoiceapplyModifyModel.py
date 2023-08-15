#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcTcnInvoiceapplyModifyModel(object):

    def __init__(self):
        self._apply_id = None
        self._apply_status = None
        self._failed_reason = None
        self._logistics_company_code = None
        self._logistics_no = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def failed_reason(self):
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, value):
        self._failed_reason = value
    @property
    def logistics_company_code(self):
        return self._logistics_company_code

    @logistics_company_code.setter
    def logistics_company_code(self, value):
        self._logistics_company_code = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.failed_reason:
            if hasattr(self.failed_reason, 'to_alipay_dict'):
                params['failed_reason'] = self.failed_reason.to_alipay_dict()
            else:
                params['failed_reason'] = self.failed_reason
        if self.logistics_company_code:
            if hasattr(self.logistics_company_code, 'to_alipay_dict'):
                params['logistics_company_code'] = self.logistics_company_code.to_alipay_dict()
            else:
                params['logistics_company_code'] = self.logistics_company_code
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcTcnInvoiceapplyModifyModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'failed_reason' in d:
            o.failed_reason = d['failed_reason']
        if 'logistics_company_code' in d:
            o.logistics_company_code = d['logistics_company_code']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        return o


