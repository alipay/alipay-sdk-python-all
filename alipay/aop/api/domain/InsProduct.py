#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsProdCoverage import InsProdCoverage
from alipay.aop.api.domain.InsLiability import InsLiability
from alipay.aop.api.domain.InsMerchant import InsMerchant
from alipay.aop.api.domain.InsProdResource import InsProdResource
from alipay.aop.api.domain.InsProdTag import InsProdTag


class InsProduct(object):

    def __init__(self):
        self._coverages = None
        self._effect_date = None
        self._invalid_date = None
        self._is_sp = None
        self._liabilities = None
        self._merchant = None
        self._prod_code = None
        self._prod_desc = None
        self._prod_name = None
        self._prod_no = None
        self._prod_version = None
        self._real_premium = None
        self._reduce_premium = None
        self._resources = None
        self._sales = None
        self._short_name = None
        self._sp_code = None
        self._tags = None
        self._total_premium = None

    @property
    def coverages(self):
        return self._coverages

    @coverages.setter
    def coverages(self, value):
        if isinstance(value, InsProdCoverage):
            self._coverages = value
        else:
            self._coverages = InsProdCoverage.from_alipay_dict(value)
    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value
    @property
    def invalid_date(self):
        return self._invalid_date

    @invalid_date.setter
    def invalid_date(self, value):
        self._invalid_date = value
    @property
    def is_sp(self):
        return self._is_sp

    @is_sp.setter
    def is_sp(self, value):
        self._is_sp = value
    @property
    def liabilities(self):
        return self._liabilities

    @liabilities.setter
    def liabilities(self, value):
        if isinstance(value, list):
            self._liabilities = list()
            for i in value:
                if isinstance(i, InsLiability):
                    self._liabilities.append(i)
                else:
                    self._liabilities.append(InsLiability.from_alipay_dict(i))
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, InsMerchant):
            self._merchant = value
        else:
            self._merchant = InsMerchant.from_alipay_dict(value)
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def prod_desc(self):
        return self._prod_desc

    @prod_desc.setter
    def prod_desc(self, value):
        self._prod_desc = value
    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value
    @property
    def prod_no(self):
        return self._prod_no

    @prod_no.setter
    def prod_no(self, value):
        self._prod_no = value
    @property
    def prod_version(self):
        return self._prod_version

    @prod_version.setter
    def prod_version(self, value):
        self._prod_version = value
    @property
    def real_premium(self):
        return self._real_premium

    @real_premium.setter
    def real_premium(self, value):
        self._real_premium = value
    @property
    def reduce_premium(self):
        return self._reduce_premium

    @reduce_premium.setter
    def reduce_premium(self, value):
        self._reduce_premium = value
    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        if isinstance(value, list):
            self._resources = list()
            for i in value:
                if isinstance(i, InsProdResource):
                    self._resources.append(i)
                else:
                    self._resources.append(InsProdResource.from_alipay_dict(i))
    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        self._sales = value
    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        self._short_name = value
    @property
    def sp_code(self):
        return self._sp_code

    @sp_code.setter
    def sp_code(self, value):
        self._sp_code = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                if isinstance(i, InsProdTag):
                    self._tags.append(i)
                else:
                    self._tags.append(InsProdTag.from_alipay_dict(i))
    @property
    def total_premium(self):
        return self._total_premium

    @total_premium.setter
    def total_premium(self, value):
        self._total_premium = value


    def to_alipay_dict(self):
        params = dict()
        if self.coverages:
            if hasattr(self.coverages, 'to_alipay_dict'):
                params['coverages'] = self.coverages.to_alipay_dict()
            else:
                params['coverages'] = self.coverages
        if self.effect_date:
            if hasattr(self.effect_date, 'to_alipay_dict'):
                params['effect_date'] = self.effect_date.to_alipay_dict()
            else:
                params['effect_date'] = self.effect_date
        if self.invalid_date:
            if hasattr(self.invalid_date, 'to_alipay_dict'):
                params['invalid_date'] = self.invalid_date.to_alipay_dict()
            else:
                params['invalid_date'] = self.invalid_date
        if self.is_sp:
            if hasattr(self.is_sp, 'to_alipay_dict'):
                params['is_sp'] = self.is_sp.to_alipay_dict()
            else:
                params['is_sp'] = self.is_sp
        if self.liabilities:
            if isinstance(self.liabilities, list):
                for i in range(0, len(self.liabilities)):
                    element = self.liabilities[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.liabilities[i] = element.to_alipay_dict()
            if hasattr(self.liabilities, 'to_alipay_dict'):
                params['liabilities'] = self.liabilities.to_alipay_dict()
            else:
                params['liabilities'] = self.liabilities
        if self.merchant:
            if hasattr(self.merchant, 'to_alipay_dict'):
                params['merchant'] = self.merchant.to_alipay_dict()
            else:
                params['merchant'] = self.merchant
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.prod_desc:
            if hasattr(self.prod_desc, 'to_alipay_dict'):
                params['prod_desc'] = self.prod_desc.to_alipay_dict()
            else:
                params['prod_desc'] = self.prod_desc
        if self.prod_name:
            if hasattr(self.prod_name, 'to_alipay_dict'):
                params['prod_name'] = self.prod_name.to_alipay_dict()
            else:
                params['prod_name'] = self.prod_name
        if self.prod_no:
            if hasattr(self.prod_no, 'to_alipay_dict'):
                params['prod_no'] = self.prod_no.to_alipay_dict()
            else:
                params['prod_no'] = self.prod_no
        if self.prod_version:
            if hasattr(self.prod_version, 'to_alipay_dict'):
                params['prod_version'] = self.prod_version.to_alipay_dict()
            else:
                params['prod_version'] = self.prod_version
        if self.real_premium:
            if hasattr(self.real_premium, 'to_alipay_dict'):
                params['real_premium'] = self.real_premium.to_alipay_dict()
            else:
                params['real_premium'] = self.real_premium
        if self.reduce_premium:
            if hasattr(self.reduce_premium, 'to_alipay_dict'):
                params['reduce_premium'] = self.reduce_premium.to_alipay_dict()
            else:
                params['reduce_premium'] = self.reduce_premium
        if self.resources:
            if isinstance(self.resources, list):
                for i in range(0, len(self.resources)):
                    element = self.resources[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.resources[i] = element.to_alipay_dict()
            if hasattr(self.resources, 'to_alipay_dict'):
                params['resources'] = self.resources.to_alipay_dict()
            else:
                params['resources'] = self.resources
        if self.sales:
            if hasattr(self.sales, 'to_alipay_dict'):
                params['sales'] = self.sales.to_alipay_dict()
            else:
                params['sales'] = self.sales
        if self.short_name:
            if hasattr(self.short_name, 'to_alipay_dict'):
                params['short_name'] = self.short_name.to_alipay_dict()
            else:
                params['short_name'] = self.short_name
        if self.sp_code:
            if hasattr(self.sp_code, 'to_alipay_dict'):
                params['sp_code'] = self.sp_code.to_alipay_dict()
            else:
                params['sp_code'] = self.sp_code
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.total_premium:
            if hasattr(self.total_premium, 'to_alipay_dict'):
                params['total_premium'] = self.total_premium.to_alipay_dict()
            else:
                params['total_premium'] = self.total_premium
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsProduct()
        if 'coverages' in d:
            o.coverages = d['coverages']
        if 'effect_date' in d:
            o.effect_date = d['effect_date']
        if 'invalid_date' in d:
            o.invalid_date = d['invalid_date']
        if 'is_sp' in d:
            o.is_sp = d['is_sp']
        if 'liabilities' in d:
            o.liabilities = d['liabilities']
        if 'merchant' in d:
            o.merchant = d['merchant']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'prod_desc' in d:
            o.prod_desc = d['prod_desc']
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        if 'prod_version' in d:
            o.prod_version = d['prod_version']
        if 'real_premium' in d:
            o.real_premium = d['real_premium']
        if 'reduce_premium' in d:
            o.reduce_premium = d['reduce_premium']
        if 'resources' in d:
            o.resources = d['resources']
        if 'sales' in d:
            o.sales = d['sales']
        if 'short_name' in d:
            o.short_name = d['short_name']
        if 'sp_code' in d:
            o.sp_code = d['sp_code']
        if 'tags' in d:
            o.tags = d['tags']
        if 'total_premium' in d:
            o.total_premium = d['total_premium']
        return o


