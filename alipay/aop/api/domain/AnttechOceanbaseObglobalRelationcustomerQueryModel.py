#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryCustomerAndLeadsByUidRequest import QueryCustomerAndLeadsByUidRequest


class AnttechOceanbaseObglobalRelationcustomerQueryModel(object):

    def __init__(self):
        self._query_customer_and_leads_by_uid_request = None

    @property
    def query_customer_and_leads_by_uid_request(self):
        return self._query_customer_and_leads_by_uid_request

    @query_customer_and_leads_by_uid_request.setter
    def query_customer_and_leads_by_uid_request(self, value):
        if isinstance(value, list):
            self._query_customer_and_leads_by_uid_request = list()
            for i in value:
                if isinstance(i, QueryCustomerAndLeadsByUidRequest):
                    self._query_customer_and_leads_by_uid_request.append(i)
                else:
                    self._query_customer_and_leads_by_uid_request.append(QueryCustomerAndLeadsByUidRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.query_customer_and_leads_by_uid_request:
            if isinstance(self.query_customer_and_leads_by_uid_request, list):
                for i in range(0, len(self.query_customer_and_leads_by_uid_request)):
                    element = self.query_customer_and_leads_by_uid_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_customer_and_leads_by_uid_request[i] = element.to_alipay_dict()
            if hasattr(self.query_customer_and_leads_by_uid_request, 'to_alipay_dict'):
                params['query_customer_and_leads_by_uid_request'] = self.query_customer_and_leads_by_uid_request.to_alipay_dict()
            else:
                params['query_customer_and_leads_by_uid_request'] = self.query_customer_and_leads_by_uid_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalRelationcustomerQueryModel()
        if 'query_customer_and_leads_by_uid_request' in d:
            o.query_customer_and_leads_by_uid_request = d['query_customer_and_leads_by_uid_request']
        return o


