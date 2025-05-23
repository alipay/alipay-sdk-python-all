#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPrescriptionPdfModifyModel(object):

    def __init__(self):
        self._prescription_id = None
        self._signed_prsc_pdf_url = None
        self._store_code = None

    @property
    def prescription_id(self):
        return self._prescription_id

    @prescription_id.setter
    def prescription_id(self, value):
        self._prescription_id = value
    @property
    def signed_prsc_pdf_url(self):
        return self._signed_prsc_pdf_url

    @signed_prsc_pdf_url.setter
    def signed_prsc_pdf_url(self, value):
        self._signed_prsc_pdf_url = value
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.prescription_id:
            if hasattr(self.prescription_id, 'to_alipay_dict'):
                params['prescription_id'] = self.prescription_id.to_alipay_dict()
            else:
                params['prescription_id'] = self.prescription_id
        if self.signed_prsc_pdf_url:
            if hasattr(self.signed_prsc_pdf_url, 'to_alipay_dict'):
                params['signed_prsc_pdf_url'] = self.signed_prsc_pdf_url.to_alipay_dict()
            else:
                params['signed_prsc_pdf_url'] = self.signed_prsc_pdf_url
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalPrescriptionPdfModifyModel()
        if 'prescription_id' in d:
            o.prescription_id = d['prescription_id']
        if 'signed_prsc_pdf_url' in d:
            o.signed_prsc_pdf_url = d['signed_prsc_pdf_url']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


