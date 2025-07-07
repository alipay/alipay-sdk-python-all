#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingBenefitaccountAccountQueryModel(object):

    def __init__(self):
        self._benefit_account_no = None
        self._publisher_user_id = None

    @property
    def benefit_account_no(self):
        return self._benefit_account_no

    @benefit_account_no.setter
    def benefit_account_no(self, value):
        self._benefit_account_no = value
    @property
    def publisher_user_id(self):
        return self._publisher_user_id

    @publisher_user_id.setter
    def publisher_user_id(self, value):
        self._publisher_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_account_no:
            if hasattr(self.benefit_account_no, 'to_alipay_dict'):
                params['benefit_account_no'] = self.benefit_account_no.to_alipay_dict()
            else:
                params['benefit_account_no'] = self.benefit_account_no
        if self.publisher_user_id:
            if hasattr(self.publisher_user_id, 'to_alipay_dict'):
                params['publisher_user_id'] = self.publisher_user_id.to_alipay_dict()
            else:
                params['publisher_user_id'] = self.publisher_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingBenefitaccountAccountQueryModel()
        if 'benefit_account_no' in d:
            o.benefit_account_no = d['benefit_account_no']
        if 'publisher_user_id' in d:
            o.publisher_user_id = d['publisher_user_id']
        return o


