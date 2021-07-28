#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecomPlan import RecomPlan
from alipay.aop.api.domain.ProdResource import ProdResource
from alipay.aop.api.domain.ProdResource import ProdResource


class RecomProduct(object):

    def __init__(self):
        self._base_premium = None
        self._biz_data = None
        self._company_id = None
        self._company_name = None
        self._company_seller_id = None
        self._company_seller_nick = None
        self._company_service_phone = None
        self._csu_no = None
        self._max_quan = None
        self._name = None
        self._plans = None
        self._premium = None
        self._prod_no = None
        self._resource_list = None
        self._resources = None
        self._restriction_type = None
        self._sum_insured = None
        self._type = None

    @property
    def base_premium(self):
        return self._base_premium

    @base_premium.setter
    def base_premium(self, value):
        self._base_premium = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_seller_id(self):
        return self._company_seller_id

    @company_seller_id.setter
    def company_seller_id(self, value):
        self._company_seller_id = value
    @property
    def company_seller_nick(self):
        return self._company_seller_nick

    @company_seller_nick.setter
    def company_seller_nick(self, value):
        self._company_seller_nick = value
    @property
    def company_service_phone(self):
        return self._company_service_phone

    @company_service_phone.setter
    def company_service_phone(self, value):
        self._company_service_phone = value
    @property
    def csu_no(self):
        return self._csu_no

    @csu_no.setter
    def csu_no(self, value):
        self._csu_no = value
    @property
    def max_quan(self):
        return self._max_quan

    @max_quan.setter
    def max_quan(self, value):
        self._max_quan = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def plans(self):
        return self._plans

    @plans.setter
    def plans(self, value):
        if isinstance(value, RecomPlan):
            self._plans = value
        else:
            self._plans = RecomPlan.from_alipay_dict(value)
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def prod_no(self):
        return self._prod_no

    @prod_no.setter
    def prod_no(self, value):
        self._prod_no = value
    @property
    def resource_list(self):
        return self._resource_list

    @resource_list.setter
    def resource_list(self, value):
        if isinstance(value, list):
            self._resource_list = list()
            for i in value:
                if isinstance(i, ProdResource):
                    self._resource_list.append(i)
                else:
                    self._resource_list.append(ProdResource.from_alipay_dict(i))
    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        if isinstance(value, ProdResource):
            self._resources = value
        else:
            self._resources = ProdResource.from_alipay_dict(value)
    @property
    def restriction_type(self):
        return self._restriction_type

    @restriction_type.setter
    def restriction_type(self, value):
        self._restriction_type = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_premium:
            if hasattr(self.base_premium, 'to_alipay_dict'):
                params['base_premium'] = self.base_premium.to_alipay_dict()
            else:
                params['base_premium'] = self.base_premium
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.company_seller_id:
            if hasattr(self.company_seller_id, 'to_alipay_dict'):
                params['company_seller_id'] = self.company_seller_id.to_alipay_dict()
            else:
                params['company_seller_id'] = self.company_seller_id
        if self.company_seller_nick:
            if hasattr(self.company_seller_nick, 'to_alipay_dict'):
                params['company_seller_nick'] = self.company_seller_nick.to_alipay_dict()
            else:
                params['company_seller_nick'] = self.company_seller_nick
        if self.company_service_phone:
            if hasattr(self.company_service_phone, 'to_alipay_dict'):
                params['company_service_phone'] = self.company_service_phone.to_alipay_dict()
            else:
                params['company_service_phone'] = self.company_service_phone
        if self.csu_no:
            if hasattr(self.csu_no, 'to_alipay_dict'):
                params['csu_no'] = self.csu_no.to_alipay_dict()
            else:
                params['csu_no'] = self.csu_no
        if self.max_quan:
            if hasattr(self.max_quan, 'to_alipay_dict'):
                params['max_quan'] = self.max_quan.to_alipay_dict()
            else:
                params['max_quan'] = self.max_quan
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.plans:
            if hasattr(self.plans, 'to_alipay_dict'):
                params['plans'] = self.plans.to_alipay_dict()
            else:
                params['plans'] = self.plans
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.prod_no:
            if hasattr(self.prod_no, 'to_alipay_dict'):
                params['prod_no'] = self.prod_no.to_alipay_dict()
            else:
                params['prod_no'] = self.prod_no
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
        if self.resources:
            if hasattr(self.resources, 'to_alipay_dict'):
                params['resources'] = self.resources.to_alipay_dict()
            else:
                params['resources'] = self.resources
        if self.restriction_type:
            if hasattr(self.restriction_type, 'to_alipay_dict'):
                params['restriction_type'] = self.restriction_type.to_alipay_dict()
            else:
                params['restriction_type'] = self.restriction_type
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
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
        o = RecomProduct()
        if 'base_premium' in d:
            o.base_premium = d['base_premium']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'company_seller_id' in d:
            o.company_seller_id = d['company_seller_id']
        if 'company_seller_nick' in d:
            o.company_seller_nick = d['company_seller_nick']
        if 'company_service_phone' in d:
            o.company_service_phone = d['company_service_phone']
        if 'csu_no' in d:
            o.csu_no = d['csu_no']
        if 'max_quan' in d:
            o.max_quan = d['max_quan']
        if 'name' in d:
            o.name = d['name']
        if 'plans' in d:
            o.plans = d['plans']
        if 'premium' in d:
            o.premium = d['premium']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        if 'resource_list' in d:
            o.resource_list = d['resource_list']
        if 'resources' in d:
            o.resources = d['resources']
        if 'restriction_type' in d:
            o.restriction_type = d['restriction_type']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        if 'type' in d:
            o.type = d['type']
        return o


