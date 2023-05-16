#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasInsuranceAccidentriskQueryModel(object):

    def __init__(self):
        self._applicant_cert_no = None
        self._assess_priority = None
        self._auth_agreement = None
        self._biz_id = None
        self._insured_amt = None
        self._insured_cert_no = None
        self._product_code = None
        self._profession_level = None

    @property
    def applicant_cert_no(self):
        return self._applicant_cert_no

    @applicant_cert_no.setter
    def applicant_cert_no(self, value):
        self._applicant_cert_no = value
    @property
    def assess_priority(self):
        return self._assess_priority

    @assess_priority.setter
    def assess_priority(self, value):
        self._assess_priority = value
    @property
    def auth_agreement(self):
        return self._auth_agreement

    @auth_agreement.setter
    def auth_agreement(self, value):
        self._auth_agreement = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def insured_amt(self):
        return self._insured_amt

    @insured_amt.setter
    def insured_amt(self, value):
        self._insured_amt = value
    @property
    def insured_cert_no(self):
        return self._insured_cert_no

    @insured_cert_no.setter
    def insured_cert_no(self, value):
        self._insured_cert_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def profession_level(self):
        return self._profession_level

    @profession_level.setter
    def profession_level(self, value):
        self._profession_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant_cert_no:
            if hasattr(self.applicant_cert_no, 'to_alipay_dict'):
                params['applicant_cert_no'] = self.applicant_cert_no.to_alipay_dict()
            else:
                params['applicant_cert_no'] = self.applicant_cert_no
        if self.assess_priority:
            if hasattr(self.assess_priority, 'to_alipay_dict'):
                params['assess_priority'] = self.assess_priority.to_alipay_dict()
            else:
                params['assess_priority'] = self.assess_priority
        if self.auth_agreement:
            if hasattr(self.auth_agreement, 'to_alipay_dict'):
                params['auth_agreement'] = self.auth_agreement.to_alipay_dict()
            else:
                params['auth_agreement'] = self.auth_agreement
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.insured_amt:
            if hasattr(self.insured_amt, 'to_alipay_dict'):
                params['insured_amt'] = self.insured_amt.to_alipay_dict()
            else:
                params['insured_amt'] = self.insured_amt
        if self.insured_cert_no:
            if hasattr(self.insured_cert_no, 'to_alipay_dict'):
                params['insured_cert_no'] = self.insured_cert_no.to_alipay_dict()
            else:
                params['insured_cert_no'] = self.insured_cert_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.profession_level:
            if hasattr(self.profession_level, 'to_alipay_dict'):
                params['profession_level'] = self.profession_level.to_alipay_dict()
            else:
                params['profession_level'] = self.profession_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasInsuranceAccidentriskQueryModel()
        if 'applicant_cert_no' in d:
            o.applicant_cert_no = d['applicant_cert_no']
        if 'assess_priority' in d:
            o.assess_priority = d['assess_priority']
        if 'auth_agreement' in d:
            o.auth_agreement = d['auth_agreement']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'insured_amt' in d:
            o.insured_amt = d['insured_amt']
        if 'insured_cert_no' in d:
            o.insured_cert_no = d['insured_cert_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'profession_level' in d:
            o.profession_level = d['profession_level']
        return o


