#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssistantCompanySimpleInfo(object):

    def __init__(self):
        self._company_name = None
        self._ep_cert_no = None

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssistantCompanySimpleInfo()
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        return o


