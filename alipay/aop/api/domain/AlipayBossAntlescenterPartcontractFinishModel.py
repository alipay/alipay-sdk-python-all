#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntlescenterFileDTO import AntlescenterFileDTO


class AlipayBossAntlescenterPartcontractFinishModel(object):

    def __init__(self):
        self._contract_no = None
        self._file_info = None
        self._tenant = None

    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def file_info(self):
        return self._file_info

    @file_info.setter
    def file_info(self, value):
        if isinstance(value, AntlescenterFileDTO):
            self._file_info = value
        else:
            self._file_info = AntlescenterFileDTO.from_alipay_dict(value)
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.file_info:
            if hasattr(self.file_info, 'to_alipay_dict'):
                params['file_info'] = self.file_info.to_alipay_dict()
            else:
                params['file_info'] = self.file_info
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossAntlescenterPartcontractFinishModel()
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'file_info' in d:
            o.file_info = d['file_info']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


