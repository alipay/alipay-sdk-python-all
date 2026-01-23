#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsuranceMaterialInfo import InsuranceMaterialInfo
from alipay.aop.api.domain.InsurancePreAuthInfo import InsurancePreAuthInfo
from alipay.aop.api.domain.InsuranceVisitInfo import InsuranceVisitInfo


class AlipayCommerceMedicalInsuranceTpaclaimstatusNotifyModel(object):

    def __init__(self):
        self._apply_time = None
        self._biz_no = None
        self._cert_no = None
        self._cert_type = None
        self._claim_amount = None
        self._claim_application_biz_no = None
        self._claim_application_form_url = None
        self._claim_no = None
        self._claim_note_url = None
        self._claim_status = None
        self._company_type = None
        self._direct_pay_quota = None
        self._dplan_code = None
        self._dplan_name = None
        self._insured_cert_no = None
        self._insured_cert_type = None
        self._insured_name = None
        self._material_list = None
        self._name = None
        self._open_id = None
        self._policy_no = None
        self._pre_auth_info_list = None
        self._reject_reason = None
        self._tpa_id = None
        self._user_id = None
        self._visit_info = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def claim_amount(self):
        return self._claim_amount

    @claim_amount.setter
    def claim_amount(self, value):
        self._claim_amount = value
    @property
    def claim_application_biz_no(self):
        return self._claim_application_biz_no

    @claim_application_biz_no.setter
    def claim_application_biz_no(self, value):
        self._claim_application_biz_no = value
    @property
    def claim_application_form_url(self):
        return self._claim_application_form_url

    @claim_application_form_url.setter
    def claim_application_form_url(self, value):
        self._claim_application_form_url = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_note_url(self):
        return self._claim_note_url

    @claim_note_url.setter
    def claim_note_url(self, value):
        self._claim_note_url = value
    @property
    def claim_status(self):
        return self._claim_status

    @claim_status.setter
    def claim_status(self, value):
        self._claim_status = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def direct_pay_quota(self):
        return self._direct_pay_quota

    @direct_pay_quota.setter
    def direct_pay_quota(self, value):
        self._direct_pay_quota = value
    @property
    def dplan_code(self):
        return self._dplan_code

    @dplan_code.setter
    def dplan_code(self, value):
        self._dplan_code = value
    @property
    def dplan_name(self):
        return self._dplan_name

    @dplan_name.setter
    def dplan_name(self, value):
        self._dplan_name = value
    @property
    def insured_cert_no(self):
        return self._insured_cert_no

    @insured_cert_no.setter
    def insured_cert_no(self, value):
        self._insured_cert_no = value
    @property
    def insured_cert_type(self):
        return self._insured_cert_type

    @insured_cert_type.setter
    def insured_cert_type(self, value):
        self._insured_cert_type = value
    @property
    def insured_name(self):
        return self._insured_name

    @insured_name.setter
    def insured_name(self, value):
        self._insured_name = value
    @property
    def material_list(self):
        return self._material_list

    @material_list.setter
    def material_list(self, value):
        if isinstance(value, list):
            self._material_list = list()
            for i in value:
                if isinstance(i, InsuranceMaterialInfo):
                    self._material_list.append(i)
                else:
                    self._material_list.append(InsuranceMaterialInfo.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def pre_auth_info_list(self):
        return self._pre_auth_info_list

    @pre_auth_info_list.setter
    def pre_auth_info_list(self, value):
        if isinstance(value, list):
            self._pre_auth_info_list = list()
            for i in value:
                if isinstance(i, InsurancePreAuthInfo):
                    self._pre_auth_info_list.append(i)
                else:
                    self._pre_auth_info_list.append(InsurancePreAuthInfo.from_alipay_dict(i))
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def tpa_id(self):
        return self._tpa_id

    @tpa_id.setter
    def tpa_id(self, value):
        self._tpa_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def visit_info(self):
        return self._visit_info

    @visit_info.setter
    def visit_info(self, value):
        if isinstance(value, InsuranceVisitInfo):
            self._visit_info = value
        else:
            self._visit_info = InsuranceVisitInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.claim_amount:
            if hasattr(self.claim_amount, 'to_alipay_dict'):
                params['claim_amount'] = self.claim_amount.to_alipay_dict()
            else:
                params['claim_amount'] = self.claim_amount
        if self.claim_application_biz_no:
            if hasattr(self.claim_application_biz_no, 'to_alipay_dict'):
                params['claim_application_biz_no'] = self.claim_application_biz_no.to_alipay_dict()
            else:
                params['claim_application_biz_no'] = self.claim_application_biz_no
        if self.claim_application_form_url:
            if hasattr(self.claim_application_form_url, 'to_alipay_dict'):
                params['claim_application_form_url'] = self.claim_application_form_url.to_alipay_dict()
            else:
                params['claim_application_form_url'] = self.claim_application_form_url
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_note_url:
            if hasattr(self.claim_note_url, 'to_alipay_dict'):
                params['claim_note_url'] = self.claim_note_url.to_alipay_dict()
            else:
                params['claim_note_url'] = self.claim_note_url
        if self.claim_status:
            if hasattr(self.claim_status, 'to_alipay_dict'):
                params['claim_status'] = self.claim_status.to_alipay_dict()
            else:
                params['claim_status'] = self.claim_status
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.direct_pay_quota:
            if hasattr(self.direct_pay_quota, 'to_alipay_dict'):
                params['direct_pay_quota'] = self.direct_pay_quota.to_alipay_dict()
            else:
                params['direct_pay_quota'] = self.direct_pay_quota
        if self.dplan_code:
            if hasattr(self.dplan_code, 'to_alipay_dict'):
                params['dplan_code'] = self.dplan_code.to_alipay_dict()
            else:
                params['dplan_code'] = self.dplan_code
        if self.dplan_name:
            if hasattr(self.dplan_name, 'to_alipay_dict'):
                params['dplan_name'] = self.dplan_name.to_alipay_dict()
            else:
                params['dplan_name'] = self.dplan_name
        if self.insured_cert_no:
            if hasattr(self.insured_cert_no, 'to_alipay_dict'):
                params['insured_cert_no'] = self.insured_cert_no.to_alipay_dict()
            else:
                params['insured_cert_no'] = self.insured_cert_no
        if self.insured_cert_type:
            if hasattr(self.insured_cert_type, 'to_alipay_dict'):
                params['insured_cert_type'] = self.insured_cert_type.to_alipay_dict()
            else:
                params['insured_cert_type'] = self.insured_cert_type
        if self.insured_name:
            if hasattr(self.insured_name, 'to_alipay_dict'):
                params['insured_name'] = self.insured_name.to_alipay_dict()
            else:
                params['insured_name'] = self.insured_name
        if self.material_list:
            if isinstance(self.material_list, list):
                for i in range(0, len(self.material_list)):
                    element = self.material_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_list[i] = element.to_alipay_dict()
            if hasattr(self.material_list, 'to_alipay_dict'):
                params['material_list'] = self.material_list.to_alipay_dict()
            else:
                params['material_list'] = self.material_list
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.pre_auth_info_list:
            if isinstance(self.pre_auth_info_list, list):
                for i in range(0, len(self.pre_auth_info_list)):
                    element = self.pre_auth_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pre_auth_info_list[i] = element.to_alipay_dict()
            if hasattr(self.pre_auth_info_list, 'to_alipay_dict'):
                params['pre_auth_info_list'] = self.pre_auth_info_list.to_alipay_dict()
            else:
                params['pre_auth_info_list'] = self.pre_auth_info_list
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.tpa_id:
            if hasattr(self.tpa_id, 'to_alipay_dict'):
                params['tpa_id'] = self.tpa_id.to_alipay_dict()
            else:
                params['tpa_id'] = self.tpa_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.visit_info:
            if hasattr(self.visit_info, 'to_alipay_dict'):
                params['visit_info'] = self.visit_info.to_alipay_dict()
            else:
                params['visit_info'] = self.visit_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceTpaclaimstatusNotifyModel()
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'claim_amount' in d:
            o.claim_amount = d['claim_amount']
        if 'claim_application_biz_no' in d:
            o.claim_application_biz_no = d['claim_application_biz_no']
        if 'claim_application_form_url' in d:
            o.claim_application_form_url = d['claim_application_form_url']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_note_url' in d:
            o.claim_note_url = d['claim_note_url']
        if 'claim_status' in d:
            o.claim_status = d['claim_status']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'direct_pay_quota' in d:
            o.direct_pay_quota = d['direct_pay_quota']
        if 'dplan_code' in d:
            o.dplan_code = d['dplan_code']
        if 'dplan_name' in d:
            o.dplan_name = d['dplan_name']
        if 'insured_cert_no' in d:
            o.insured_cert_no = d['insured_cert_no']
        if 'insured_cert_type' in d:
            o.insured_cert_type = d['insured_cert_type']
        if 'insured_name' in d:
            o.insured_name = d['insured_name']
        if 'material_list' in d:
            o.material_list = d['material_list']
        if 'name' in d:
            o.name = d['name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'pre_auth_info_list' in d:
            o.pre_auth_info_list = d['pre_auth_info_list']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'tpa_id' in d:
            o.tpa_id = d['tpa_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'visit_info' in d:
            o.visit_info = d['visit_info']
        return o


