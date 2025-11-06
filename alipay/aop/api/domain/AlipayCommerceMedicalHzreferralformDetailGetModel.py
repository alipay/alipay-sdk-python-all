#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHzreferralformDetailGetModel(object):

    def __init__(self):
        self._doctor_cert_no = None
        self._referral_form_id = None

    @property
    def doctor_cert_no(self):
        return self._doctor_cert_no

    @doctor_cert_no.setter
    def doctor_cert_no(self, value):
        self._doctor_cert_no = value
    @property
    def referral_form_id(self):
        return self._referral_form_id

    @referral_form_id.setter
    def referral_form_id(self, value):
        self._referral_form_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_cert_no:
            if hasattr(self.doctor_cert_no, 'to_alipay_dict'):
                params['doctor_cert_no'] = self.doctor_cert_no.to_alipay_dict()
            else:
                params['doctor_cert_no'] = self.doctor_cert_no
        if self.referral_form_id:
            if hasattr(self.referral_form_id, 'to_alipay_dict'):
                params['referral_form_id'] = self.referral_form_id.to_alipay_dict()
            else:
                params['referral_form_id'] = self.referral_form_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHzreferralformDetailGetModel()
        if 'doctor_cert_no' in d:
            o.doctor_cert_no = d['doctor_cert_no']
        if 'referral_form_id' in d:
            o.referral_form_id = d['referral_form_id']
        return o


