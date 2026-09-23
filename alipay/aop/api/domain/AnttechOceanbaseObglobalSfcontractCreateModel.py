#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalSfcontractCreateModel(object):

    def __init__(self):
        self._applicant_work_no = None
        self._audit_csm_work_no = None
        self._contract_create_system = None
        self._contract_title = None
        self._contract_type = None
        self._external_contract_id = None
        self._final_admin_email = None
        self._final_admin_email_source_code = None
        self._leads_code = None
        self._our_sign_subject = None
        self._quotation_application_item_no = None
        self._request_id = None

    @property
    def applicant_work_no(self):
        return self._applicant_work_no

    @applicant_work_no.setter
    def applicant_work_no(self, value):
        self._applicant_work_no = value
    @property
    def audit_csm_work_no(self):
        return self._audit_csm_work_no

    @audit_csm_work_no.setter
    def audit_csm_work_no(self, value):
        self._audit_csm_work_no = value
    @property
    def contract_create_system(self):
        return self._contract_create_system

    @contract_create_system.setter
    def contract_create_system(self, value):
        self._contract_create_system = value
    @property
    def contract_title(self):
        return self._contract_title

    @contract_title.setter
    def contract_title(self, value):
        self._contract_title = value
    @property
    def contract_type(self):
        return self._contract_type

    @contract_type.setter
    def contract_type(self, value):
        self._contract_type = value
    @property
    def external_contract_id(self):
        return self._external_contract_id

    @external_contract_id.setter
    def external_contract_id(self, value):
        self._external_contract_id = value
    @property
    def final_admin_email(self):
        return self._final_admin_email

    @final_admin_email.setter
    def final_admin_email(self, value):
        self._final_admin_email = value
    @property
    def final_admin_email_source_code(self):
        return self._final_admin_email_source_code

    @final_admin_email_source_code.setter
    def final_admin_email_source_code(self, value):
        self._final_admin_email_source_code = value
    @property
    def leads_code(self):
        return self._leads_code

    @leads_code.setter
    def leads_code(self, value):
        self._leads_code = value
    @property
    def our_sign_subject(self):
        return self._our_sign_subject

    @our_sign_subject.setter
    def our_sign_subject(self, value):
        self._our_sign_subject = value
    @property
    def quotation_application_item_no(self):
        return self._quotation_application_item_no

    @quotation_application_item_no.setter
    def quotation_application_item_no(self, value):
        self._quotation_application_item_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant_work_no:
            if hasattr(self.applicant_work_no, 'to_alipay_dict'):
                params['applicant_work_no'] = self.applicant_work_no.to_alipay_dict()
            else:
                params['applicant_work_no'] = self.applicant_work_no
        if self.audit_csm_work_no:
            if hasattr(self.audit_csm_work_no, 'to_alipay_dict'):
                params['audit_csm_work_no'] = self.audit_csm_work_no.to_alipay_dict()
            else:
                params['audit_csm_work_no'] = self.audit_csm_work_no
        if self.contract_create_system:
            if hasattr(self.contract_create_system, 'to_alipay_dict'):
                params['contract_create_system'] = self.contract_create_system.to_alipay_dict()
            else:
                params['contract_create_system'] = self.contract_create_system
        if self.contract_title:
            if hasattr(self.contract_title, 'to_alipay_dict'):
                params['contract_title'] = self.contract_title.to_alipay_dict()
            else:
                params['contract_title'] = self.contract_title
        if self.contract_type:
            if hasattr(self.contract_type, 'to_alipay_dict'):
                params['contract_type'] = self.contract_type.to_alipay_dict()
            else:
                params['contract_type'] = self.contract_type
        if self.external_contract_id:
            if hasattr(self.external_contract_id, 'to_alipay_dict'):
                params['external_contract_id'] = self.external_contract_id.to_alipay_dict()
            else:
                params['external_contract_id'] = self.external_contract_id
        if self.final_admin_email:
            if hasattr(self.final_admin_email, 'to_alipay_dict'):
                params['final_admin_email'] = self.final_admin_email.to_alipay_dict()
            else:
                params['final_admin_email'] = self.final_admin_email
        if self.final_admin_email_source_code:
            if hasattr(self.final_admin_email_source_code, 'to_alipay_dict'):
                params['final_admin_email_source_code'] = self.final_admin_email_source_code.to_alipay_dict()
            else:
                params['final_admin_email_source_code'] = self.final_admin_email_source_code
        if self.leads_code:
            if hasattr(self.leads_code, 'to_alipay_dict'):
                params['leads_code'] = self.leads_code.to_alipay_dict()
            else:
                params['leads_code'] = self.leads_code
        if self.our_sign_subject:
            if hasattr(self.our_sign_subject, 'to_alipay_dict'):
                params['our_sign_subject'] = self.our_sign_subject.to_alipay_dict()
            else:
                params['our_sign_subject'] = self.our_sign_subject
        if self.quotation_application_item_no:
            if hasattr(self.quotation_application_item_no, 'to_alipay_dict'):
                params['quotation_application_item_no'] = self.quotation_application_item_no.to_alipay_dict()
            else:
                params['quotation_application_item_no'] = self.quotation_application_item_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfcontractCreateModel()
        if 'applicant_work_no' in d:
            o.applicant_work_no = d['applicant_work_no']
        if 'audit_csm_work_no' in d:
            o.audit_csm_work_no = d['audit_csm_work_no']
        if 'contract_create_system' in d:
            o.contract_create_system = d['contract_create_system']
        if 'contract_title' in d:
            o.contract_title = d['contract_title']
        if 'contract_type' in d:
            o.contract_type = d['contract_type']
        if 'external_contract_id' in d:
            o.external_contract_id = d['external_contract_id']
        if 'final_admin_email' in d:
            o.final_admin_email = d['final_admin_email']
        if 'final_admin_email_source_code' in d:
            o.final_admin_email_source_code = d['final_admin_email_source_code']
        if 'leads_code' in d:
            o.leads_code = d['leads_code']
        if 'our_sign_subject' in d:
            o.our_sign_subject = d['our_sign_subject']
        if 'quotation_application_item_no' in d:
            o.quotation_application_item_no = d['quotation_application_item_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


