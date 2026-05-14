#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecyclingFarmerItemResult import RecyclingFarmerItemResult


class AlipayCommerceEcRecyclinginvoiceFarmerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceFarmerQueryResponse, self).__init__()
        self._account_no = None
        self._account_type = None
        self._cert_no = None
        self._confirm_status = None
        self._farmer_auth_url = None
        self._farmer_id = None
        self._farmer_item_list = None
        self._farmer_name = None
        self._farmer_type_list = None
        self._is_family_master = None
        self._proxy_cert_no = None
        self._proxy_name = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def confirm_status(self):
        return self._confirm_status

    @confirm_status.setter
    def confirm_status(self, value):
        self._confirm_status = value
    @property
    def farmer_auth_url(self):
        return self._farmer_auth_url

    @farmer_auth_url.setter
    def farmer_auth_url(self, value):
        self._farmer_auth_url = value
    @property
    def farmer_id(self):
        return self._farmer_id

    @farmer_id.setter
    def farmer_id(self, value):
        self._farmer_id = value
    @property
    def farmer_item_list(self):
        return self._farmer_item_list

    @farmer_item_list.setter
    def farmer_item_list(self, value):
        if isinstance(value, list):
            self._farmer_item_list = list()
            for i in value:
                if isinstance(i, RecyclingFarmerItemResult):
                    self._farmer_item_list.append(i)
                else:
                    self._farmer_item_list.append(RecyclingFarmerItemResult.from_alipay_dict(i))
    @property
    def farmer_name(self):
        return self._farmer_name

    @farmer_name.setter
    def farmer_name(self, value):
        self._farmer_name = value
    @property
    def farmer_type_list(self):
        return self._farmer_type_list

    @farmer_type_list.setter
    def farmer_type_list(self, value):
        if isinstance(value, list):
            self._farmer_type_list = list()
            for i in value:
                self._farmer_type_list.append(i)
    @property
    def is_family_master(self):
        return self._is_family_master

    @is_family_master.setter
    def is_family_master(self, value):
        self._is_family_master = value
    @property
    def proxy_cert_no(self):
        return self._proxy_cert_no

    @proxy_cert_no.setter
    def proxy_cert_no(self, value):
        self._proxy_cert_no = value
    @property
    def proxy_name(self):
        return self._proxy_name

    @proxy_name.setter
    def proxy_name(self, value):
        self._proxy_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceFarmerQueryResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'account_type' in response:
            self.account_type = response['account_type']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'confirm_status' in response:
            self.confirm_status = response['confirm_status']
        if 'farmer_auth_url' in response:
            self.farmer_auth_url = response['farmer_auth_url']
        if 'farmer_id' in response:
            self.farmer_id = response['farmer_id']
        if 'farmer_item_list' in response:
            self.farmer_item_list = response['farmer_item_list']
        if 'farmer_name' in response:
            self.farmer_name = response['farmer_name']
        if 'farmer_type_list' in response:
            self.farmer_type_list = response['farmer_type_list']
        if 'is_family_master' in response:
            self.is_family_master = response['is_family_master']
        if 'proxy_cert_no' in response:
            self.proxy_cert_no = response['proxy_cert_no']
        if 'proxy_name' in response:
            self.proxy_name = response['proxy_name']
