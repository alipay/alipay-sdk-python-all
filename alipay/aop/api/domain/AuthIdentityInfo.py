#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndirectCertificateInfo import IndirectCertificateInfo
from alipay.aop.api.domain.IndirectFinancialOrgInfo import IndirectFinancialOrgInfo
from alipay.aop.api.domain.IndirectQualificationInfo import IndirectQualificationInfo
from alipay.aop.api.domain.IndirectSupportCredentials import IndirectSupportCredentials


class AuthIdentityInfo(object):

    def __init__(self):
        self._certificate_info = None
        self._certificate_type = None
        self._employer_letter_img = None
        self._financial_org_info = None
        self._identity_type = None
        self._is_financial_org = None
        self._qualification_info_list = None
        self._support_credentials = None

    @property
    def certificate_info(self):
        return self._certificate_info

    @certificate_info.setter
    def certificate_info(self, value):
        if isinstance(value, IndirectCertificateInfo):
            self._certificate_info = value
        else:
            self._certificate_info = IndirectCertificateInfo.from_alipay_dict(value)
    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value
    @property
    def employer_letter_img(self):
        return self._employer_letter_img

    @employer_letter_img.setter
    def employer_letter_img(self, value):
        self._employer_letter_img = value
    @property
    def financial_org_info(self):
        return self._financial_org_info

    @financial_org_info.setter
    def financial_org_info(self, value):
        if isinstance(value, IndirectFinancialOrgInfo):
            self._financial_org_info = value
        else:
            self._financial_org_info = IndirectFinancialOrgInfo.from_alipay_dict(value)
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def is_financial_org(self):
        return self._is_financial_org

    @is_financial_org.setter
    def is_financial_org(self, value):
        self._is_financial_org = value
    @property
    def qualification_info_list(self):
        return self._qualification_info_list

    @qualification_info_list.setter
    def qualification_info_list(self, value):
        if isinstance(value, list):
            self._qualification_info_list = list()
            for i in value:
                if isinstance(i, IndirectQualificationInfo):
                    self._qualification_info_list.append(i)
                else:
                    self._qualification_info_list.append(IndirectQualificationInfo.from_alipay_dict(i))
    @property
    def support_credentials(self):
        return self._support_credentials

    @support_credentials.setter
    def support_credentials(self, value):
        if isinstance(value, IndirectSupportCredentials):
            self._support_credentials = value
        else:
            self._support_credentials = IndirectSupportCredentials.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_info:
            if hasattr(self.certificate_info, 'to_alipay_dict'):
                params['certificate_info'] = self.certificate_info.to_alipay_dict()
            else:
                params['certificate_info'] = self.certificate_info
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        if self.employer_letter_img:
            if hasattr(self.employer_letter_img, 'to_alipay_dict'):
                params['employer_letter_img'] = self.employer_letter_img.to_alipay_dict()
            else:
                params['employer_letter_img'] = self.employer_letter_img
        if self.financial_org_info:
            if hasattr(self.financial_org_info, 'to_alipay_dict'):
                params['financial_org_info'] = self.financial_org_info.to_alipay_dict()
            else:
                params['financial_org_info'] = self.financial_org_info
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.is_financial_org:
            if hasattr(self.is_financial_org, 'to_alipay_dict'):
                params['is_financial_org'] = self.is_financial_org.to_alipay_dict()
            else:
                params['is_financial_org'] = self.is_financial_org
        if self.qualification_info_list:
            if isinstance(self.qualification_info_list, list):
                for i in range(0, len(self.qualification_info_list)):
                    element = self.qualification_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qualification_info_list[i] = element.to_alipay_dict()
            if hasattr(self.qualification_info_list, 'to_alipay_dict'):
                params['qualification_info_list'] = self.qualification_info_list.to_alipay_dict()
            else:
                params['qualification_info_list'] = self.qualification_info_list
        if self.support_credentials:
            if hasattr(self.support_credentials, 'to_alipay_dict'):
                params['support_credentials'] = self.support_credentials.to_alipay_dict()
            else:
                params['support_credentials'] = self.support_credentials
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthIdentityInfo()
        if 'certificate_info' in d:
            o.certificate_info = d['certificate_info']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'employer_letter_img' in d:
            o.employer_letter_img = d['employer_letter_img']
        if 'financial_org_info' in d:
            o.financial_org_info = d['financial_org_info']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'is_financial_org' in d:
            o.is_financial_org = d['is_financial_org']
        if 'qualification_info_list' in d:
            o.qualification_info_list = d['qualification_info_list']
        if 'support_credentials' in d:
            o.support_credentials = d['support_credentials']
        return o


