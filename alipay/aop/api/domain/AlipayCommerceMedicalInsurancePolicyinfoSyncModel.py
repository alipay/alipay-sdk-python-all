#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContinuousPlan import ContinuousPlan
from alipay.aop.api.domain.Coverage import Coverage
from alipay.aop.api.domain.RelatedPerson import RelatedPerson


class AlipayCommerceMedicalInsurancePolicyinfoSyncModel(object):

    def __init__(self):
        self._company_type = None
        self._continuous_frequency = None
        self._continuous_period = None
        self._continuous_plan_list = None
        self._coverage_list = None
        self._currency = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._electronic_policy_url = None
        self._ext_info = None
        self._first_premium = None
        self._insured_time = None
        self._issue_time = None
        self._old_policy_no = None
        self._open_id = None
        self._pay_time = None
        self._pay_trade_no = None
        self._person_list = None
        self._policy_no = None
        self._policy_type = None
        self._premium = None
        self._prod_name = None
        self._prod_no = None
        self._product_scheme_code = None
        self._source_policy_no = None
        self._status = None
        self._sum_insured = None
        self._surrender_amount = None
        self._surrender_reason = None
        self._surrender_time = None
        self._suspended_reason = None
        self._suspended_time = None
        self._total_premium = None
        self._user_id = None

    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def continuous_frequency(self):
        return self._continuous_frequency

    @continuous_frequency.setter
    def continuous_frequency(self, value):
        self._continuous_frequency = value
    @property
    def continuous_period(self):
        return self._continuous_period

    @continuous_period.setter
    def continuous_period(self, value):
        self._continuous_period = value
    @property
    def continuous_plan_list(self):
        return self._continuous_plan_list

    @continuous_plan_list.setter
    def continuous_plan_list(self, value):
        if isinstance(value, list):
            self._continuous_plan_list = list()
            for i in value:
                if isinstance(i, ContinuousPlan):
                    self._continuous_plan_list.append(i)
                else:
                    self._continuous_plan_list.append(ContinuousPlan.from_alipay_dict(i))
    @property
    def coverage_list(self):
        return self._coverage_list

    @coverage_list.setter
    def coverage_list(self, value):
        if isinstance(value, list):
            self._coverage_list = list()
            for i in value:
                if isinstance(i, Coverage):
                    self._coverage_list.append(i)
                else:
                    self._coverage_list.append(Coverage.from_alipay_dict(i))
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def electronic_policy_url(self):
        return self._electronic_policy_url

    @electronic_policy_url.setter
    def electronic_policy_url(self, value):
        self._electronic_policy_url = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def first_premium(self):
        return self._first_premium

    @first_premium.setter
    def first_premium(self, value):
        self._first_premium = value
    @property
    def insured_time(self):
        return self._insured_time

    @insured_time.setter
    def insured_time(self, value):
        self._insured_time = value
    @property
    def issue_time(self):
        return self._issue_time

    @issue_time.setter
    def issue_time(self, value):
        self._issue_time = value
    @property
    def old_policy_no(self):
        return self._old_policy_no

    @old_policy_no.setter
    def old_policy_no(self, value):
        self._old_policy_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def pay_trade_no(self):
        return self._pay_trade_no

    @pay_trade_no.setter
    def pay_trade_no(self, value):
        self._pay_trade_no = value
    @property
    def person_list(self):
        return self._person_list

    @person_list.setter
    def person_list(self, value):
        if isinstance(value, list):
            self._person_list = list()
            for i in value:
                if isinstance(i, RelatedPerson):
                    self._person_list.append(i)
                else:
                    self._person_list.append(RelatedPerson.from_alipay_dict(i))
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def policy_type(self):
        return self._policy_type

    @policy_type.setter
    def policy_type(self, value):
        self._policy_type = value
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
    def product_scheme_code(self):
        return self._product_scheme_code

    @product_scheme_code.setter
    def product_scheme_code(self, value):
        self._product_scheme_code = value
    @property
    def source_policy_no(self):
        return self._source_policy_no

    @source_policy_no.setter
    def source_policy_no(self, value):
        self._source_policy_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value
    @property
    def surrender_amount(self):
        return self._surrender_amount

    @surrender_amount.setter
    def surrender_amount(self, value):
        self._surrender_amount = value
    @property
    def surrender_reason(self):
        return self._surrender_reason

    @surrender_reason.setter
    def surrender_reason(self, value):
        self._surrender_reason = value
    @property
    def surrender_time(self):
        return self._surrender_time

    @surrender_time.setter
    def surrender_time(self, value):
        self._surrender_time = value
    @property
    def suspended_reason(self):
        return self._suspended_reason

    @suspended_reason.setter
    def suspended_reason(self, value):
        self._suspended_reason = value
    @property
    def suspended_time(self):
        return self._suspended_time

    @suspended_time.setter
    def suspended_time(self, value):
        self._suspended_time = value
    @property
    def total_premium(self):
        return self._total_premium

    @total_premium.setter
    def total_premium(self, value):
        self._total_premium = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.continuous_frequency:
            if hasattr(self.continuous_frequency, 'to_alipay_dict'):
                params['continuous_frequency'] = self.continuous_frequency.to_alipay_dict()
            else:
                params['continuous_frequency'] = self.continuous_frequency
        if self.continuous_period:
            if hasattr(self.continuous_period, 'to_alipay_dict'):
                params['continuous_period'] = self.continuous_period.to_alipay_dict()
            else:
                params['continuous_period'] = self.continuous_period
        if self.continuous_plan_list:
            if isinstance(self.continuous_plan_list, list):
                for i in range(0, len(self.continuous_plan_list)):
                    element = self.continuous_plan_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.continuous_plan_list[i] = element.to_alipay_dict()
            if hasattr(self.continuous_plan_list, 'to_alipay_dict'):
                params['continuous_plan_list'] = self.continuous_plan_list.to_alipay_dict()
            else:
                params['continuous_plan_list'] = self.continuous_plan_list
        if self.coverage_list:
            if isinstance(self.coverage_list, list):
                for i in range(0, len(self.coverage_list)):
                    element = self.coverage_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coverage_list[i] = element.to_alipay_dict()
            if hasattr(self.coverage_list, 'to_alipay_dict'):
                params['coverage_list'] = self.coverage_list.to_alipay_dict()
            else:
                params['coverage_list'] = self.coverage_list
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.effect_end_time:
            if hasattr(self.effect_end_time, 'to_alipay_dict'):
                params['effect_end_time'] = self.effect_end_time.to_alipay_dict()
            else:
                params['effect_end_time'] = self.effect_end_time
        if self.effect_start_time:
            if hasattr(self.effect_start_time, 'to_alipay_dict'):
                params['effect_start_time'] = self.effect_start_time.to_alipay_dict()
            else:
                params['effect_start_time'] = self.effect_start_time
        if self.electronic_policy_url:
            if hasattr(self.electronic_policy_url, 'to_alipay_dict'):
                params['electronic_policy_url'] = self.electronic_policy_url.to_alipay_dict()
            else:
                params['electronic_policy_url'] = self.electronic_policy_url
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.first_premium:
            if hasattr(self.first_premium, 'to_alipay_dict'):
                params['first_premium'] = self.first_premium.to_alipay_dict()
            else:
                params['first_premium'] = self.first_premium
        if self.insured_time:
            if hasattr(self.insured_time, 'to_alipay_dict'):
                params['insured_time'] = self.insured_time.to_alipay_dict()
            else:
                params['insured_time'] = self.insured_time
        if self.issue_time:
            if hasattr(self.issue_time, 'to_alipay_dict'):
                params['issue_time'] = self.issue_time.to_alipay_dict()
            else:
                params['issue_time'] = self.issue_time
        if self.old_policy_no:
            if hasattr(self.old_policy_no, 'to_alipay_dict'):
                params['old_policy_no'] = self.old_policy_no.to_alipay_dict()
            else:
                params['old_policy_no'] = self.old_policy_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.pay_trade_no:
            if hasattr(self.pay_trade_no, 'to_alipay_dict'):
                params['pay_trade_no'] = self.pay_trade_no.to_alipay_dict()
            else:
                params['pay_trade_no'] = self.pay_trade_no
        if self.person_list:
            if isinstance(self.person_list, list):
                for i in range(0, len(self.person_list)):
                    element = self.person_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.person_list[i] = element.to_alipay_dict()
            if hasattr(self.person_list, 'to_alipay_dict'):
                params['person_list'] = self.person_list.to_alipay_dict()
            else:
                params['person_list'] = self.person_list
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.policy_type:
            if hasattr(self.policy_type, 'to_alipay_dict'):
                params['policy_type'] = self.policy_type.to_alipay_dict()
            else:
                params['policy_type'] = self.policy_type
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
        if self.product_scheme_code:
            if hasattr(self.product_scheme_code, 'to_alipay_dict'):
                params['product_scheme_code'] = self.product_scheme_code.to_alipay_dict()
            else:
                params['product_scheme_code'] = self.product_scheme_code
        if self.source_policy_no:
            if hasattr(self.source_policy_no, 'to_alipay_dict'):
                params['source_policy_no'] = self.source_policy_no.to_alipay_dict()
            else:
                params['source_policy_no'] = self.source_policy_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        if self.surrender_amount:
            if hasattr(self.surrender_amount, 'to_alipay_dict'):
                params['surrender_amount'] = self.surrender_amount.to_alipay_dict()
            else:
                params['surrender_amount'] = self.surrender_amount
        if self.surrender_reason:
            if hasattr(self.surrender_reason, 'to_alipay_dict'):
                params['surrender_reason'] = self.surrender_reason.to_alipay_dict()
            else:
                params['surrender_reason'] = self.surrender_reason
        if self.surrender_time:
            if hasattr(self.surrender_time, 'to_alipay_dict'):
                params['surrender_time'] = self.surrender_time.to_alipay_dict()
            else:
                params['surrender_time'] = self.surrender_time
        if self.suspended_reason:
            if hasattr(self.suspended_reason, 'to_alipay_dict'):
                params['suspended_reason'] = self.suspended_reason.to_alipay_dict()
            else:
                params['suspended_reason'] = self.suspended_reason
        if self.suspended_time:
            if hasattr(self.suspended_time, 'to_alipay_dict'):
                params['suspended_time'] = self.suspended_time.to_alipay_dict()
            else:
                params['suspended_time'] = self.suspended_time
        if self.total_premium:
            if hasattr(self.total_premium, 'to_alipay_dict'):
                params['total_premium'] = self.total_premium.to_alipay_dict()
            else:
                params['total_premium'] = self.total_premium
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
        o = AlipayCommerceMedicalInsurancePolicyinfoSyncModel()
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'continuous_frequency' in d:
            o.continuous_frequency = d['continuous_frequency']
        if 'continuous_period' in d:
            o.continuous_period = d['continuous_period']
        if 'continuous_plan_list' in d:
            o.continuous_plan_list = d['continuous_plan_list']
        if 'coverage_list' in d:
            o.coverage_list = d['coverage_list']
        if 'currency' in d:
            o.currency = d['currency']
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'electronic_policy_url' in d:
            o.electronic_policy_url = d['electronic_policy_url']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'first_premium' in d:
            o.first_premium = d['first_premium']
        if 'insured_time' in d:
            o.insured_time = d['insured_time']
        if 'issue_time' in d:
            o.issue_time = d['issue_time']
        if 'old_policy_no' in d:
            o.old_policy_no = d['old_policy_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'pay_trade_no' in d:
            o.pay_trade_no = d['pay_trade_no']
        if 'person_list' in d:
            o.person_list = d['person_list']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'policy_type' in d:
            o.policy_type = d['policy_type']
        if 'premium' in d:
            o.premium = d['premium']
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        if 'product_scheme_code' in d:
            o.product_scheme_code = d['product_scheme_code']
        if 'source_policy_no' in d:
            o.source_policy_no = d['source_policy_no']
        if 'status' in d:
            o.status = d['status']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        if 'surrender_amount' in d:
            o.surrender_amount = d['surrender_amount']
        if 'surrender_reason' in d:
            o.surrender_reason = d['surrender_reason']
        if 'surrender_time' in d:
            o.surrender_time = d['surrender_time']
        if 'suspended_reason' in d:
            o.suspended_reason = d['suspended_reason']
        if 'suspended_time' in d:
            o.suspended_time = d['suspended_time']
        if 'total_premium' in d:
            o.total_premium = d['total_premium']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


