#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementTemplate import AgreementTemplate


class AlipayCommerceMedicalAgreementsignCreateModel(object):

    def __init__(self):
        self._agreement_signing_time = None
        self._agreement_template_list = None
        self._app_code = None
        self._doctor_id = None
        self._signing_alipay_user_id = None
        self._signing_cert_no = None
        self._signing_name = None
        self._signing_phone_no = None

    @property
    def agreement_signing_time(self):
        return self._agreement_signing_time

    @agreement_signing_time.setter
    def agreement_signing_time(self, value):
        self._agreement_signing_time = value
    @property
    def agreement_template_list(self):
        return self._agreement_template_list

    @agreement_template_list.setter
    def agreement_template_list(self, value):
        if isinstance(value, list):
            self._agreement_template_list = list()
            for i in value:
                if isinstance(i, AgreementTemplate):
                    self._agreement_template_list.append(i)
                else:
                    self._agreement_template_list.append(AgreementTemplate.from_alipay_dict(i))
    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def signing_alipay_user_id(self):
        return self._signing_alipay_user_id

    @signing_alipay_user_id.setter
    def signing_alipay_user_id(self, value):
        self._signing_alipay_user_id = value
    @property
    def signing_cert_no(self):
        return self._signing_cert_no

    @signing_cert_no.setter
    def signing_cert_no(self, value):
        self._signing_cert_no = value
    @property
    def signing_name(self):
        return self._signing_name

    @signing_name.setter
    def signing_name(self, value):
        self._signing_name = value
    @property
    def signing_phone_no(self):
        return self._signing_phone_no

    @signing_phone_no.setter
    def signing_phone_no(self, value):
        self._signing_phone_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_signing_time:
            if hasattr(self.agreement_signing_time, 'to_alipay_dict'):
                params['agreement_signing_time'] = self.agreement_signing_time.to_alipay_dict()
            else:
                params['agreement_signing_time'] = self.agreement_signing_time
        if self.agreement_template_list:
            if isinstance(self.agreement_template_list, list):
                for i in range(0, len(self.agreement_template_list)):
                    element = self.agreement_template_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agreement_template_list[i] = element.to_alipay_dict()
            if hasattr(self.agreement_template_list, 'to_alipay_dict'):
                params['agreement_template_list'] = self.agreement_template_list.to_alipay_dict()
            else:
                params['agreement_template_list'] = self.agreement_template_list
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.signing_alipay_user_id:
            if hasattr(self.signing_alipay_user_id, 'to_alipay_dict'):
                params['signing_alipay_user_id'] = self.signing_alipay_user_id.to_alipay_dict()
            else:
                params['signing_alipay_user_id'] = self.signing_alipay_user_id
        if self.signing_cert_no:
            if hasattr(self.signing_cert_no, 'to_alipay_dict'):
                params['signing_cert_no'] = self.signing_cert_no.to_alipay_dict()
            else:
                params['signing_cert_no'] = self.signing_cert_no
        if self.signing_name:
            if hasattr(self.signing_name, 'to_alipay_dict'):
                params['signing_name'] = self.signing_name.to_alipay_dict()
            else:
                params['signing_name'] = self.signing_name
        if self.signing_phone_no:
            if hasattr(self.signing_phone_no, 'to_alipay_dict'):
                params['signing_phone_no'] = self.signing_phone_no.to_alipay_dict()
            else:
                params['signing_phone_no'] = self.signing_phone_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAgreementsignCreateModel()
        if 'agreement_signing_time' in d:
            o.agreement_signing_time = d['agreement_signing_time']
        if 'agreement_template_list' in d:
            o.agreement_template_list = d['agreement_template_list']
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'signing_alipay_user_id' in d:
            o.signing_alipay_user_id = d['signing_alipay_user_id']
        if 'signing_cert_no' in d:
            o.signing_cert_no = d['signing_cert_no']
        if 'signing_name' in d:
            o.signing_name = d['signing_name']
        if 'signing_phone_no' in d:
            o.signing_phone_no = d['signing_phone_no']
        return o


