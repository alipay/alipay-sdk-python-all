#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinAttachment import FinAttachment
from alipay.aop.api.domain.CompanyInformation import CompanyInformation
from alipay.aop.api.domain.PersonInfo import PersonInfo
from alipay.aop.api.domain.CreditQuotaDetail import CreditQuotaDetail


class AnttechBlockchainFinanceTruspleCreditgrantapplySubmitModel(object):

    def __init__(self):
        self._attachments = None
        self._borrower_type = None
        self._company_credit_inquiry_request_id = None
        self._company_info = None
        self._ext_info = None
        self._external_credit_grant_id = None
        self._external_product_code = None
        self._external_user_id = None
        self._inst_code = None
        self._legal_person_info = None
        self._personal_credit_inquiry_request_id = None
        self._quota_details = None
        self._risk_info = None

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, FinAttachment):
                    self._attachments.append(i)
                else:
                    self._attachments.append(FinAttachment.from_alipay_dict(i))
    @property
    def borrower_type(self):
        return self._borrower_type

    @borrower_type.setter
    def borrower_type(self, value):
        self._borrower_type = value
    @property
    def company_credit_inquiry_request_id(self):
        return self._company_credit_inquiry_request_id

    @company_credit_inquiry_request_id.setter
    def company_credit_inquiry_request_id(self, value):
        self._company_credit_inquiry_request_id = value
    @property
    def company_info(self):
        return self._company_info

    @company_info.setter
    def company_info(self, value):
        if isinstance(value, CompanyInformation):
            self._company_info = value
        else:
            self._company_info = CompanyInformation.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def external_credit_grant_id(self):
        return self._external_credit_grant_id

    @external_credit_grant_id.setter
    def external_credit_grant_id(self, value):
        self._external_credit_grant_id = value
    @property
    def external_product_code(self):
        return self._external_product_code

    @external_product_code.setter
    def external_product_code(self, value):
        self._external_product_code = value
    @property
    def external_user_id(self):
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, value):
        self._external_user_id = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def legal_person_info(self):
        return self._legal_person_info

    @legal_person_info.setter
    def legal_person_info(self, value):
        if isinstance(value, PersonInfo):
            self._legal_person_info = value
        else:
            self._legal_person_info = PersonInfo.from_alipay_dict(value)
    @property
    def personal_credit_inquiry_request_id(self):
        return self._personal_credit_inquiry_request_id

    @personal_credit_inquiry_request_id.setter
    def personal_credit_inquiry_request_id(self, value):
        self._personal_credit_inquiry_request_id = value
    @property
    def quota_details(self):
        return self._quota_details

    @quota_details.setter
    def quota_details(self, value):
        if isinstance(value, list):
            self._quota_details = list()
            for i in value:
                if isinstance(i, CreditQuotaDetail):
                    self._quota_details.append(i)
                else:
                    self._quota_details.append(CreditQuotaDetail.from_alipay_dict(i))
    @property
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        self._risk_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.borrower_type:
            if hasattr(self.borrower_type, 'to_alipay_dict'):
                params['borrower_type'] = self.borrower_type.to_alipay_dict()
            else:
                params['borrower_type'] = self.borrower_type
        if self.company_credit_inquiry_request_id:
            if hasattr(self.company_credit_inquiry_request_id, 'to_alipay_dict'):
                params['company_credit_inquiry_request_id'] = self.company_credit_inquiry_request_id.to_alipay_dict()
            else:
                params['company_credit_inquiry_request_id'] = self.company_credit_inquiry_request_id
        if self.company_info:
            if hasattr(self.company_info, 'to_alipay_dict'):
                params['company_info'] = self.company_info.to_alipay_dict()
            else:
                params['company_info'] = self.company_info
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.external_credit_grant_id:
            if hasattr(self.external_credit_grant_id, 'to_alipay_dict'):
                params['external_credit_grant_id'] = self.external_credit_grant_id.to_alipay_dict()
            else:
                params['external_credit_grant_id'] = self.external_credit_grant_id
        if self.external_product_code:
            if hasattr(self.external_product_code, 'to_alipay_dict'):
                params['external_product_code'] = self.external_product_code.to_alipay_dict()
            else:
                params['external_product_code'] = self.external_product_code
        if self.external_user_id:
            if hasattr(self.external_user_id, 'to_alipay_dict'):
                params['external_user_id'] = self.external_user_id.to_alipay_dict()
            else:
                params['external_user_id'] = self.external_user_id
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.legal_person_info:
            if hasattr(self.legal_person_info, 'to_alipay_dict'):
                params['legal_person_info'] = self.legal_person_info.to_alipay_dict()
            else:
                params['legal_person_info'] = self.legal_person_info
        if self.personal_credit_inquiry_request_id:
            if hasattr(self.personal_credit_inquiry_request_id, 'to_alipay_dict'):
                params['personal_credit_inquiry_request_id'] = self.personal_credit_inquiry_request_id.to_alipay_dict()
            else:
                params['personal_credit_inquiry_request_id'] = self.personal_credit_inquiry_request_id
        if self.quota_details:
            if isinstance(self.quota_details, list):
                for i in range(0, len(self.quota_details)):
                    element = self.quota_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.quota_details[i] = element.to_alipay_dict()
            if hasattr(self.quota_details, 'to_alipay_dict'):
                params['quota_details'] = self.quota_details.to_alipay_dict()
            else:
                params['quota_details'] = self.quota_details
        if self.risk_info:
            if hasattr(self.risk_info, 'to_alipay_dict'):
                params['risk_info'] = self.risk_info.to_alipay_dict()
            else:
                params['risk_info'] = self.risk_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTruspleCreditgrantapplySubmitModel()
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'borrower_type' in d:
            o.borrower_type = d['borrower_type']
        if 'company_credit_inquiry_request_id' in d:
            o.company_credit_inquiry_request_id = d['company_credit_inquiry_request_id']
        if 'company_info' in d:
            o.company_info = d['company_info']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'external_credit_grant_id' in d:
            o.external_credit_grant_id = d['external_credit_grant_id']
        if 'external_product_code' in d:
            o.external_product_code = d['external_product_code']
        if 'external_user_id' in d:
            o.external_user_id = d['external_user_id']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'legal_person_info' in d:
            o.legal_person_info = d['legal_person_info']
        if 'personal_credit_inquiry_request_id' in d:
            o.personal_credit_inquiry_request_id = d['personal_credit_inquiry_request_id']
        if 'quota_details' in d:
            o.quota_details = d['quota_details']
        if 'risk_info' in d:
            o.risk_info = d['risk_info']
        return o


