#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromiseConfigDTO import PromiseConfigDTO
from alipay.aop.api.domain.RiskConfigDTO import RiskConfigDTO


class AlipayMerchantSolcreditserviceprodMerchantreviewQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolcreditserviceprodMerchantreviewQueryResponse, self).__init__()
        self._app_jump_link = None
        self._contact_email = None
        self._contact_number = None
        self._logo_url = None
        self._merchant_app_id = None
        self._merchant_name = None
        self._promise_config = None
        self._risk_config = None
        self._scene_code = None
        self._version_no = None

    @property
    def app_jump_link(self):
        return self._app_jump_link

    @app_jump_link.setter
    def app_jump_link(self, value):
        self._app_jump_link = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def promise_config(self):
        return self._promise_config

    @promise_config.setter
    def promise_config(self, value):
        if isinstance(value, PromiseConfigDTO):
            self._promise_config = value
        else:
            self._promise_config = PromiseConfigDTO.from_alipay_dict(value)
    @property
    def risk_config(self):
        return self._risk_config

    @risk_config.setter
    def risk_config(self, value):
        if isinstance(value, RiskConfigDTO):
            self._risk_config = value
        else:
            self._risk_config = RiskConfigDTO.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolcreditserviceprodMerchantreviewQueryResponse, self).parse_response_content(response_content)
        if 'app_jump_link' in response:
            self.app_jump_link = response['app_jump_link']
        if 'contact_email' in response:
            self.contact_email = response['contact_email']
        if 'contact_number' in response:
            self.contact_number = response['contact_number']
        if 'logo_url' in response:
            self.logo_url = response['logo_url']
        if 'merchant_app_id' in response:
            self.merchant_app_id = response['merchant_app_id']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'promise_config' in response:
            self.promise_config = response['promise_config']
        if 'risk_config' in response:
            self.risk_config = response['risk_config']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
        if 'version_no' in response:
            self.version_no = response['version_no']
