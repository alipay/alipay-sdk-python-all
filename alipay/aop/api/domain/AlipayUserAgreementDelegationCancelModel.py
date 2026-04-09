#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAgreementDelegationCancelModel(object):

    def __init__(self):
        self._agreement_no = None
        self._delegation_id = None

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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementDelegationCancelModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'delegation_id' in d:
            o.delegation_id = d['delegation_id']
        return o


