#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommercialInsuranceParams import CommercialInsuranceParams


class AlipayCommerceMedicalPaymentPreconsultModel(object):

    def __init__(self):
        self._amount = None
        self._business_scene = None
        self._callback_url = None
        self._commercial_insurance_params = None
        self._drug_store_tag = None
        self._payment_city_code = None
        self._user_cert_no = None
        self._user_cert_type = None
        self._user_mobile_no = None
        self._user_name = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def business_scene(self):
        return self._business_scene

    @business_scene.setter
    def business_scene(self, value):
        self._business_scene = value
    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def commercial_insurance_params(self):
        return self._commercial_insurance_params

    @commercial_insurance_params.setter
    def commercial_insurance_params(self, value):
        if isinstance(value, CommercialInsuranceParams):
            self._commercial_insurance_params = value
        else:
            self._commercial_insurance_params = CommercialInsuranceParams.from_alipay_dict(value)
    @property
    def drug_store_tag(self):
        return self._drug_store_tag

    @drug_store_tag.setter
    def drug_store_tag(self, value):
        self._drug_store_tag = value
    @property
    def payment_city_code(self):
        return self._payment_city_code

    @payment_city_code.setter
    def payment_city_code(self, value):
        self._payment_city_code = value
    @property
    def user_cert_no(self):
        return self._user_cert_no

    @user_cert_no.setter
    def user_cert_no(self, value):
        self._user_cert_no = value
    @property
    def user_cert_type(self):
        return self._user_cert_type

    @user_cert_type.setter
    def user_cert_type(self, value):
        self._user_cert_type = value
    @property
    def user_mobile_no(self):
        return self._user_mobile_no

    @user_mobile_no.setter
    def user_mobile_no(self, value):
        self._user_mobile_no = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.business_scene:
            if hasattr(self.business_scene, 'to_alipay_dict'):
                params['business_scene'] = self.business_scene.to_alipay_dict()
            else:
                params['business_scene'] = self.business_scene
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.commercial_insurance_params:
            if hasattr(self.commercial_insurance_params, 'to_alipay_dict'):
                params['commercial_insurance_params'] = self.commercial_insurance_params.to_alipay_dict()
            else:
                params['commercial_insurance_params'] = self.commercial_insurance_params
        if self.drug_store_tag:
            if hasattr(self.drug_store_tag, 'to_alipay_dict'):
                params['drug_store_tag'] = self.drug_store_tag.to_alipay_dict()
            else:
                params['drug_store_tag'] = self.drug_store_tag
        if self.payment_city_code:
            if hasattr(self.payment_city_code, 'to_alipay_dict'):
                params['payment_city_code'] = self.payment_city_code.to_alipay_dict()
            else:
                params['payment_city_code'] = self.payment_city_code
        if self.user_cert_no:
            if hasattr(self.user_cert_no, 'to_alipay_dict'):
                params['user_cert_no'] = self.user_cert_no.to_alipay_dict()
            else:
                params['user_cert_no'] = self.user_cert_no
        if self.user_cert_type:
            if hasattr(self.user_cert_type, 'to_alipay_dict'):
                params['user_cert_type'] = self.user_cert_type.to_alipay_dict()
            else:
                params['user_cert_type'] = self.user_cert_type
        if self.user_mobile_no:
            if hasattr(self.user_mobile_no, 'to_alipay_dict'):
                params['user_mobile_no'] = self.user_mobile_no.to_alipay_dict()
            else:
                params['user_mobile_no'] = self.user_mobile_no
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalPaymentPreconsultModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'business_scene' in d:
            o.business_scene = d['business_scene']
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'commercial_insurance_params' in d:
            o.commercial_insurance_params = d['commercial_insurance_params']
        if 'drug_store_tag' in d:
            o.drug_store_tag = d['drug_store_tag']
        if 'payment_city_code' in d:
            o.payment_city_code = d['payment_city_code']
        if 'user_cert_no' in d:
            o.user_cert_no = d['user_cert_no']
        if 'user_cert_type' in d:
            o.user_cert_type = d['user_cert_type']
        if 'user_mobile_no' in d:
            o.user_mobile_no = d['user_mobile_no']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


