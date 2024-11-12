#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommandContent import CommandContent


class AnttechBlockchainFinanceEnergyCommandSubmitModel(object):

    def __init__(self):
        self._command_content = None
        self._entity_id = None
        self._function_type = None
        self._product_agreement_code = None
        self._request_id = None
        self._scheduler_flag = None
        self._scheduler_time = None

    @property
    def command_content(self):
        return self._command_content

    @command_content.setter
    def command_content(self, value):
        if isinstance(value, CommandContent):
            self._command_content = value
        else:
            self._command_content = CommandContent.from_alipay_dict(value)
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def function_type(self):
        return self._function_type

    @function_type.setter
    def function_type(self, value):
        self._function_type = value
    @property
    def product_agreement_code(self):
        return self._product_agreement_code

    @product_agreement_code.setter
    def product_agreement_code(self, value):
        self._product_agreement_code = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scheduler_flag(self):
        return self._scheduler_flag

    @scheduler_flag.setter
    def scheduler_flag(self, value):
        self._scheduler_flag = value
    @property
    def scheduler_time(self):
        return self._scheduler_time

    @scheduler_time.setter
    def scheduler_time(self, value):
        self._scheduler_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.command_content:
            if hasattr(self.command_content, 'to_alipay_dict'):
                params['command_content'] = self.command_content.to_alipay_dict()
            else:
                params['command_content'] = self.command_content
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.function_type:
            if hasattr(self.function_type, 'to_alipay_dict'):
                params['function_type'] = self.function_type.to_alipay_dict()
            else:
                params['function_type'] = self.function_type
        if self.product_agreement_code:
            if hasattr(self.product_agreement_code, 'to_alipay_dict'):
                params['product_agreement_code'] = self.product_agreement_code.to_alipay_dict()
            else:
                params['product_agreement_code'] = self.product_agreement_code
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scheduler_flag:
            if hasattr(self.scheduler_flag, 'to_alipay_dict'):
                params['scheduler_flag'] = self.scheduler_flag.to_alipay_dict()
            else:
                params['scheduler_flag'] = self.scheduler_flag
        if self.scheduler_time:
            if hasattr(self.scheduler_time, 'to_alipay_dict'):
                params['scheduler_time'] = self.scheduler_time.to_alipay_dict()
            else:
                params['scheduler_time'] = self.scheduler_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceEnergyCommandSubmitModel()
        if 'command_content' in d:
            o.command_content = d['command_content']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'function_type' in d:
            o.function_type = d['function_type']
        if 'product_agreement_code' in d:
            o.product_agreement_code = d['product_agreement_code']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scheduler_flag' in d:
            o.scheduler_flag = d['scheduler_flag']
        if 'scheduler_time' in d:
            o.scheduler_time = d['scheduler_time']
        return o


