#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaleForceLeadsMemberModifyDTO import SaleForceLeadsMemberModifyDTO


class AnttechOceanbaseObglobalSfleadsmemberModifyModel(object):

    def __init__(self):
        self._salesforce_update_leads_member_request = None

    @property
    def salesforce_update_leads_member_request(self):
        return self._salesforce_update_leads_member_request

    @salesforce_update_leads_member_request.setter
    def salesforce_update_leads_member_request(self, value):
        if isinstance(value, SaleForceLeadsMemberModifyDTO):
            self._salesforce_update_leads_member_request = value
        else:
            self._salesforce_update_leads_member_request = SaleForceLeadsMemberModifyDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.salesforce_update_leads_member_request:
            if hasattr(self.salesforce_update_leads_member_request, 'to_alipay_dict'):
                params['salesforce_update_leads_member_request'] = self.salesforce_update_leads_member_request.to_alipay_dict()
            else:
                params['salesforce_update_leads_member_request'] = self.salesforce_update_leads_member_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfleadsmemberModifyModel()
        if 'salesforce_update_leads_member_request' in d:
            o.salesforce_update_leads_member_request = d['salesforce_update_leads_member_request']
        return o


