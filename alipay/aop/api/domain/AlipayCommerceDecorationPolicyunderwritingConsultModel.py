#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsuredVO import InsuredVO
from alipay.aop.api.domain.PolicyOrgHolderVO import PolicyOrgHolderVO
from alipay.aop.api.domain.SubjectMatterVO import SubjectMatterVO


class AlipayCommerceDecorationPolicyunderwritingConsultModel(object):

    def __init__(self):
        self._apply_time = None
        self._insurance_company_code = None
        self._insured_list = None
        self._order_amount = None
        self._out_order_no = None
        self._policy_end_date = None
        self._policy_org_holder = None
        self._policy_start_date = None
        self._product_code = None
        self._project_id = None
        self._subject_matter = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def insurance_company_code(self):
        return self._insurance_company_code

    @insurance_company_code.setter
    def insurance_company_code(self, value):
        self._insurance_company_code = value
    @property
    def insured_list(self):
        return self._insured_list

    @insured_list.setter
    def insured_list(self, value):
        if isinstance(value, list):
            self._insured_list = list()
            for i in value:
                if isinstance(i, InsuredVO):
                    self._insured_list.append(i)
                else:
                    self._insured_list.append(InsuredVO.from_alipay_dict(i))
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def policy_end_date(self):
        return self._policy_end_date

    @policy_end_date.setter
    def policy_end_date(self, value):
        self._policy_end_date = value
    @property
    def policy_org_holder(self):
        return self._policy_org_holder

    @policy_org_holder.setter
    def policy_org_holder(self, value):
        if isinstance(value, PolicyOrgHolderVO):
            self._policy_org_holder = value
        else:
            self._policy_org_holder = PolicyOrgHolderVO.from_alipay_dict(value)
    @property
    def policy_start_date(self):
        return self._policy_start_date

    @policy_start_date.setter
    def policy_start_date(self, value):
        self._policy_start_date = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def subject_matter(self):
        return self._subject_matter

    @subject_matter.setter
    def subject_matter(self, value):
        if isinstance(value, list):
            self._subject_matter = list()
            for i in value:
                if isinstance(i, SubjectMatterVO):
                    self._subject_matter.append(i)
                else:
                    self._subject_matter.append(SubjectMatterVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.insurance_company_code:
            if hasattr(self.insurance_company_code, 'to_alipay_dict'):
                params['insurance_company_code'] = self.insurance_company_code.to_alipay_dict()
            else:
                params['insurance_company_code'] = self.insurance_company_code
        if self.insured_list:
            if isinstance(self.insured_list, list):
                for i in range(0, len(self.insured_list)):
                    element = self.insured_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.insured_list[i] = element.to_alipay_dict()
            if hasattr(self.insured_list, 'to_alipay_dict'):
                params['insured_list'] = self.insured_list.to_alipay_dict()
            else:
                params['insured_list'] = self.insured_list
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.policy_end_date:
            if hasattr(self.policy_end_date, 'to_alipay_dict'):
                params['policy_end_date'] = self.policy_end_date.to_alipay_dict()
            else:
                params['policy_end_date'] = self.policy_end_date
        if self.policy_org_holder:
            if hasattr(self.policy_org_holder, 'to_alipay_dict'):
                params['policy_org_holder'] = self.policy_org_holder.to_alipay_dict()
            else:
                params['policy_org_holder'] = self.policy_org_holder
        if self.policy_start_date:
            if hasattr(self.policy_start_date, 'to_alipay_dict'):
                params['policy_start_date'] = self.policy_start_date.to_alipay_dict()
            else:
                params['policy_start_date'] = self.policy_start_date
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.subject_matter:
            if isinstance(self.subject_matter, list):
                for i in range(0, len(self.subject_matter)):
                    element = self.subject_matter[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subject_matter[i] = element.to_alipay_dict()
            if hasattr(self.subject_matter, 'to_alipay_dict'):
                params['subject_matter'] = self.subject_matter.to_alipay_dict()
            else:
                params['subject_matter'] = self.subject_matter
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDecorationPolicyunderwritingConsultModel()
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'insurance_company_code' in d:
            o.insurance_company_code = d['insurance_company_code']
        if 'insured_list' in d:
            o.insured_list = d['insured_list']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'policy_end_date' in d:
            o.policy_end_date = d['policy_end_date']
        if 'policy_org_holder' in d:
            o.policy_org_holder = d['policy_org_holder']
        if 'policy_start_date' in d:
            o.policy_start_date = d['policy_start_date']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'subject_matter' in d:
            o.subject_matter = d['subject_matter']
        return o


