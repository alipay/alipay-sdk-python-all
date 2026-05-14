#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaleForceLeadsMemberDeleteDTO import SaleForceLeadsMemberDeleteDTO


class AnttechOceanbaseObglobalSfleadsmemberDeleteModel(object):

    def __init__(self):
        self._salesforce_delete_leads_member_request = None

    @property
    def salesforce_delete_leads_member_request(self):
        return self._salesforce_delete_leads_member_request

    @salesforce_delete_leads_member_request.setter
    def salesforce_delete_leads_member_request(self, value):
        if isinstance(value, SaleForceLeadsMemberDeleteDTO):
            self._salesforce_delete_leads_member_request = value
        else:
            self._salesforce_delete_leads_member_request = SaleForceLeadsMemberDeleteDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.salesforce_delete_leads_member_request:
            if hasattr(self.salesforce_delete_leads_member_request, 'to_alipay_dict'):
                params['salesforce_delete_leads_member_request'] = self.salesforce_delete_leads_member_request.to_alipay_dict()
            else:
                params['salesforce_delete_leads_member_request'] = self.salesforce_delete_leads_member_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfleadsmemberDeleteModel()
        if 'salesforce_delete_leads_member_request' in d:
            o.salesforce_delete_leads_member_request = d['salesforce_delete_leads_member_request']
        return o


