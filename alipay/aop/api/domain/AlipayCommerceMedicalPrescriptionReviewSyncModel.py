#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPrescriptionReviewSyncModel(object):

    def __init__(self):
        self._pharmacist_code = None
        self._prescription_code = None
        self._prescription_id = None
        self._reject_reason = None
        self._review_result = None
        self._store_code = None

    @property
    def pharmacist_code(self):
        return self._pharmacist_code

    @pharmacist_code.setter
    def pharmacist_code(self, value):
        self._pharmacist_code = value
    @property
    def prescription_code(self):
        return self._prescription_code

    @prescription_code.setter
    def prescription_code(self, value):
        self._prescription_code = value
    @property
    def prescription_id(self):
        return self._prescription_id

    @prescription_id.setter
    def prescription_id(self, value):
        self._prescription_id = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def review_result(self):
        return self._review_result

    @review_result.setter
    def review_result(self, value):
        self._review_result = value
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.pharmacist_code:
            if hasattr(self.pharmacist_code, 'to_alipay_dict'):
                params['pharmacist_code'] = self.pharmacist_code.to_alipay_dict()
            else:
                params['pharmacist_code'] = self.pharmacist_code
        if self.prescription_code:
            if hasattr(self.prescription_code, 'to_alipay_dict'):
                params['prescription_code'] = self.prescription_code.to_alipay_dict()
            else:
                params['prescription_code'] = self.prescription_code
        if self.prescription_id:
            if hasattr(self.prescription_id, 'to_alipay_dict'):
                params['prescription_id'] = self.prescription_id.to_alipay_dict()
            else:
                params['prescription_id'] = self.prescription_id
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.review_result:
            if hasattr(self.review_result, 'to_alipay_dict'):
                params['review_result'] = self.review_result.to_alipay_dict()
            else:
                params['review_result'] = self.review_result
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
        o = AlipayCommerceMedicalPrescriptionReviewSyncModel()
        if 'pharmacist_code' in d:
            o.pharmacist_code = d['pharmacist_code']
        if 'prescription_code' in d:
            o.prescription_code = d['prescription_code']
        if 'prescription_id' in d:
            o.prescription_id = d['prescription_id']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'review_result' in d:
            o.review_result = d['review_result']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


