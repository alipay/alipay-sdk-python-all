#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaleForceUpdateLeadsParams import SaleForceUpdateLeadsParams


class AnttechOceanbaseObglobalSfleadsModifyModel(object):

    def __init__(self):
        self._salesforce_update_leads_request = None

    @property
    def salesforce_update_leads_request(self):
        return self._salesforce_update_leads_request

    @salesforce_update_leads_request.setter
    def salesforce_update_leads_request(self, value):
        if isinstance(value, SaleForceUpdateLeadsParams):
            self._salesforce_update_leads_request = value
        else:
            self._salesforce_update_leads_request = SaleForceUpdateLeadsParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.salesforce_update_leads_request:
            if hasattr(self.salesforce_update_leads_request, 'to_alipay_dict'):
                params['salesforce_update_leads_request'] = self.salesforce_update_leads_request.to_alipay_dict()
            else:
                params['salesforce_update_leads_request'] = self.salesforce_update_leads_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfleadsModifyModel()
        if 'salesforce_update_leads_request' in d:
            o.salesforce_update_leads_request = d['salesforce_update_leads_request']
        return o


