#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditBankTraining(object):

    def __init__(self):
        self._experience_time = None
        self._have_project_certificate = None
        self._inst_name = None
        self._project_name = None
        self._training_outer_id = None

    @property
    def experience_time(self):
        return self._experience_time

    @experience_time.setter
    def experience_time(self, value):
        self._experience_time = value
    @property
    def have_project_certificate(self):
        return self._have_project_certificate

    @have_project_certificate.setter
    def have_project_certificate(self, value):
        self._have_project_certificate = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def training_outer_id(self):
        return self._training_outer_id

    @training_outer_id.setter
    def training_outer_id(self, value):
        self._training_outer_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.experience_time:
            if hasattr(self.experience_time, 'to_alipay_dict'):
                params['experience_time'] = self.experience_time.to_alipay_dict()
            else:
                params['experience_time'] = self.experience_time
        if self.have_project_certificate:
            if hasattr(self.have_project_certificate, 'to_alipay_dict'):
                params['have_project_certificate'] = self.have_project_certificate.to_alipay_dict()
            else:
                params['have_project_certificate'] = self.have_project_certificate
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.training_outer_id:
            if hasattr(self.training_outer_id, 'to_alipay_dict'):
                params['training_outer_id'] = self.training_outer_id.to_alipay_dict()
            else:
                params['training_outer_id'] = self.training_outer_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditBankTraining()
        if 'experience_time' in d:
            o.experience_time = d['experience_time']
        if 'have_project_certificate' in d:
            o.have_project_certificate = d['have_project_certificate']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'training_outer_id' in d:
            o.training_outer_id = d['training_outer_id']
        return o


