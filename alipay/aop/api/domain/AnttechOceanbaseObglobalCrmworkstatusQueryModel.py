#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalCrmworkstatusQueryModel(object):

    def __init__(self):
        self._crm_query_worker_suspended_status_request = None

    @property
    def crm_query_worker_suspended_status_request(self):
        return self._crm_query_worker_suspended_status_request

    @crm_query_worker_suspended_status_request.setter
    def crm_query_worker_suspended_status_request(self, value):
        self._crm_query_worker_suspended_status_request = value


    def to_alipay_dict(self):
        params = dict()
        if self.crm_query_worker_suspended_status_request:
            if hasattr(self.crm_query_worker_suspended_status_request, 'to_alipay_dict'):
                params['crm_query_worker_suspended_status_request'] = self.crm_query_worker_suspended_status_request.to_alipay_dict()
            else:
                params['crm_query_worker_suspended_status_request'] = self.crm_query_worker_suspended_status_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalCrmworkstatusQueryModel()
        if 'crm_query_worker_suspended_status_request' in d:
            o.crm_query_worker_suspended_status_request = d['crm_query_worker_suspended_status_request']
        return o


