#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceWithholdrepayorderAgreementQueryModel(object):

    def __init__(self):
        self._agreement_no = None
        self._alipay_open_id = None
        self._alipay_user_id = None
        self._external_agreement_no = None
        self._personal_product_code = None
        self._sign_scene = None
        self._third_party_type = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def external_agreement_no(self):
        return self._external_agreement_no

    @external_agreement_no.setter
    def external_agreement_no(self, value):
        self._external_agreement_no = value
    @property
    def personal_product_code(self):
        return self._personal_product_code

    @personal_product_code.setter
    def personal_product_code(self, value):
        self._personal_product_code = value
    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value
    @property
    def third_party_type(self):
        return self._third_party_type

    @third_party_type.setter
    def third_party_type(self, value):
        self._third_party_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.external_agreement_no:
            if hasattr(self.external_agreement_no, 'to_alipay_dict'):
                params['external_agreement_no'] = self.external_agreement_no.to_alipay_dict()
            else:
                params['external_agreement_no'] = self.external_agreement_no
        if self.personal_product_code:
            if hasattr(self.personal_product_code, 'to_alipay_dict'):
                params['personal_product_code'] = self.personal_product_code.to_alipay_dict()
            else:
                params['personal_product_code'] = self.personal_product_code
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
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
        o = AlipayCommerceWithholdrepayorderAgreementQueryModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'personal_product_code' in d:
            o.personal_product_code = d['personal_product_code']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        if 'third_party_type' in d:
            o.third_party_type = d['third_party_type']
        return o


