#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAgreementDelegationQueryModel(object):

    def __init__(self):
        self._agreement_no = None
        self._delegation_id = None
        self._external_agreement_no = None
        self._external_delegation_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def delegation_id(self):
        return self._delegation_id

    @delegation_id.setter
    def delegation_id(self, value):
        self._delegation_id = value
    @property
    def external_agreement_no(self):
        return self._external_agreement_no

    @external_agreement_no.setter
    def external_agreement_no(self, value):
        self._external_agreement_no = value
    @property
    def external_delegation_id(self):
        return self._external_delegation_id

    @external_delegation_id.setter
    def external_delegation_id(self, value):
        self._external_delegation_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.delegation_id:
            if hasattr(self.delegation_id, 'to_alipay_dict'):
                params['delegation_id'] = self.delegation_id.to_alipay_dict()
            else:
                params['delegation_id'] = self.delegation_id
        if self.external_agreement_no:
            if hasattr(self.external_agreement_no, 'to_alipay_dict'):
                params['external_agreement_no'] = self.external_agreement_no.to_alipay_dict()
            else:
                params['external_agreement_no'] = self.external_agreement_no
        if self.external_delegation_id:
            if hasattr(self.external_delegation_id, 'to_alipay_dict'):
                params['external_delegation_id'] = self.external_delegation_id.to_alipay_dict()
            else:
                params['external_delegation_id'] = self.external_delegation_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementDelegationQueryModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'delegation_id' in d:
            o.delegation_id = d['delegation_id']
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'external_delegation_id' in d:
            o.external_delegation_id = d['external_delegation_id']
        return o


