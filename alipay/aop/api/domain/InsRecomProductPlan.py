#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsProdResource import InsProdResource


class InsRecomProductPlan(object):

    def __init__(self):
        self._continuous_frequency = None
        self._insurance_id = None
        self._insurance_name = None
        self._name = None
        self._period = None
        self._premium = None
        self._prod_name = None
        self._prod_no = None
        self._prod_version = None
        self._product_id = None
        self._product_plan_id = None
        self._recom_flow_no = None
        self._resource_list = None
        self._sale_plan_no = None
        self._sum_insured = None

    @property
    def continuous_frequency(self):
        return self._continuous_frequency

    @continuous_frequency.setter
    def continuous_frequency(self, value):
        self._continuous_frequency = value
    @property
    def insurance_id(self):
        return self._insurance_id

    @insurance_id.setter
    def insurance_id(self, value):
        self._insurance_id = value
    @property
    def insurance_name(self):
        return self._insurance_name

    @insurance_name.setter
    def insurance_name(self, value):
        self._insurance_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
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
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value
    @property
    def recom_flow_no(self):
        return self._recom_flow_no

    @recom_flow_no.setter
    def recom_flow_no(self, value):
        self._recom_flow_no = value
    @property
    def resource_list(self):
        return self._resource_list

    @resource_list.setter
    def resource_list(self, value):
        if isinstance(value, list):
            self._resource_list = list()
            for i in value:
                if isinstance(i, InsProdResource):
                    self._resource_list.append(i)
                else:
                    self._resource_list.append(InsProdResource.from_alipay_dict(i))
    @property
    def sale_plan_no(self):
        return self._sale_plan_no

    @sale_plan_no.setter
    def sale_plan_no(self, value):
        self._sale_plan_no = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


    def to_alipay_dict(self):
        params = dict()
        if self.continuous_frequency:
            if hasattr(self.continuous_frequency, 'to_alipay_dict'):
                params['continuous_frequency'] = self.continuous_frequency.to_alipay_dict()
            else:
                params['continuous_frequency'] = self.continuous_frequency
        if self.insurance_id:
            if hasattr(self.insurance_id, 'to_alipay_dict'):
                params['insurance_id'] = self.insurance_id.to_alipay_dict()
            else:
                params['insurance_id'] = self.insurance_id
        if self.insurance_name:
            if hasattr(self.insurance_name, 'to_alipay_dict'):
                params['insurance_name'] = self.insurance_name.to_alipay_dict()
            else:
                params['insurance_name'] = self.insurance_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
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
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        if self.recom_flow_no:
            if hasattr(self.recom_flow_no, 'to_alipay_dict'):
                params['recom_flow_no'] = self.recom_flow_no.to_alipay_dict()
            else:
                params['recom_flow_no'] = self.recom_flow_no
        if self.resource_list:
            if isinstance(self.resource_list, list):
                for i in range(0, len(self.resource_list)):
                    element = self.resource_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.resource_list[i] = element.to_alipay_dict()
            if hasattr(self.resource_list, 'to_alipay_dict'):
                params['resource_list'] = self.resource_list.to_alipay_dict()
            else:
                params['resource_list'] = self.resource_list
        if self.sale_plan_no:
            if hasattr(self.sale_plan_no, 'to_alipay_dict'):
                params['sale_plan_no'] = self.sale_plan_no.to_alipay_dict()
            else:
                params['sale_plan_no'] = self.sale_plan_no
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsRecomProductPlan()
        if 'continuous_frequency' in d:
            o.continuous_frequency = d['continuous_frequency']
        if 'insurance_id' in d:
            o.insurance_id = d['insurance_id']
        if 'insurance_name' in d:
            o.insurance_name = d['insurance_name']
        if 'name' in d:
            o.name = d['name']
        if 'period' in d:
            o.period = d['period']
        if 'premium' in d:
            o.premium = d['premium']
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        if 'prod_version' in d:
            o.prod_version = d['prod_version']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'recom_flow_no' in d:
            o.recom_flow_no = d['recom_flow_no']
        if 'resource_list' in d:
            o.resource_list = d['resource_list']
        if 'sale_plan_no' in d:
            o.sale_plan_no = d['sale_plan_no']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


