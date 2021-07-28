#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractWorkflowUrlResult(object):

    def __init__(self):
        self._contract_no = None
        self._workflow_url = None

    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def workflow_url(self):
        return self._workflow_url

    @workflow_url.setter
    def workflow_url(self, value):
        self._workflow_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.workflow_url:
            if hasattr(self.workflow_url, 'to_alipay_dict'):
                params['workflow_url'] = self.workflow_url.to_alipay_dict()
            else:
                params['workflow_url'] = self.workflow_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractWorkflowUrlResult()
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'workflow_url' in d:
            o.workflow_url = d['workflow_url']
        return o


