#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNpassporterBenefitCreateModel(object):

    def __init__(self):
        self._benefits_list = None
        self._cert_no = None
        self._cert_type = None
        self._phone = None
        self._project_id = None
        self._solution_type = None

    @property
    def benefits_list(self):
        return self._benefits_list

    @benefits_list.setter
    def benefits_list(self, value):
        if isinstance(value, list):
            self._benefits_list = list()
            for i in value:
                self._benefits_list.append(i)
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def solution_type(self):
        return self._solution_type

    @solution_type.setter
    def solution_type(self, value):
        self._solution_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefits_list:
            if isinstance(self.benefits_list, list):
                for i in range(0, len(self.benefits_list)):
                    element = self.benefits_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefits_list[i] = element.to_alipay_dict()
            if hasattr(self.benefits_list, 'to_alipay_dict'):
                params['benefits_list'] = self.benefits_list.to_alipay_dict()
            else:
                params['benefits_list'] = self.benefits_list
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.solution_type:
            if hasattr(self.solution_type, 'to_alipay_dict'):
                params['solution_type'] = self.solution_type.to_alipay_dict()
            else:
                params['solution_type'] = self.solution_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNpassporterBenefitCreateModel()
        if 'benefits_list' in d:
            o.benefits_list = d['benefits_list']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'phone' in d:
            o.phone = d['phone']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'solution_type' in d:
            o.solution_type = d['solution_type']
        return o


