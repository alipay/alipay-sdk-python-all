#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignMerchantParams import SignMerchantParams


class AgreementSignParams(object):

    def __init__(self):
        self._buckle_app_id = None
        self._buckle_merchant_id = None
        self._external_agreement_no = None
        self._external_logon_id = None
        self._personal_product_code = None
        self._promo_params = None
        self._sign_scene = None
        self._sign_validity_period = None
        self._sub_merchant = None
        self._third_party_type = None

    @property
    def buckle_app_id(self):
        return self._buckle_app_id

    @buckle_app_id.setter
    def buckle_app_id(self, value):
        self._buckle_app_id = value
    @property
    def buckle_merchant_id(self):
        return self._buckle_merchant_id

    @buckle_merchant_id.setter
    def buckle_merchant_id(self, value):
        self._buckle_merchant_id = value
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
    @property
    def promo_params(self):
        return self._promo_params

    @promo_params.setter
    def promo_params(self, value):
        self._promo_params = value
    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value
    @property
    def sign_validity_period(self):
        return self._sign_validity_period

    @sign_validity_period.setter
    def sign_validity_period(self, value):
        self._sign_validity_period = value
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, SignMerchantParams):
            self._sub_merchant = value
        else:
            self._sub_merchant = SignMerchantParams.from_alipay_dict(value)
    @property
    def third_party_type(self):
        return self._third_party_type

    @third_party_type.setter
    def third_party_type(self, value):
        self._third_party_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.buckle_app_id:
            if hasattr(self.buckle_app_id, 'to_alipay_dict'):
                params['buckle_app_id'] = self.buckle_app_id.to_alipay_dict()
            else:
                params['buckle_app_id'] = self.buckle_app_id
        if self.buckle_merchant_id:
            if hasattr(self.buckle_merchant_id, 'to_alipay_dict'):
                params['buckle_merchant_id'] = self.buckle_merchant_id.to_alipay_dict()
            else:
                params['buckle_merchant_id'] = self.buckle_merchant_id
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
        if self.promo_params:
            if hasattr(self.promo_params, 'to_alipay_dict'):
                params['promo_params'] = self.promo_params.to_alipay_dict()
            else:
                params['promo_params'] = self.promo_params
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
        if self.sign_validity_period:
            if hasattr(self.sign_validity_period, 'to_alipay_dict'):
                params['sign_validity_period'] = self.sign_validity_period.to_alipay_dict()
            else:
                params['sign_validity_period'] = self.sign_validity_period
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        if self.third_party_type:
            if hasattr(self.third_party_type, 'to_alipay_dict'):
                params['third_party_type'] = self.third_party_type.to_alipay_dict()
            else:
                params['third_party_type'] = self.third_party_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgreementSignParams()
        if 'buckle_app_id' in d:
            o.buckle_app_id = d['buckle_app_id']
        if 'buckle_merchant_id' in d:
            o.buckle_merchant_id = d['buckle_merchant_id']
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'external_logon_id' in d:
            o.external_logon_id = d['external_logon_id']
        if 'personal_product_code' in d:
            o.personal_product_code = d['personal_product_code']
        if 'promo_params' in d:
            o.promo_params = d['promo_params']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        if 'sign_validity_period' in d:
            o.sign_validity_period = d['sign_validity_period']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'third_party_type' in d:
            o.third_party_type = d['third_party_type']
        return o


