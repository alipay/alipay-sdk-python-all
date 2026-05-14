#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaleForceLeadsMemberCreateDTO import SaleForceLeadsMemberCreateDTO


class AnttechOceanbaseObglobalSfleadsmemberCreateModel(object):

    def __init__(self):
        self._salesforce_create_leads_member_request = None

    @property
    def salesforce_create_leads_member_request(self):
        return self._salesforce_create_leads_member_request

    @salesforce_create_leads_member_request.setter
    def salesforce_create_leads_member_request(self, value):
        if isinstance(value, SaleForceLeadsMemberCreateDTO):
            self._salesforce_create_leads_member_request = value
        else:
            self._salesforce_create_leads_member_request = SaleForceLeadsMemberCreateDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.salesforce_create_leads_member_request:
            if hasattr(self.salesforce_create_leads_member_request, 'to_alipay_dict'):
                params['salesforce_create_leads_member_request'] = self.salesforce_create_leads_member_request.to_alipay_dict()
            else:
                params['salesforce_create_leads_member_request'] = self.salesforce_create_leads_member_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfleadsmemberCreateModel()
        if 'salesforce_create_leads_member_request' in d:
            o.salesforce_create_leads_member_request = d['salesforce_create_leads_member_request']
        return o


