#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractInfoVO import ContractInfoVO


class ContractBatchInfoOpenApiResult(object):

    def __init__(self):
        self._approval_status = None
        self._contract_infos = None

    @property
    def approval_status(self):
        return self._approval_status

    @approval_status.setter
    def approval_status(self, value):
        self._approval_status = value
    @property
    def contract_infos(self):
        return self._contract_infos

    @contract_infos.setter
    def contract_infos(self, value):
        if isinstance(value, list):
            self._contract_infos = list()
            for i in value:
                if isinstance(i, ContractInfoVO):
                    self._contract_infos.append(i)
                else:
                    self._contract_infos.append(ContractInfoVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.approval_status:
            if hasattr(self.approval_status, 'to_alipay_dict'):
                params['approval_status'] = self.approval_status.to_alipay_dict()
            else:
                params['approval_status'] = self.approval_status
        if self.contract_infos:
            if isinstance(self.contract_infos, list):
                for i in range(0, len(self.contract_infos)):
                    element = self.contract_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_infos[i] = element.to_alipay_dict()
            if hasattr(self.contract_infos, 'to_alipay_dict'):
                params['contract_infos'] = self.contract_infos.to_alipay_dict()
            else:
                params['contract_infos'] = self.contract_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractBatchInfoOpenApiResult()
        if 'approval_status' in d:
            o.approval_status = d['approval_status']
        if 'contract_infos' in d:
            o.contract_infos = d['contract_infos']
        return o


