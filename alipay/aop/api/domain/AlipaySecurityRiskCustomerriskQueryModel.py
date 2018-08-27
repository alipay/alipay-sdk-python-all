#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskCustomerriskQueryModel(object):

    def __init__(self):
        self._bank_card_no = None
        self._business_license_no = None
        self._card_no = None
        self._cert_no = None
        self._company_name = None
        self._external_id = None
        self._mobile_no = None
        self._risk_type = None

    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = self.business_license_no.to_alipay_dict()
            else:
                params['business_license_no'] = self.business_license_no
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskCustomerriskQueryModel()
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'business_license_no' in d:
            o.business_license_no = d['business_license_no']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        return o


