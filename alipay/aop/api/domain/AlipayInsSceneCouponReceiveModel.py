#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsCertificate import InsCertificate
from alipay.aop.api.domain.InsPerson import InsPerson


class AlipayInsSceneCouponReceiveModel(object):

    def __init__(self):
        self._applicant = None
        self._certificate = None
        self._insured = None
        self._market_type = None
        self._out_biz_no = None
        self._partner_id = None
        self._prod_code = None
        self._prod_version = None
        self._service_scenario = None

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, InsPerson):
            self._applicant = value
        else:
            self._applicant = InsPerson.from_alipay_dict(value)
    @property
    def certificate(self):
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        if isinstance(value, InsCertificate):
            self._certificate = value
        else:
            self._certificate = InsCertificate.from_alipay_dict(value)
    @property
    def insured(self):
        return self._insured

    @insured.setter
    def insured(self, value):
        if isinstance(value, InsPerson):
            self._insured = value
        else:
            self._insured = InsPerson.from_alipay_dict(value)
    @property
    def market_type(self):
        return self._market_type

    @market_type.setter
    def market_type(self, value):
        self._market_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def prod_version(self):
        return self._prod_version

    @prod_version.setter
    def prod_version(self, value):
        self._prod_version = value
    @property
    def service_scenario(self):
        return self._service_scenario

    @service_scenario.setter
    def service_scenario(self, value):
        self._service_scenario = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.certificate:
            if hasattr(self.certificate, 'to_alipay_dict'):
                params['certificate'] = self.certificate.to_alipay_dict()
            else:
                params['certificate'] = self.certificate
        if self.insured:
            if hasattr(self.insured, 'to_alipay_dict'):
                params['insured'] = self.insured.to_alipay_dict()
            else:
                params['insured'] = self.insured
        if self.market_type:
            if hasattr(self.market_type, 'to_alipay_dict'):
                params['market_type'] = self.market_type.to_alipay_dict()
            else:
                params['market_type'] = self.market_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.prod_version:
            if hasattr(self.prod_version, 'to_alipay_dict'):
                params['prod_version'] = self.prod_version.to_alipay_dict()
            else:
                params['prod_version'] = self.prod_version
        if self.service_scenario:
            if hasattr(self.service_scenario, 'to_alipay_dict'):
                params['service_scenario'] = self.service_scenario.to_alipay_dict()
            else:
                params['service_scenario'] = self.service_scenario
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneCouponReceiveModel()
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'certificate' in d:
            o.certificate = d['certificate']
        if 'insured' in d:
            o.insured = d['insured']
        if 'market_type' in d:
            o.market_type = d['market_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'prod_version' in d:
            o.prod_version = d['prod_version']
        if 'service_scenario' in d:
            o.service_scenario = d['service_scenario']
        return o


