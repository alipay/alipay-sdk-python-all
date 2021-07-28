#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractInfo import ContractInfo


class AlipayBossContractManagementCreateModel(object):

    def __init__(self):
        self._biz_source = None
        self._contract_batch_no = None
        self._contract_info_list = None
        self._process_instance_id = None
        self._task_id = None

    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def contract_batch_no(self):
        return self._contract_batch_no

    @contract_batch_no.setter
    def contract_batch_no(self, value):
        self._contract_batch_no = value
    @property
    def contract_info_list(self):
        return self._contract_info_list

    @contract_info_list.setter
    def contract_info_list(self, value):
        if isinstance(value, list):
            self._contract_info_list = list()
            for i in value:
                if isinstance(i, ContractInfo):
                    self._contract_info_list.append(i)
                else:
                    self._contract_info_list.append(ContractInfo.from_alipay_dict(i))
    @property
    def process_instance_id(self):
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, value):
        self._process_instance_id = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.contract_batch_no:
            if hasattr(self.contract_batch_no, 'to_alipay_dict'):
                params['contract_batch_no'] = self.contract_batch_no.to_alipay_dict()
            else:
                params['contract_batch_no'] = self.contract_batch_no
        if self.contract_info_list:
            if isinstance(self.contract_info_list, list):
                for i in range(0, len(self.contract_info_list)):
                    element = self.contract_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_info_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_info_list, 'to_alipay_dict'):
                params['contract_info_list'] = self.contract_info_list.to_alipay_dict()
            else:
                params['contract_info_list'] = self.contract_info_list
        if self.process_instance_id:
            if hasattr(self.process_instance_id, 'to_alipay_dict'):
                params['process_instance_id'] = self.process_instance_id.to_alipay_dict()
            else:
                params['process_instance_id'] = self.process_instance_id
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossContractManagementCreateModel()
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'contract_batch_no' in d:
            o.contract_batch_no = d['contract_batch_no']
        if 'contract_info_list' in d:
            o.contract_info_list = d['contract_info_list']
        if 'process_instance_id' in d:
            o.process_instance_id = d['process_instance_id']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


