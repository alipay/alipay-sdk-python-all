#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryCustomerByCsdWorkNoReq import QueryCustomerByCsdWorkNoReq


class AnttechOceanbaseObglobalCustomerbycsdQueryModel(object):

    def __init__(self):
        self._query_customer_by_csd_work_no_request = None

    @property
    def query_customer_by_csd_work_no_request(self):
        return self._query_customer_by_csd_work_no_request

    @query_customer_by_csd_work_no_request.setter
    def query_customer_by_csd_work_no_request(self, value):
        if isinstance(value, QueryCustomerByCsdWorkNoReq):
            self._query_customer_by_csd_work_no_request = value
        else:
            self._query_customer_by_csd_work_no_request = QueryCustomerByCsdWorkNoReq.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.query_customer_by_csd_work_no_request:
            if hasattr(self.query_customer_by_csd_work_no_request, 'to_alipay_dict'):
                params['query_customer_by_csd_work_no_request'] = self.query_customer_by_csd_work_no_request.to_alipay_dict()
            else:
                params['query_customer_by_csd_work_no_request'] = self.query_customer_by_csd_work_no_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalCustomerbycsdQueryModel()
        if 'query_customer_by_csd_work_no_request' in d:
            o.query_customer_by_csd_work_no_request = d['query_customer_by_csd_work_no_request']
        return o


