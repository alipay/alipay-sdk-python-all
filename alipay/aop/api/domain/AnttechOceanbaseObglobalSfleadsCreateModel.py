#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaleForceCreateLeadsParams import SaleForceCreateLeadsParams


class AnttechOceanbaseObglobalSfleadsCreateModel(object):

    def __init__(self):
        self._salesforce_create_leads_request = None

    @property
    def salesforce_create_leads_request(self):
        return self._salesforce_create_leads_request

    @salesforce_create_leads_request.setter
    def salesforce_create_leads_request(self, value):
        if isinstance(value, SaleForceCreateLeadsParams):
            self._salesforce_create_leads_request = value
        else:
            self._salesforce_create_leads_request = SaleForceCreateLeadsParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.salesforce_create_leads_request:
            if hasattr(self.salesforce_create_leads_request, 'to_alipay_dict'):
                params['salesforce_create_leads_request'] = self.salesforce_create_leads_request.to_alipay_dict()
            else:
                params['salesforce_create_leads_request'] = self.salesforce_create_leads_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfleadsCreateModel()
        if 'salesforce_create_leads_request' in d:
            o.salesforce_create_leads_request = d['salesforce_create_leads_request']
        return o


