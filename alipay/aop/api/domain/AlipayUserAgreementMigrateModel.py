#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAgreementMigrateModel(object):

    def __init__(self):
        self._agreement_no = None
        self._target_app_id = None
        self._target_invoke_app_id = None
        self._target_partner_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def target_app_id(self):
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, value):
        self._target_app_id = value
    @property
    def target_invoke_app_id(self):
        return self._target_invoke_app_id

    @target_invoke_app_id.setter
    def target_invoke_app_id(self, value):
        self._target_invoke_app_id = value
    @property
    def target_partner_id(self):
        return self._target_partner_id

    @target_partner_id.setter
    def target_partner_id(self, value):
        self._target_partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.target_app_id:
            if hasattr(self.target_app_id, 'to_alipay_dict'):
                params['target_app_id'] = self.target_app_id.to_alipay_dict()
            else:
                params['target_app_id'] = self.target_app_id
        if self.target_invoke_app_id:
            if hasattr(self.target_invoke_app_id, 'to_alipay_dict'):
                params['target_invoke_app_id'] = self.target_invoke_app_id.to_alipay_dict()
            else:
                params['target_invoke_app_id'] = self.target_invoke_app_id
        if self.target_partner_id:
            if hasattr(self.target_partner_id, 'to_alipay_dict'):
                params['target_partner_id'] = self.target_partner_id.to_alipay_dict()
            else:
                params['target_partner_id'] = self.target_partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementMigrateModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'target_app_id' in d:
            o.target_app_id = d['target_app_id']
        if 'target_invoke_app_id' in d:
            o.target_invoke_app_id = d['target_invoke_app_id']
        if 'target_partner_id' in d:
            o.target_partner_id = d['target_partner_id']
        return o


