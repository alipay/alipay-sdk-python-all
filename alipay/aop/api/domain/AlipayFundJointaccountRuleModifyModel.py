#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JointAccountQuotaDTO import JointAccountQuotaDTO
from alipay.aop.api.domain.AuthorizedRuleDTO import AuthorizedRuleDTO


class AlipayFundJointaccountRuleModifyModel(object):

    def __init__(self):
        self._account_id = None
        self._account_name = None
        self._account_quota = None
        self._agreement_no = None
        self._authorized_rule = None
        self._biz_scene = None
        self._product_code = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_quota(self):
        return self._account_quota

    @account_quota.setter
    def account_quota(self, value):
        if isinstance(value, list):
            self._account_quota = list()
            for i in value:
                if isinstance(i, JointAccountQuotaDTO):
                    self._account_quota.append(i)
                else:
                    self._account_quota.append(JointAccountQuotaDTO.from_alipay_dict(i))
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def authorized_rule(self):
        return self._authorized_rule

    @authorized_rule.setter
    def authorized_rule(self, value):
        if isinstance(value, AuthorizedRuleDTO):
            self._authorized_rule = value
        else:
            self._authorized_rule = AuthorizedRuleDTO.from_alipay_dict(value)
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_quota:
            if isinstance(self.account_quota, list):
                for i in range(0, len(self.account_quota)):
                    element = self.account_quota[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.account_quota[i] = element.to_alipay_dict()
            if hasattr(self.account_quota, 'to_alipay_dict'):
                params['account_quota'] = self.account_quota.to_alipay_dict()
            else:
                params['account_quota'] = self.account_quota
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.authorized_rule:
            if hasattr(self.authorized_rule, 'to_alipay_dict'):
                params['authorized_rule'] = self.authorized_rule.to_alipay_dict()
            else:
                params['authorized_rule'] = self.authorized_rule
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundJointaccountRuleModifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_quota' in d:
            o.account_quota = d['account_quota']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'authorized_rule' in d:
            o.authorized_rule = d['authorized_rule']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


