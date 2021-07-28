#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EsignResult(object):

    def __init__(self):
        self._agreement_url = None
        self._apply_dutiable_mode_enum = None
        self._contractor_code = None
        self._contractor_name = None
        self._employer_code = None
        self._identification_in_belonging_employer = None
        self._pay_salary_mode_enum = None
        self._sign_time = None
        self._status = None
        self._tax_optimization_mode = None
        self._termination_time = None

    @property
    def agreement_url(self):
        return self._agreement_url

    @agreement_url.setter
    def agreement_url(self, value):
        self._agreement_url = value
    @property
    def apply_dutiable_mode_enum(self):
        return self._apply_dutiable_mode_enum

    @apply_dutiable_mode_enum.setter
    def apply_dutiable_mode_enum(self, value):
        self._apply_dutiable_mode_enum = value
    @property
    def contractor_code(self):
        return self._contractor_code

    @contractor_code.setter
    def contractor_code(self, value):
        self._contractor_code = value
    @property
    def contractor_name(self):
        return self._contractor_name

    @contractor_name.setter
    def contractor_name(self, value):
        self._contractor_name = value
    @property
    def employer_code(self):
        return self._employer_code

    @employer_code.setter
    def employer_code(self, value):
        self._employer_code = value
    @property
    def identification_in_belonging_employer(self):
        return self._identification_in_belonging_employer

    @identification_in_belonging_employer.setter
    def identification_in_belonging_employer(self, value):
        self._identification_in_belonging_employer = value
    @property
    def pay_salary_mode_enum(self):
        return self._pay_salary_mode_enum

    @pay_salary_mode_enum.setter
    def pay_salary_mode_enum(self, value):
        self._pay_salary_mode_enum = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tax_optimization_mode(self):
        return self._tax_optimization_mode

    @tax_optimization_mode.setter
    def tax_optimization_mode(self, value):
        self._tax_optimization_mode = value
    @property
    def termination_time(self):
        return self._termination_time

    @termination_time.setter
    def termination_time(self, value):
        self._termination_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_url:
            if hasattr(self.agreement_url, 'to_alipay_dict'):
                params['agreement_url'] = self.agreement_url.to_alipay_dict()
            else:
                params['agreement_url'] = self.agreement_url
        if self.apply_dutiable_mode_enum:
            if hasattr(self.apply_dutiable_mode_enum, 'to_alipay_dict'):
                params['apply_dutiable_mode_enum'] = self.apply_dutiable_mode_enum.to_alipay_dict()
            else:
                params['apply_dutiable_mode_enum'] = self.apply_dutiable_mode_enum
        if self.contractor_code:
            if hasattr(self.contractor_code, 'to_alipay_dict'):
                params['contractor_code'] = self.contractor_code.to_alipay_dict()
            else:
                params['contractor_code'] = self.contractor_code
        if self.contractor_name:
            if hasattr(self.contractor_name, 'to_alipay_dict'):
                params['contractor_name'] = self.contractor_name.to_alipay_dict()
            else:
                params['contractor_name'] = self.contractor_name
        if self.employer_code:
            if hasattr(self.employer_code, 'to_alipay_dict'):
                params['employer_code'] = self.employer_code.to_alipay_dict()
            else:
                params['employer_code'] = self.employer_code
        if self.identification_in_belonging_employer:
            if hasattr(self.identification_in_belonging_employer, 'to_alipay_dict'):
                params['identification_in_belonging_employer'] = self.identification_in_belonging_employer.to_alipay_dict()
            else:
                params['identification_in_belonging_employer'] = self.identification_in_belonging_employer
        if self.pay_salary_mode_enum:
            if hasattr(self.pay_salary_mode_enum, 'to_alipay_dict'):
                params['pay_salary_mode_enum'] = self.pay_salary_mode_enum.to_alipay_dict()
            else:
                params['pay_salary_mode_enum'] = self.pay_salary_mode_enum
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tax_optimization_mode:
            if hasattr(self.tax_optimization_mode, 'to_alipay_dict'):
                params['tax_optimization_mode'] = self.tax_optimization_mode.to_alipay_dict()
            else:
                params['tax_optimization_mode'] = self.tax_optimization_mode
        if self.termination_time:
            if hasattr(self.termination_time, 'to_alipay_dict'):
                params['termination_time'] = self.termination_time.to_alipay_dict()
            else:
                params['termination_time'] = self.termination_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EsignResult()
        if 'agreement_url' in d:
            o.agreement_url = d['agreement_url']
        if 'apply_dutiable_mode_enum' in d:
            o.apply_dutiable_mode_enum = d['apply_dutiable_mode_enum']
        if 'contractor_code' in d:
            o.contractor_code = d['contractor_code']
        if 'contractor_name' in d:
            o.contractor_name = d['contractor_name']
        if 'employer_code' in d:
            o.employer_code = d['employer_code']
        if 'identification_in_belonging_employer' in d:
            o.identification_in_belonging_employer = d['identification_in_belonging_employer']
        if 'pay_salary_mode_enum' in d:
            o.pay_salary_mode_enum = d['pay_salary_mode_enum']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'status' in d:
            o.status = d['status']
        if 'tax_optimization_mode' in d:
            o.tax_optimization_mode = d['tax_optimization_mode']
        if 'termination_time' in d:
            o.termination_time = d['termination_time']
        return o


