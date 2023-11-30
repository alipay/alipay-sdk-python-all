#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiRelateMatterDTO(object):

    def __init__(self):
        self._consult_contract_code = None
        self._gmt_create = None
        self._matter_code = None
        self._matter_name = None
        self._out_contract_code = None

    @property
    def consult_contract_code(self):
        return self._consult_contract_code

    @consult_contract_code.setter
    def consult_contract_code(self, value):
        self._consult_contract_code = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def matter_code(self):
        return self._matter_code

    @matter_code.setter
    def matter_code(self, value):
        self._matter_code = value
    @property
    def matter_name(self):
        return self._matter_name

    @matter_name.setter
    def matter_name(self, value):
        self._matter_name = value
    @property
    def out_contract_code(self):
        return self._out_contract_code

    @out_contract_code.setter
    def out_contract_code(self, value):
        self._out_contract_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_contract_code:
            if hasattr(self.consult_contract_code, 'to_alipay_dict'):
                params['consult_contract_code'] = self.consult_contract_code.to_alipay_dict()
            else:
                params['consult_contract_code'] = self.consult_contract_code
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.matter_code:
            if hasattr(self.matter_code, 'to_alipay_dict'):
                params['matter_code'] = self.matter_code.to_alipay_dict()
            else:
                params['matter_code'] = self.matter_code
        if self.matter_name:
            if hasattr(self.matter_name, 'to_alipay_dict'):
                params['matter_name'] = self.matter_name.to_alipay_dict()
            else:
                params['matter_name'] = self.matter_name
        if self.out_contract_code:
            if hasattr(self.out_contract_code, 'to_alipay_dict'):
                params['out_contract_code'] = self.out_contract_code.to_alipay_dict()
            else:
                params['out_contract_code'] = self.out_contract_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiRelateMatterDTO()
        if 'consult_contract_code' in d:
            o.consult_contract_code = d['consult_contract_code']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'matter_code' in d:
            o.matter_code = d['matter_code']
        if 'matter_name' in d:
            o.matter_name = d['matter_name']
        if 'out_contract_code' in d:
            o.out_contract_code = d['out_contract_code']
        return o


