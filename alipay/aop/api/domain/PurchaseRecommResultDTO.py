#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsAgreementDTO import InsAgreementDTO
from alipay.aop.api.domain.PurchaseInsurePlanDTO import PurchaseInsurePlanDTO


class PurchaseRecommResultDTO(object):

    def __init__(self):
        self._agreement_list = None
        self._inst_id = None
        self._inst_name = None
        self._insure_plans = None
        self._product_code = None
        self._product_desc = None
        self._product_info_url = None
        self._product_plan_id = None
        self._recommend_flow_id = None
        self._show_uninsured_option = None

    @property
    def agreement_list(self):
        return self._agreement_list

    @agreement_list.setter
    def agreement_list(self, value):
        if isinstance(value, list):
            self._agreement_list = list()
            for i in value:
                if isinstance(i, InsAgreementDTO):
                    self._agreement_list.append(i)
                else:
                    self._agreement_list.append(InsAgreementDTO.from_alipay_dict(i))
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def insure_plans(self):
        return self._insure_plans

    @insure_plans.setter
    def insure_plans(self, value):
        if isinstance(value, list):
            self._insure_plans = list()
            for i in value:
                if isinstance(i, PurchaseInsurePlanDTO):
                    self._insure_plans.append(i)
                else:
                    self._insure_plans.append(PurchaseInsurePlanDTO.from_alipay_dict(i))
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_desc(self):
        return self._product_desc

    @product_desc.setter
    def product_desc(self, value):
        self._product_desc = value
    @property
    def product_info_url(self):
        return self._product_info_url

    @product_info_url.setter
    def product_info_url(self, value):
        self._product_info_url = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value
    @property
    def recommend_flow_id(self):
        return self._recommend_flow_id

    @recommend_flow_id.setter
    def recommend_flow_id(self, value):
        self._recommend_flow_id = value
    @property
    def show_uninsured_option(self):
        return self._show_uninsured_option

    @show_uninsured_option.setter
    def show_uninsured_option(self, value):
        self._show_uninsured_option = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_list:
            if isinstance(self.agreement_list, list):
                for i in range(0, len(self.agreement_list)):
                    element = self.agreement_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agreement_list[i] = element.to_alipay_dict()
            if hasattr(self.agreement_list, 'to_alipay_dict'):
                params['agreement_list'] = self.agreement_list.to_alipay_dict()
            else:
                params['agreement_list'] = self.agreement_list
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.insure_plans:
            if isinstance(self.insure_plans, list):
                for i in range(0, len(self.insure_plans)):
                    element = self.insure_plans[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.insure_plans[i] = element.to_alipay_dict()
            if hasattr(self.insure_plans, 'to_alipay_dict'):
                params['insure_plans'] = self.insure_plans.to_alipay_dict()
            else:
                params['insure_plans'] = self.insure_plans
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_desc:
            if hasattr(self.product_desc, 'to_alipay_dict'):
                params['product_desc'] = self.product_desc.to_alipay_dict()
            else:
                params['product_desc'] = self.product_desc
        if self.product_info_url:
            if hasattr(self.product_info_url, 'to_alipay_dict'):
                params['product_info_url'] = self.product_info_url.to_alipay_dict()
            else:
                params['product_info_url'] = self.product_info_url
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        if self.recommend_flow_id:
            if hasattr(self.recommend_flow_id, 'to_alipay_dict'):
                params['recommend_flow_id'] = self.recommend_flow_id.to_alipay_dict()
            else:
                params['recommend_flow_id'] = self.recommend_flow_id
        if self.show_uninsured_option:
            if hasattr(self.show_uninsured_option, 'to_alipay_dict'):
                params['show_uninsured_option'] = self.show_uninsured_option.to_alipay_dict()
            else:
                params['show_uninsured_option'] = self.show_uninsured_option
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PurchaseRecommResultDTO()
        if 'agreement_list' in d:
            o.agreement_list = d['agreement_list']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'insure_plans' in d:
            o.insure_plans = d['insure_plans']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_desc' in d:
            o.product_desc = d['product_desc']
        if 'product_info_url' in d:
            o.product_info_url = d['product_info_url']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'recommend_flow_id' in d:
            o.recommend_flow_id = d['recommend_flow_id']
        if 'show_uninsured_option' in d:
            o.show_uninsured_option = d['show_uninsured_option']
        return o


