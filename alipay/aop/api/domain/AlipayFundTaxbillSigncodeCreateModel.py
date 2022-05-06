#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTaxbillSigncodeCreateModel(object):

    def __init__(self):
        self._back_url = None
        self._biz_scene = None
        self._contractor_code = None
        self._employee_alipay_logon_id = None
        self._employee_id_card_no = None
        self._employee_name = None
        self._employer_code = None
        self._identification_in_belonging_employer = None
        self._identity = None
        self._identity_type = None
        self._product_code = None
        self._sign_code_type = None
        self._tax_optimization_mode = None

    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def contractor_code(self):
        return self._contractor_code

    @contractor_code.setter
    def contractor_code(self, value):
        self._contractor_code = value
    @property
    def employee_alipay_logon_id(self):
        return self._employee_alipay_logon_id

    @employee_alipay_logon_id.setter
    def employee_alipay_logon_id(self, value):
        self._employee_alipay_logon_id = value
    @property
    def employee_id_card_no(self):
        return self._employee_id_card_no

    @employee_id_card_no.setter
    def employee_id_card_no(self, value):
        self._employee_id_card_no = value
    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self, value):
        self._employee_name = value
    @property
    def employer_code(self):
        return self._employer_code

    @employer_code.setter
    def employer_code(self, value):
        self._employer_code = value
    @property
    def identification_in_belonging_employer(self):
        return self._identification_in_belonging_employer

    @identification_in_belonging_employer.setter
    def identification_in_belonging_employer(self, value):
        self._identification_in_belonging_employer = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sign_code_type(self):
        return self._sign_code_type

    @sign_code_type.setter
    def sign_code_type(self, value):
        self._sign_code_type = value
    @property
    def tax_optimization_mode(self):
        return self._tax_optimization_mode

    @tax_optimization_mode.setter
    def tax_optimization_mode(self, value):
        self._tax_optimization_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.contractor_code:
            if hasattr(self.contractor_code, 'to_alipay_dict'):
                params['contractor_code'] = self.contractor_code.to_alipay_dict()
            else:
                params['contractor_code'] = self.contractor_code
        if self.employee_alipay_logon_id:
            if hasattr(self.employee_alipay_logon_id, 'to_alipay_dict'):
                params['employee_alipay_logon_id'] = self.employee_alipay_logon_id.to_alipay_dict()
            else:
                params['employee_alipay_logon_id'] = self.employee_alipay_logon_id
        if self.employee_id_card_no:
            if hasattr(self.employee_id_card_no, 'to_alipay_dict'):
                params['employee_id_card_no'] = self.employee_id_card_no.to_alipay_dict()
            else:
                params['employee_id_card_no'] = self.employee_id_card_no
        if self.employee_name:
            if hasattr(self.employee_name, 'to_alipay_dict'):
                params['employee_name'] = self.employee_name.to_alipay_dict()
            else:
                params['employee_name'] = self.employee_name
        if self.employer_code:
            if hasattr(self.employer_code, 'to_alipay_dict'):
                params['employer_code'] = self.employer_code.to_alipay_dict()
            else:
                params['employer_code'] = self.employer_code
        if self.identification_in_belonging_employer:
            if hasattr(self.identification_in_belonging_employer, 'to_alipay_dict'):
                params['identification_in_belonging_employer'] = self.identification_in_belonging_employer.to_alipay_dict()
            else:
                params['identification_in_belonging_employer'] = self.identification_in_belonging_employer
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sign_code_type:
            if hasattr(self.sign_code_type, 'to_alipay_dict'):
                params['sign_code_type'] = self.sign_code_type.to_alipay_dict()
            else:
                params['sign_code_type'] = self.sign_code_type
        if self.tax_optimization_mode:
            if hasattr(self.tax_optimization_mode, 'to_alipay_dict'):
                params['tax_optimization_mode'] = self.tax_optimization_mode.to_alipay_dict()
            else:
                params['tax_optimization_mode'] = self.tax_optimization_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTaxbillSigncodeCreateModel()
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'contractor_code' in d:
            o.contractor_code = d['contractor_code']
        if 'employee_alipay_logon_id' in d:
            o.employee_alipay_logon_id = d['employee_alipay_logon_id']
        if 'employee_id_card_no' in d:
            o.employee_id_card_no = d['employee_id_card_no']
        if 'employee_name' in d:
            o.employee_name = d['employee_name']
        if 'employer_code' in d:
            o.employer_code = d['employer_code']
        if 'identification_in_belonging_employer' in d:
            o.identification_in_belonging_employer = d['identification_in_belonging_employer']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sign_code_type' in d:
            o.sign_code_type = d['sign_code_type']
        if 'tax_optimization_mode' in d:
            o.tax_optimization_mode = d['tax_optimization_mode']
        return o


