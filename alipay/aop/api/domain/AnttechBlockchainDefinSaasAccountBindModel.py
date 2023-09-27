#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceId import ReferenceId


class AnttechBlockchainDefinSaasAccountBindModel(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._category = None
        self._inst_id = None
        self._offical_name = None
        self._offical_number = None
        self._out_member_id = None
        self._platform_member_id = None
        self._principal = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, list):
            self._category = list()
            for i in value:
                self._category.append(i)
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def offical_name(self):
        return self._offical_name

    @offical_name.setter
    def offical_name(self, value):
        self._offical_name = value
    @property
    def offical_number(self):
        return self._offical_number

    @offical_number.setter
    def offical_number(self, value):
        self._offical_number = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._out_member_id = value
        else:
            self._out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.category:
            if isinstance(self.category, list):
                for i in range(0, len(self.category)):
                    element = self.category[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category[i] = element.to_alipay_dict()
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.offical_name:
            if hasattr(self.offical_name, 'to_alipay_dict'):
                params['offical_name'] = self.offical_name.to_alipay_dict()
            else:
                params['offical_name'] = self.offical_name
        if self.offical_number:
            if hasattr(self.offical_number, 'to_alipay_dict'):
                params['offical_number'] = self.offical_number.to_alipay_dict()
            else:
                params['offical_number'] = self.offical_number
        if self.out_member_id:
            if hasattr(self.out_member_id, 'to_alipay_dict'):
                params['out_member_id'] = self.out_member_id.to_alipay_dict()
            else:
                params['out_member_id'] = self.out_member_id
        if self.platform_member_id:
            if hasattr(self.platform_member_id, 'to_alipay_dict'):
                params['platform_member_id'] = self.platform_member_id.to_alipay_dict()
            else:
                params['platform_member_id'] = self.platform_member_id
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinSaasAccountBindModel()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'category' in d:
            o.category = d['category']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'offical_name' in d:
            o.offical_name = d['offical_name']
        if 'offical_number' in d:
            o.offical_number = d['offical_number']
        if 'out_member_id' in d:
            o.out_member_id = d['out_member_id']
        if 'platform_member_id' in d:
            o.platform_member_id = d['platform_member_id']
        if 'principal' in d:
            o.principal = d['principal']
        return o


