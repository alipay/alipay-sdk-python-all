#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractConsultResultVO(object):

    def __init__(self):
        self._contract_no = None
        self._need_approval = None

    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def need_approval(self):
        return self._need_approval

    @need_approval.setter
    def need_approval(self, value):
        self._need_approval = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.need_approval:
            if hasattr(self.need_approval, 'to_alipay_dict'):
                params['need_approval'] = self.need_approval.to_alipay_dict()
            else:
                params['need_approval'] = self.need_approval
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractConsultResultVO()
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'need_approval' in d:
            o.need_approval = d['need_approval']
        return o


