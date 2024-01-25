#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceAuditInfo(object):

    def __init__(self):
        self._invoice_audit_remark = None
        self._invoice_audit_status = None
        self._invoice_id = None
        self._invoice_out_no = None

    @property
    def invoice_audit_remark(self):
        return self._invoice_audit_remark

    @invoice_audit_remark.setter
    def invoice_audit_remark(self, value):
        self._invoice_audit_remark = value
    @property
    def invoice_audit_status(self):
        return self._invoice_audit_status

    @invoice_audit_status.setter
    def invoice_audit_status(self, value):
        self._invoice_audit_status = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_out_no(self):
        return self._invoice_out_no

    @invoice_out_no.setter
    def invoice_out_no(self, value):
        self._invoice_out_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_audit_remark:
            if hasattr(self.invoice_audit_remark, 'to_alipay_dict'):
                params['invoice_audit_remark'] = self.invoice_audit_remark.to_alipay_dict()
            else:
                params['invoice_audit_remark'] = self.invoice_audit_remark
        if self.invoice_audit_status:
            if hasattr(self.invoice_audit_status, 'to_alipay_dict'):
                params['invoice_audit_status'] = self.invoice_audit_status.to_alipay_dict()
            else:
                params['invoice_audit_status'] = self.invoice_audit_status
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_out_no:
            if hasattr(self.invoice_out_no, 'to_alipay_dict'):
                params['invoice_out_no'] = self.invoice_out_no.to_alipay_dict()
            else:
                params['invoice_out_no'] = self.invoice_out_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceAuditInfo()
        if 'invoice_audit_remark' in d:
            o.invoice_audit_remark = d['invoice_audit_remark']
        if 'invoice_audit_status' in d:
            o.invoice_audit_status = d['invoice_audit_status']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_out_no' in d:
            o.invoice_out_no = d['invoice_out_no']
        return o


