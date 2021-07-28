#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractStartInfoOpenApiVO import ContractStartInfoOpenApiVO


class AlipayBossContractGeneralCreateModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_source = None
        self._contract_list = None
        self._start_type = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def contract_list(self):
        return self._contract_list

    @contract_list.setter
    def contract_list(self, value):
        if isinstance(value, list):
            self._contract_list = list()
            for i in value:
                if isinstance(i, ContractStartInfoOpenApiVO):
                    self._contract_list.append(i)
                else:
                    self._contract_list.append(ContractStartInfoOpenApiVO.from_alipay_dict(i))
    @property
    def start_type(self):
        return self._start_type

    @start_type.setter
    def start_type(self, value):
        self._start_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.contract_list:
            if isinstance(self.contract_list, list):
                for i in range(0, len(self.contract_list)):
                    element = self.contract_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_list, 'to_alipay_dict'):
                params['contract_list'] = self.contract_list.to_alipay_dict()
            else:
                params['contract_list'] = self.contract_list
        if self.start_type:
            if hasattr(self.start_type, 'to_alipay_dict'):
                params['start_type'] = self.start_type.to_alipay_dict()
            else:
                params['start_type'] = self.start_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossContractGeneralCreateModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'contract_list' in d:
            o.contract_list = d['contract_list']
        if 'start_type' in d:
            o.start_type = d['start_type']
        return o


