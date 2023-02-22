#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccessCheckInfo import AccessCheckInfo
from alipay.aop.api.domain.BrandCertInfo import BrandCertInfo
from alipay.aop.api.domain.SearchBoxAppInfo import SearchBoxAppInfo


class AlipayOpenSearchboxUpgradePreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchboxUpgradePreconsultResponse, self).__init__()
        self._access_check_info = None
        self._applicable_box_type = None
        self._brand_cert_info = None
        self._opt_principal_id = None
        self._tiny_app_info = None

    @property
    def access_check_info(self):
        return self._access_check_info

    @access_check_info.setter
    def access_check_info(self, value):
        if isinstance(value, AccessCheckInfo):
            self._access_check_info = value
        else:
            self._access_check_info = AccessCheckInfo.from_alipay_dict(value)
    @property
    def applicable_box_type(self):
        return self._applicable_box_type

    @applicable_box_type.setter
    def applicable_box_type(self, value):
        self._applicable_box_type = value
    @property
    def brand_cert_info(self):
        return self._brand_cert_info

    @brand_cert_info.setter
    def brand_cert_info(self, value):
        if isinstance(value, BrandCertInfo):
            self._brand_cert_info = value
        else:
            self._brand_cert_info = BrandCertInfo.from_alipay_dict(value)
    @property
    def opt_principal_id(self):
        return self._opt_principal_id

    @opt_principal_id.setter
    def opt_principal_id(self, value):
        self._opt_principal_id = value
    @property
    def tiny_app_info(self):
        return self._tiny_app_info

    @tiny_app_info.setter
    def tiny_app_info(self, value):
        if isinstance(value, SearchBoxAppInfo):
            self._tiny_app_info = value
        else:
            self._tiny_app_info = SearchBoxAppInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchboxUpgradePreconsultResponse, self).parse_response_content(response_content)
        if 'access_check_info' in response:
            self.access_check_info = response['access_check_info']
        if 'applicable_box_type' in response:
            self.applicable_box_type = response['applicable_box_type']
        if 'brand_cert_info' in response:
            self.brand_cert_info = response['brand_cert_info']
        if 'opt_principal_id' in response:
            self.opt_principal_id = response['opt_principal_id']
        if 'tiny_app_info' in response:
            self.tiny_app_info = response['tiny_app_info']
