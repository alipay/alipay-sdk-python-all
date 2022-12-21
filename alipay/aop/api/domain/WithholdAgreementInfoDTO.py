#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WithholdAgreementInfoDTO(object):

    def __init__(self):
        self._agreement_no = None
        self._alipay_logon_id = None
        self._external_agreement_no = None
        self._invalid_time = None
        self._personal_product_code = None
        self._sign_scene = None
        self._sign_time = None
        self._unsign_time = None
        self._valid_time = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def external_agreement_no(self):
        return self._external_agreement_no

    @external_agreement_no.setter
    def external_agreement_no(self, value):
        self._external_agreement_no = value
    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
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
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def unsign_time(self):
        return self._unsign_time

    @unsign_time.setter
    def unsign_time(self, value):
        self._unsign_time = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
        if self.external_agreement_no:
            if hasattr(self.external_agreement_no, 'to_alipay_dict'):
                params['external_agreement_no'] = self.external_agreement_no.to_alipay_dict()
            else:
                params['external_agreement_no'] = self.external_agreement_no
        if self.invalid_time:
            if hasattr(self.invalid_time, 'to_alipay_dict'):
                params['invalid_time'] = self.invalid_time.to_alipay_dict()
            else:
                params['invalid_time'] = self.invalid_time
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
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.unsign_time:
            if hasattr(self.unsign_time, 'to_alipay_dict'):
                params['unsign_time'] = self.unsign_time.to_alipay_dict()
            else:
                params['unsign_time'] = self.unsign_time
        if self.valid_time:
            if hasattr(self.valid_time, 'to_alipay_dict'):
                params['valid_time'] = self.valid_time.to_alipay_dict()
            else:
                params['valid_time'] = self.valid_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WithholdAgreementInfoDTO()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'invalid_time' in d:
            o.invalid_time = d['invalid_time']
        if 'personal_product_code' in d:
            o.personal_product_code = d['personal_product_code']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'unsign_time' in d:
            o.unsign_time = d['unsign_time']
        if 'valid_time' in d:
            o.valid_time = d['valid_time']
        return o


