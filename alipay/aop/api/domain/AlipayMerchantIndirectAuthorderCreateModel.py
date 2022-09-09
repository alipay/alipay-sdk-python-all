#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthIdentityInfo import AuthIdentityInfo
from alipay.aop.api.domain.IndirectBenefitPersonInfo import IndirectBenefitPersonInfo
from alipay.aop.api.domain.IndirectContactPersonInfo import IndirectContactPersonInfo
from alipay.aop.api.domain.IndirectExtraCredentials import IndirectExtraCredentials
from alipay.aop.api.domain.IndirectLegalPersonInfo import IndirectLegalPersonInfo


class AlipayMerchantIndirectAuthorderCreateModel(object):

    def __init__(self):
        self._auth_identity_info = None
        self._benefit_person_info = None
        self._contact_person_info = None
        self._extra_credentials = None
        self._legal_person_info = None
        self._out_biz_no = None
        self._source = None

    @property
    def auth_identity_info(self):
        return self._auth_identity_info

    @auth_identity_info.setter
    def auth_identity_info(self, value):
        if isinstance(value, AuthIdentityInfo):
            self._auth_identity_info = value
        else:
            self._auth_identity_info = AuthIdentityInfo.from_alipay_dict(value)
    @property
    def benefit_person_info(self):
        return self._benefit_person_info

    @benefit_person_info.setter
    def benefit_person_info(self, value):
        if isinstance(value, IndirectBenefitPersonInfo):
            self._benefit_person_info = value
        else:
            self._benefit_person_info = IndirectBenefitPersonInfo.from_alipay_dict(value)
    @property
    def contact_person_info(self):
        return self._contact_person_info

    @contact_person_info.setter
    def contact_person_info(self, value):
        if isinstance(value, IndirectContactPersonInfo):
            self._contact_person_info = value
        else:
            self._contact_person_info = IndirectContactPersonInfo.from_alipay_dict(value)
    @property
    def extra_credentials(self):
        return self._extra_credentials

    @extra_credentials.setter
    def extra_credentials(self, value):
        if isinstance(value, IndirectExtraCredentials):
            self._extra_credentials = value
        else:
            self._extra_credentials = IndirectExtraCredentials.from_alipay_dict(value)
    @property
    def legal_person_info(self):
        return self._legal_person_info

    @legal_person_info.setter
    def legal_person_info(self, value):
        if isinstance(value, IndirectLegalPersonInfo):
            self._legal_person_info = value
        else:
            self._legal_person_info = IndirectLegalPersonInfo.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_identity_info:
            if hasattr(self.auth_identity_info, 'to_alipay_dict'):
                params['auth_identity_info'] = self.auth_identity_info.to_alipay_dict()
            else:
                params['auth_identity_info'] = self.auth_identity_info
        if self.benefit_person_info:
            if hasattr(self.benefit_person_info, 'to_alipay_dict'):
                params['benefit_person_info'] = self.benefit_person_info.to_alipay_dict()
            else:
                params['benefit_person_info'] = self.benefit_person_info
        if self.contact_person_info:
            if hasattr(self.contact_person_info, 'to_alipay_dict'):
                params['contact_person_info'] = self.contact_person_info.to_alipay_dict()
            else:
                params['contact_person_info'] = self.contact_person_info
        if self.extra_credentials:
            if hasattr(self.extra_credentials, 'to_alipay_dict'):
                params['extra_credentials'] = self.extra_credentials.to_alipay_dict()
            else:
                params['extra_credentials'] = self.extra_credentials
        if self.legal_person_info:
            if hasattr(self.legal_person_info, 'to_alipay_dict'):
                params['legal_person_info'] = self.legal_person_info.to_alipay_dict()
            else:
                params['legal_person_info'] = self.legal_person_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectAuthorderCreateModel()
        if 'auth_identity_info' in d:
            o.auth_identity_info = d['auth_identity_info']
        if 'benefit_person_info' in d:
            o.benefit_person_info = d['benefit_person_info']
        if 'contact_person_info' in d:
            o.contact_person_info = d['contact_person_info']
        if 'extra_credentials' in d:
            o.extra_credentials = d['extra_credentials']
        if 'legal_person_info' in d:
            o.legal_person_info = d['legal_person_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'source' in d:
            o.source = d['source']
        return o


