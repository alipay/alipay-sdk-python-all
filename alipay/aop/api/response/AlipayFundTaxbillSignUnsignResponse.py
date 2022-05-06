#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTaxbillSignUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTaxbillSignUnsignResponse, self).__init__()
        self._accept = None
        self._agreement_id = None
        self._agreement_status = None
        self._biz_scene = None
        self._contractor_code = None
        self._contractor_name = None
        self._employer_code = None
        self._error_code = None
        self._error_msg = None
        self._identification_in_belonging_employer = None
        self._product_code = None
        self._sign_status = None
        self._tax_optimization_mode = None
        self._terminated_time = None
        self._user_status = None

    @property
    def accept(self):
        return self._accept

    @accept.setter
    def accept(self, value):
        self._accept = value
    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
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
    def contractor_name(self):
        return self._contractor_name

    @contractor_name.setter
    def contractor_name(self, value):
        self._contractor_name = value
    @property
    def employer_code(self):
        return self._employer_code

    @employer_code.setter
    def employer_code(self, value):
        self._employer_code = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def identification_in_belonging_employer(self):
        return self._identification_in_belonging_employer

    @identification_in_belonging_employer.setter
    def identification_in_belonging_employer(self, value):
        self._identification_in_belonging_employer = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def tax_optimization_mode(self):
        return self._tax_optimization_mode

    @tax_optimization_mode.setter
    def tax_optimization_mode(self, value):
        self._tax_optimization_mode = value
    @property
    def terminated_time(self):
        return self._terminated_time

    @terminated_time.setter
    def terminated_time(self, value):
        self._terminated_time = value
    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTaxbillSignUnsignResponse, self).parse_response_content(response_content)
        if 'accept' in response:
            self.accept = response['accept']
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'contractor_code' in response:
            self.contractor_code = response['contractor_code']
        if 'contractor_name' in response:
            self.contractor_name = response['contractor_name']
        if 'employer_code' in response:
            self.employer_code = response['employer_code']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'identification_in_belonging_employer' in response:
            self.identification_in_belonging_employer = response['identification_in_belonging_employer']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'sign_status' in response:
            self.sign_status = response['sign_status']
        if 'tax_optimization_mode' in response:
            self.tax_optimization_mode = response['tax_optimization_mode']
        if 'terminated_time' in response:
            self.terminated_time = response['terminated_time']
        if 'user_status' in response:
            self.user_status = response['user_status']
