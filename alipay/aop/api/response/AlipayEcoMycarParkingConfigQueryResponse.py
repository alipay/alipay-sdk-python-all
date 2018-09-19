#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InterfaceInfoList import InterfaceInfoList


class AlipayEcoMycarParkingConfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingConfigQueryResponse, self).__init__()
        self._account_no = None
        self._interface_info_list = None
        self._merchant_logo = None
        self._merchant_name = None
        self._merchant_service_phone = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def interface_info_list(self):
        return self._interface_info_list

    @interface_info_list.setter
    def interface_info_list(self, value):
        if isinstance(value, InterfaceInfoList):
            self._interface_info_list = value
        else:
            self._interface_info_list = InterfaceInfoList.from_alipay_dict(value)
    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_service_phone(self):
        return self._merchant_service_phone

    @merchant_service_phone.setter
    def merchant_service_phone(self, value):
        self._merchant_service_phone = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingConfigQueryResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'interface_info_list' in response:
            self.interface_info_list = response['interface_info_list']
        if 'merchant_logo' in response:
            self.merchant_logo = response['merchant_logo']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'merchant_service_phone' in response:
            self.merchant_service_phone = response['merchant_service_phone']
