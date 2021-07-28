#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessParams import AccessParams
from alipay.aop.api.domain.PeriodRuleParams import PeriodRuleParams
from alipay.aop.api.domain.SignMerchantParams import SignMerchantParams


class SignParams(object):

    def __init__(self):
        self._access_params = None
        self._allow_huazhi_degrade = None
        self._external_agreement_no = None
        self._external_logon_id = None
        self._period_rule_params = None
        self._personal_product_code = None
        self._sign_notify_url = None
        self._sign_scene = None
        self._sub_merchant = None

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
    def allow_huazhi_degrade(self):
        return self._allow_huazhi_degrade

    @allow_huazhi_degrade.setter
    def allow_huazhi_degrade(self, value):
        self._allow_huazhi_degrade = value
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
    def period_rule_params(self):
        return self._period_rule_params

    @period_rule_params.setter
    def period_rule_params(self, value):
        if isinstance(value, PeriodRuleParams):
            self._period_rule_params = value
        else:
            self._period_rule_params = PeriodRuleParams.from_alipay_dict(value)
    @property
    def personal_product_code(self):
        return self._personal_product_code

    @personal_product_code.setter
    def personal_product_code(self, value):
        self._personal_product_code = value
    @property
    def sign_notify_url(self):
        return self._sign_notify_url

    @sign_notify_url.setter
    def sign_notify_url(self, value):
        self._sign_notify_url = value
    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, SignMerchantParams):
            self._sub_merchant = value
        else:
            self._sub_merchant = SignMerchantParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.access_params:
            if hasattr(self.access_params, 'to_alipay_dict'):
                params['access_params'] = self.access_params.to_alipay_dict()
            else:
                params['access_params'] = self.access_params
        if self.allow_huazhi_degrade:
            if hasattr(self.allow_huazhi_degrade, 'to_alipay_dict'):
                params['allow_huazhi_degrade'] = self.allow_huazhi_degrade.to_alipay_dict()
            else:
                params['allow_huazhi_degrade'] = self.allow_huazhi_degrade
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
        if self.period_rule_params:
            if hasattr(self.period_rule_params, 'to_alipay_dict'):
                params['period_rule_params'] = self.period_rule_params.to_alipay_dict()
            else:
                params['period_rule_params'] = self.period_rule_params
        if self.personal_product_code:
            if hasattr(self.personal_product_code, 'to_alipay_dict'):
                params['personal_product_code'] = self.personal_product_code.to_alipay_dict()
            else:
                params['personal_product_code'] = self.personal_product_code
        if self.sign_notify_url:
            if hasattr(self.sign_notify_url, 'to_alipay_dict'):
                params['sign_notify_url'] = self.sign_notify_url.to_alipay_dict()
            else:
                params['sign_notify_url'] = self.sign_notify_url
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignParams()
        if 'access_params' in d:
            o.access_params = d['access_params']
        if 'allow_huazhi_degrade' in d:
            o.allow_huazhi_degrade = d['allow_huazhi_degrade']
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'external_logon_id' in d:
            o.external_logon_id = d['external_logon_id']
        if 'period_rule_params' in d:
            o.period_rule_params = d['period_rule_params']
        if 'personal_product_code' in d:
            o.personal_product_code = d['personal_product_code']
        if 'sign_notify_url' in d:
            o.sign_notify_url = d['sign_notify_url']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        return o


