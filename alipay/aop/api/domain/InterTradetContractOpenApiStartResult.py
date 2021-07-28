#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractWorkflowUrlResult import ContractWorkflowUrlResult


class InterTradetContractOpenApiStartResult(object):

    def __init__(self):
        self._contract_workflow_urls = None

    @property
    def contract_workflow_urls(self):
        return self._contract_workflow_urls

    @contract_workflow_urls.setter
    def contract_workflow_urls(self, value):
        if isinstance(value, list):
            self._contract_workflow_urls = list()
            for i in value:
                if isinstance(i, ContractWorkflowUrlResult):
                    self._contract_workflow_urls.append(i)
                else:
                    self._contract_workflow_urls.append(ContractWorkflowUrlResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.contract_workflow_urls:
            if isinstance(self.contract_workflow_urls, list):
                for i in range(0, len(self.contract_workflow_urls)):
                    element = self.contract_workflow_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_workflow_urls[i] = element.to_alipay_dict()
            if hasattr(self.contract_workflow_urls, 'to_alipay_dict'):
                params['contract_workflow_urls'] = self.contract_workflow_urls.to_alipay_dict()
            else:
                params['contract_workflow_urls'] = self.contract_workflow_urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InterTradetContractOpenApiStartResult()
        if 'contract_workflow_urls' in d:
            o.contract_workflow_urls = d['contract_workflow_urls']
        return o


