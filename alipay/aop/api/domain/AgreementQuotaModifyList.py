#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ModifyQuotaDetails import ModifyQuotaDetails


class AgreementQuotaModifyList(object):

    def __init__(self):
        self._agreement_no = None
        self._quota_details = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def quota_details(self):
        return self._quota_details

    @quota_details.setter
    def quota_details(self, value):
        if isinstance(value, list):
            self._quota_details = list()
            for i in value:
                if isinstance(i, ModifyQuotaDetails):
                    self._quota_details.append(i)
                else:
                    self._quota_details.append(ModifyQuotaDetails.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgreementQuotaModifyList()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'quota_details' in d:
            o.quota_details = d['quota_details']
        return o


