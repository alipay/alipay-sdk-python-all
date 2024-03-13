#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GetLeadsByLeadsCodeRequest import GetLeadsByLeadsCodeRequest


class AnttechOceanbaseObglobalLeadsQueryModel(object):

    def __init__(self):
        self._describe_leads_request = None

    @property
    def describe_leads_request(self):
        return self._describe_leads_request

    @describe_leads_request.setter
    def describe_leads_request(self, value):
        if isinstance(value, GetLeadsByLeadsCodeRequest):
            self._describe_leads_request = value
        else:
            self._describe_leads_request = GetLeadsByLeadsCodeRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.describe_leads_request:
            if hasattr(self.describe_leads_request, 'to_alipay_dict'):
                params['describe_leads_request'] = self.describe_leads_request.to_alipay_dict()
            else:
                params['describe_leads_request'] = self.describe_leads_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalLeadsQueryModel()
        if 'describe_leads_request' in d:
            o.describe_leads_request = d['describe_leads_request']
        return o


