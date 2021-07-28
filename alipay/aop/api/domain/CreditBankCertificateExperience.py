#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditBankCertificateExperience(object):

    def __init__(self):
        self._cert_exp_outer_id = None
        self._certificate_level = None
        self._certificate_name = None
        self._experience_time = None
        self._inst_name = None

    @property
    def cert_exp_outer_id(self):
        return self._cert_exp_outer_id

    @cert_exp_outer_id.setter
    def cert_exp_outer_id(self, value):
        self._cert_exp_outer_id = value
    @property
    def certificate_level(self):
        return self._certificate_level

    @certificate_level.setter
    def certificate_level(self, value):
        self._certificate_level = value
    @property
    def certificate_name(self):
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, value):
        self._certificate_name = value
    @property
    def experience_time(self):
        return self._experience_time

    @experience_time.setter
    def experience_time(self, value):
        self._experience_time = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_exp_outer_id:
            if hasattr(self.cert_exp_outer_id, 'to_alipay_dict'):
                params['cert_exp_outer_id'] = self.cert_exp_outer_id.to_alipay_dict()
            else:
                params['cert_exp_outer_id'] = self.cert_exp_outer_id
        if self.certificate_level:
            if hasattr(self.certificate_level, 'to_alipay_dict'):
                params['certificate_level'] = self.certificate_level.to_alipay_dict()
            else:
                params['certificate_level'] = self.certificate_level
        if self.certificate_name:
            if hasattr(self.certificate_name, 'to_alipay_dict'):
                params['certificate_name'] = self.certificate_name.to_alipay_dict()
            else:
                params['certificate_name'] = self.certificate_name
        if self.experience_time:
            if hasattr(self.experience_time, 'to_alipay_dict'):
                params['experience_time'] = self.experience_time.to_alipay_dict()
            else:
                params['experience_time'] = self.experience_time
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditBankCertificateExperience()
        if 'cert_exp_outer_id' in d:
            o.cert_exp_outer_id = d['cert_exp_outer_id']
        if 'certificate_level' in d:
            o.certificate_level = d['certificate_level']
        if 'certificate_name' in d:
            o.certificate_name = d['certificate_name']
        if 'experience_time' in d:
            o.experience_time = d['experience_time']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        return o


