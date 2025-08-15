#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessParams import AccessParams


class AlipayUserAgreementAgentSignModel(object):

    def __init__(self):
        self._access_params = None
        self._external_agreement_no = None
        self._external_logon_id = None
        self._personal_product_code = None

    @property
    def access_params(self):
        return self._access_params

    @access_params.setter
    def access_params(self, value):
        if isinstance(value, AccessParams):
            self._access_params = value
        else:
            self._access_params = AccessParams.from_alipay_dict(value)
    @property
    def external_agreement_no(self):
        return self._external_agreement_no

    @external_agreement_no.setter
    def external_agreement_no(self, value):
        self._external_agreement_no = value
    @property
    def external_logon_id(self):
        return self._external_logon_id

    @external_logon_id.setter
    def external_logon_id(self, value):
        self._external_logon_id = value
    @property
    def personal_product_code(self):
        return self._personal_product_code

    @personal_product_code.setter
    def personal_product_code(self, value):
        self._personal_product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_params:
            if hasattr(self.access_params, 'to_alipay_dict'):
                params['access_params'] = self.access_params.to_alipay_dict()
            else:
                params['access_params'] = self.access_params
        if self.external_agreement_no:
            if hasattr(self.external_agreement_no, 'to_alipay_dict'):
                params['external_agreement_no'] = self.external_agreement_no.to_alipay_dict()
            else:
                params['external_agreement_no'] = self.external_agreement_no
        if self.external_logon_id:
            if hasattr(self.external_logon_id, 'to_alipay_dict'):
                params['external_logon_id'] = self.external_logon_id.to_alipay_dict()
            else:
                params['external_logon_id'] = self.external_logon_id
        if self.personal_product_code:
            if hasattr(self.personal_product_code, 'to_alipay_dict'):
                params['personal_product_code'] = self.personal_product_code.to_alipay_dict()
            else:
                params['personal_product_code'] = self.personal_product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementAgentSignModel()
        if 'access_params' in d:
            o.access_params = d['access_params']
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'external_logon_id' in d:
            o.external_logon_id = d['external_logon_id']
        if 'personal_product_code' in d:
            o.personal_product_code = d['personal_product_code']
        return o


