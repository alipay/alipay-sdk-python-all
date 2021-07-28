#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GFAOpenAPICommandReceipt import GFAOpenAPICommandReceipt
from alipay.aop.api.domain.GFAOpenAPICommandReceipt import GFAOpenAPICommandReceipt


class GFAOpenAPICommand(object):

    def __init__(self):
        self._acceptance_id = None
        self._amortize_receipt = None
        self._command_consumer = None
        self._command_id = None
        self._config_instance_id = None
        self._direction = None
        self._out_business_no = None
        self._platform_product_code = None
        self._settle_receipt = None
        self._status = None
        self._type = None

    @property
    def acceptance_id(self):
        return self._acceptance_id

    @acceptance_id.setter
    def acceptance_id(self, value):
        self._acceptance_id = value
    @property
    def amortize_receipt(self):
        return self._amortize_receipt

    @amortize_receipt.setter
    def amortize_receipt(self, value):
        if isinstance(value, GFAOpenAPICommandReceipt):
            self._amortize_receipt = value
        else:
            self._amortize_receipt = GFAOpenAPICommandReceipt.from_alipay_dict(value)
    @property
    def command_consumer(self):
        return self._command_consumer

    @command_consumer.setter
    def command_consumer(self, value):
        self._command_consumer = value
    @property
    def command_id(self):
        return self._command_id

    @command_id.setter
    def command_id(self, value):
        self._command_id = value
    @property
    def config_instance_id(self):
        return self._config_instance_id

    @config_instance_id.setter
    def config_instance_id(self, value):
        self._config_instance_id = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def out_business_no(self):
        return self._out_business_no

    @out_business_no.setter
    def out_business_no(self, value):
        self._out_business_no = value
    @property
    def platform_product_code(self):
        return self._platform_product_code

    @platform_product_code.setter
    def platform_product_code(self, value):
        self._platform_product_code = value
    @property
    def settle_receipt(self):
        return self._settle_receipt

    @settle_receipt.setter
    def settle_receipt(self, value):
        if isinstance(value, GFAOpenAPICommandReceipt):
            self._settle_receipt = value
        else:
            self._settle_receipt = GFAOpenAPICommandReceipt.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.acceptance_id:
            if hasattr(self.acceptance_id, 'to_alipay_dict'):
                params['acceptance_id'] = self.acceptance_id.to_alipay_dict()
            else:
                params['acceptance_id'] = self.acceptance_id
        if self.amortize_receipt:
            if hasattr(self.amortize_receipt, 'to_alipay_dict'):
                params['amortize_receipt'] = self.amortize_receipt.to_alipay_dict()
            else:
                params['amortize_receipt'] = self.amortize_receipt
        if self.command_consumer:
            if hasattr(self.command_consumer, 'to_alipay_dict'):
                params['command_consumer'] = self.command_consumer.to_alipay_dict()
            else:
                params['command_consumer'] = self.command_consumer
        if self.command_id:
            if hasattr(self.command_id, 'to_alipay_dict'):
                params['command_id'] = self.command_id.to_alipay_dict()
            else:
                params['command_id'] = self.command_id
        if self.config_instance_id:
            if hasattr(self.config_instance_id, 'to_alipay_dict'):
                params['config_instance_id'] = self.config_instance_id.to_alipay_dict()
            else:
                params['config_instance_id'] = self.config_instance_id
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.out_business_no:
            if hasattr(self.out_business_no, 'to_alipay_dict'):
                params['out_business_no'] = self.out_business_no.to_alipay_dict()
            else:
                params['out_business_no'] = self.out_business_no
        if self.platform_product_code:
            if hasattr(self.platform_product_code, 'to_alipay_dict'):
                params['platform_product_code'] = self.platform_product_code.to_alipay_dict()
            else:
                params['platform_product_code'] = self.platform_product_code
        if self.settle_receipt:
            if hasattr(self.settle_receipt, 'to_alipay_dict'):
                params['settle_receipt'] = self.settle_receipt.to_alipay_dict()
            else:
                params['settle_receipt'] = self.settle_receipt
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPICommand()
        if 'acceptance_id' in d:
            o.acceptance_id = d['acceptance_id']
        if 'amortize_receipt' in d:
            o.amortize_receipt = d['amortize_receipt']
        if 'command_consumer' in d:
            o.command_consumer = d['command_consumer']
        if 'command_id' in d:
            o.command_id = d['command_id']
        if 'config_instance_id' in d:
            o.config_instance_id = d['config_instance_id']
        if 'direction' in d:
            o.direction = d['direction']
        if 'out_business_no' in d:
            o.out_business_no = d['out_business_no']
        if 'platform_product_code' in d:
            o.platform_product_code = d['platform_product_code']
        if 'settle_receipt' in d:
            o.settle_receipt = d['settle_receipt']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        return o


