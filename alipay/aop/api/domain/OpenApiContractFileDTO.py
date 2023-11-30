#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiSubContractFileDTO import OpenApiSubContractFileDTO


class OpenApiContractFileDTO(object):

    def __init__(self):
        self._contract_name = None
        self._contract_status = None
        self._contract_type = None
        self._matter_contract_code = None
        self._num = None
        self._sub_contract_file_results = None

    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def contract_status(self):
        return self._contract_status

    @contract_status.setter
    def contract_status(self, value):
        self._contract_status = value
    @property
    def contract_type(self):
        return self._contract_type

    @contract_type.setter
    def contract_type(self, value):
        self._contract_type = value
    @property
    def matter_contract_code(self):
        return self._matter_contract_code

    @matter_contract_code.setter
    def matter_contract_code(self, value):
        self._matter_contract_code = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def sub_contract_file_results(self):
        return self._sub_contract_file_results

    @sub_contract_file_results.setter
    def sub_contract_file_results(self, value):
        if isinstance(value, list):
            self._sub_contract_file_results = list()
            for i in value:
                if isinstance(i, OpenApiSubContractFileDTO):
                    self._sub_contract_file_results.append(i)
                else:
                    self._sub_contract_file_results.append(OpenApiSubContractFileDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.contract_status:
            if hasattr(self.contract_status, 'to_alipay_dict'):
                params['contract_status'] = self.contract_status.to_alipay_dict()
            else:
                params['contract_status'] = self.contract_status
        if self.contract_type:
            if hasattr(self.contract_type, 'to_alipay_dict'):
                params['contract_type'] = self.contract_type.to_alipay_dict()
            else:
                params['contract_type'] = self.contract_type
        if self.matter_contract_code:
            if hasattr(self.matter_contract_code, 'to_alipay_dict'):
                params['matter_contract_code'] = self.matter_contract_code.to_alipay_dict()
            else:
                params['matter_contract_code'] = self.matter_contract_code
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.sub_contract_file_results:
            if isinstance(self.sub_contract_file_results, list):
                for i in range(0, len(self.sub_contract_file_results)):
                    element = self.sub_contract_file_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_contract_file_results[i] = element.to_alipay_dict()
            if hasattr(self.sub_contract_file_results, 'to_alipay_dict'):
                params['sub_contract_file_results'] = self.sub_contract_file_results.to_alipay_dict()
            else:
                params['sub_contract_file_results'] = self.sub_contract_file_results
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiContractFileDTO()
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_status' in d:
            o.contract_status = d['contract_status']
        if 'contract_type' in d:
            o.contract_type = d['contract_type']
        if 'matter_contract_code' in d:
            o.matter_contract_code = d['matter_contract_code']
        if 'num' in d:
            o.num = d['num']
        if 'sub_contract_file_results' in d:
            o.sub_contract_file_results = d['sub_contract_file_results']
        return o


