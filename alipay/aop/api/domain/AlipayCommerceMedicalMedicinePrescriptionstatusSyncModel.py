#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedicinePrescriptionstatusSyncModel(object):

    def __init__(self):
        self._checker_hand_signature_url = None
        self._checker_name = None
        self._ext_prescription_code = None
        self._inquiry_id = None
        self._platform_code = None
        self._prescription_status = None
        self._reason = None

    @property
    def checker_hand_signature_url(self):
        return self._checker_hand_signature_url

    @checker_hand_signature_url.setter
    def checker_hand_signature_url(self, value):
        self._checker_hand_signature_url = value
    @property
    def checker_name(self):
        return self._checker_name

    @checker_name.setter
    def checker_name(self, value):
        self._checker_name = value
    @property
    def ext_prescription_code(self):
        return self._ext_prescription_code

    @ext_prescription_code.setter
    def ext_prescription_code(self, value):
        self._ext_prescription_code = value
    @property
    def inquiry_id(self):
        return self._inquiry_id

    @inquiry_id.setter
    def inquiry_id(self, value):
        self._inquiry_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def prescription_status(self):
        return self._prescription_status

    @prescription_status.setter
    def prescription_status(self, value):
        self._prescription_status = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.checker_hand_signature_url:
            if hasattr(self.checker_hand_signature_url, 'to_alipay_dict'):
                params['checker_hand_signature_url'] = self.checker_hand_signature_url.to_alipay_dict()
            else:
                params['checker_hand_signature_url'] = self.checker_hand_signature_url
        if self.checker_name:
            if hasattr(self.checker_name, 'to_alipay_dict'):
                params['checker_name'] = self.checker_name.to_alipay_dict()
            else:
                params['checker_name'] = self.checker_name
        if self.ext_prescription_code:
            if hasattr(self.ext_prescription_code, 'to_alipay_dict'):
                params['ext_prescription_code'] = self.ext_prescription_code.to_alipay_dict()
            else:
                params['ext_prescription_code'] = self.ext_prescription_code
        if self.inquiry_id:
            if hasattr(self.inquiry_id, 'to_alipay_dict'):
                params['inquiry_id'] = self.inquiry_id.to_alipay_dict()
            else:
                params['inquiry_id'] = self.inquiry_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.prescription_status:
            if hasattr(self.prescription_status, 'to_alipay_dict'):
                params['prescription_status'] = self.prescription_status.to_alipay_dict()
            else:
                params['prescription_status'] = self.prescription_status
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedicinePrescriptionstatusSyncModel()
        if 'checker_hand_signature_url' in d:
            o.checker_hand_signature_url = d['checker_hand_signature_url']
        if 'checker_name' in d:
            o.checker_name = d['checker_name']
        if 'ext_prescription_code' in d:
            o.ext_prescription_code = d['ext_prescription_code']
        if 'inquiry_id' in d:
            o.inquiry_id = d['inquiry_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'prescription_status' in d:
            o.prescription_status = d['prescription_status']
        if 'reason' in d:
            o.reason = d['reason']
        return o


