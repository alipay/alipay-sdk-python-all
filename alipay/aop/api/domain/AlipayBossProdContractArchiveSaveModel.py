#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiContractFileSaDTO import OpenApiContractFileSaDTO


class AlipayBossProdContractArchiveSaveModel(object):

    def __init__(self):
        self._contract_code = None
        self._contract_files = None
        self._tenant = None
        self._voucher_id = None

    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def contract_files(self):
        return self._contract_files

    @contract_files.setter
    def contract_files(self, value):
        if isinstance(value, list):
            self._contract_files = list()
            for i in value:
                if isinstance(i, OpenApiContractFileSaDTO):
                    self._contract_files.append(i)
                else:
                    self._contract_files.append(OpenApiContractFileSaDTO.from_alipay_dict(i))
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_code:
            if hasattr(self.contract_code, 'to_alipay_dict'):
                params['contract_code'] = self.contract_code.to_alipay_dict()
            else:
                params['contract_code'] = self.contract_code
        if self.contract_files:
            if isinstance(self.contract_files, list):
                for i in range(0, len(self.contract_files)):
                    element = self.contract_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_files[i] = element.to_alipay_dict()
            if hasattr(self.contract_files, 'to_alipay_dict'):
                params['contract_files'] = self.contract_files.to_alipay_dict()
            else:
                params['contract_files'] = self.contract_files
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdContractArchiveSaveModel()
        if 'contract_code' in d:
            o.contract_code = d['contract_code']
        if 'contract_files' in d:
            o.contract_files = d['contract_files']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


