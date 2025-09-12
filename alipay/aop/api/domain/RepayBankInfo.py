#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepayBankInfo(object):

    def __init__(self):
        self._repay_bank_code = None
        self._repay_branch_name = None
        self._repay_city = None
        self._repay_inst_id = None
        self._repay_name = None
        self._repay_no = None
        self._repay_province = None

    @property
    def repay_bank_code(self):
        return self._repay_bank_code

    @repay_bank_code.setter
    def repay_bank_code(self, value):
        self._repay_bank_code = value
    @property
    def repay_branch_name(self):
        return self._repay_branch_name

    @repay_branch_name.setter
    def repay_branch_name(self, value):
        self._repay_branch_name = value
    @property
    def repay_city(self):
        return self._repay_city

    @repay_city.setter
    def repay_city(self, value):
        self._repay_city = value
    @property
    def repay_inst_id(self):
        return self._repay_inst_id

    @repay_inst_id.setter
    def repay_inst_id(self, value):
        self._repay_inst_id = value
    @property
    def repay_name(self):
        return self._repay_name

    @repay_name.setter
    def repay_name(self, value):
        self._repay_name = value
    @property
    def repay_no(self):
        return self._repay_no

    @repay_no.setter
    def repay_no(self, value):
        self._repay_no = value
    @property
    def repay_province(self):
        return self._repay_province

    @repay_province.setter
    def repay_province(self, value):
        self._repay_province = value


    def to_alipay_dict(self):
        params = dict()
        if self.repay_bank_code:
            if hasattr(self.repay_bank_code, 'to_alipay_dict'):
                params['repay_bank_code'] = self.repay_bank_code.to_alipay_dict()
            else:
                params['repay_bank_code'] = self.repay_bank_code
        if self.repay_branch_name:
            if hasattr(self.repay_branch_name, 'to_alipay_dict'):
                params['repay_branch_name'] = self.repay_branch_name.to_alipay_dict()
            else:
                params['repay_branch_name'] = self.repay_branch_name
        if self.repay_city:
            if hasattr(self.repay_city, 'to_alipay_dict'):
                params['repay_city'] = self.repay_city.to_alipay_dict()
            else:
                params['repay_city'] = self.repay_city
        if self.repay_inst_id:
            if hasattr(self.repay_inst_id, 'to_alipay_dict'):
                params['repay_inst_id'] = self.repay_inst_id.to_alipay_dict()
            else:
                params['repay_inst_id'] = self.repay_inst_id
        if self.repay_name:
            if hasattr(self.repay_name, 'to_alipay_dict'):
                params['repay_name'] = self.repay_name.to_alipay_dict()
            else:
                params['repay_name'] = self.repay_name
        if self.repay_no:
            if hasattr(self.repay_no, 'to_alipay_dict'):
                params['repay_no'] = self.repay_no.to_alipay_dict()
            else:
                params['repay_no'] = self.repay_no
        if self.repay_province:
            if hasattr(self.repay_province, 'to_alipay_dict'):
                params['repay_province'] = self.repay_province.to_alipay_dict()
            else:
                params['repay_province'] = self.repay_province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepayBankInfo()
        if 'repay_bank_code' in d:
            o.repay_bank_code = d['repay_bank_code']
        if 'repay_branch_name' in d:
            o.repay_branch_name = d['repay_branch_name']
        if 'repay_city' in d:
            o.repay_city = d['repay_city']
        if 'repay_inst_id' in d:
            o.repay_inst_id = d['repay_inst_id']
        if 'repay_name' in d:
            o.repay_name = d['repay_name']
        if 'repay_no' in d:
            o.repay_no = d['repay_no']
        if 'repay_province' in d:
            o.repay_province = d['repay_province']
        return o


