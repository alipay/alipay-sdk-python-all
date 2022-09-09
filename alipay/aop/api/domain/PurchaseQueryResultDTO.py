#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsAgreementDTO import InsAgreementDTO
from alipay.aop.api.domain.PurchaseInsurePlanDTO import PurchaseInsurePlanDTO
from alipay.aop.api.domain.InsPeriodDTO import InsPeriodDTO


class PurchaseQueryResultDTO(object):

    def __init__(self):
        self._agreement_list = None
        self._effect_time = None
        self._end_time = None
        self._inst_id = None
        self._inst_name = None
        self._insure_plans = None
        self._issued_amount = None
        self._partner_org_id = None
        self._product_code = None
        self._product_desc = None
        self._product_info_url = None
        self._product_name = None
        self._product_plan_id = None
        self._purchase_contract_id = None
        self._related_subject_id = None
        self._related_subject_type = None
        self._renew = None
        self._renew_period = None
        self._show_uninsured_option = None
        self._status = None
        self._total_amount = None
        self._user_id = None

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
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
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
    def issued_amount(self):
        return self._issued_amount

    @issued_amount.setter
    def issued_amount(self, value):
        self._issued_amount = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
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
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value
    @property
    def purchase_contract_id(self):
        return self._purchase_contract_id

    @purchase_contract_id.setter
    def purchase_contract_id(self, value):
        self._purchase_contract_id = value
    @property
    def related_subject_id(self):
        return self._related_subject_id

    @related_subject_id.setter
    def related_subject_id(self, value):
        self._related_subject_id = value
    @property
    def related_subject_type(self):
        return self._related_subject_type

    @related_subject_type.setter
    def related_subject_type(self, value):
        self._related_subject_type = value
    @property
    def renew(self):
        return self._renew

    @renew.setter
    def renew(self, value):
        self._renew = value
    @property
    def renew_period(self):
        return self._renew_period

    @renew_period.setter
    def renew_period(self, value):
        if isinstance(value, InsPeriodDTO):
            self._renew_period = value
        else:
            self._renew_period = InsPeriodDTO.from_alipay_dict(value)
    @property
    def show_uninsured_option(self):
        return self._show_uninsured_option

    @show_uninsured_option.setter
    def show_uninsured_option(self, value):
        self._show_uninsured_option = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
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
        if self.issued_amount:
            if hasattr(self.issued_amount, 'to_alipay_dict'):
                params['issued_amount'] = self.issued_amount.to_alipay_dict()
            else:
                params['issued_amount'] = self.issued_amount
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
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
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        if self.purchase_contract_id:
            if hasattr(self.purchase_contract_id, 'to_alipay_dict'):
                params['purchase_contract_id'] = self.purchase_contract_id.to_alipay_dict()
            else:
                params['purchase_contract_id'] = self.purchase_contract_id
        if self.related_subject_id:
            if hasattr(self.related_subject_id, 'to_alipay_dict'):
                params['related_subject_id'] = self.related_subject_id.to_alipay_dict()
            else:
                params['related_subject_id'] = self.related_subject_id
        if self.related_subject_type:
            if hasattr(self.related_subject_type, 'to_alipay_dict'):
                params['related_subject_type'] = self.related_subject_type.to_alipay_dict()
            else:
                params['related_subject_type'] = self.related_subject_type
        if self.renew:
            if hasattr(self.renew, 'to_alipay_dict'):
                params['renew'] = self.renew.to_alipay_dict()
            else:
                params['renew'] = self.renew
        if self.renew_period:
            if hasattr(self.renew_period, 'to_alipay_dict'):
                params['renew_period'] = self.renew_period.to_alipay_dict()
            else:
                params['renew_period'] = self.renew_period
        if self.show_uninsured_option:
            if hasattr(self.show_uninsured_option, 'to_alipay_dict'):
                params['show_uninsured_option'] = self.show_uninsured_option.to_alipay_dict()
            else:
                params['show_uninsured_option'] = self.show_uninsured_option
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PurchaseQueryResultDTO()
        if 'agreement_list' in d:
            o.agreement_list = d['agreement_list']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'insure_plans' in d:
            o.insure_plans = d['insure_plans']
        if 'issued_amount' in d:
            o.issued_amount = d['issued_amount']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_desc' in d:
            o.product_desc = d['product_desc']
        if 'product_info_url' in d:
            o.product_info_url = d['product_info_url']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'purchase_contract_id' in d:
            o.purchase_contract_id = d['purchase_contract_id']
        if 'related_subject_id' in d:
            o.related_subject_id = d['related_subject_id']
        if 'related_subject_type' in d:
            o.related_subject_type = d['related_subject_type']
        if 'renew' in d:
            o.renew = d['renew']
        if 'renew_period' in d:
            o.renew_period = d['renew_period']
        if 'show_uninsured_option' in d:
            o.show_uninsured_option = d['show_uninsured_option']
        if 'status' in d:
            o.status = d['status']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


