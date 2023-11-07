#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcDepartmentUpgradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcDepartmentUpgradeQueryResponse, self).__init__()
        self._department_id = None
        self._enterprise_id = None
        self._process_id = None
        self._sign_url = None
        self._status = None
        self._sub_account_id = None
        self._sub_enterprise_id = None
        self._sub_enterprise_name = None

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_account_id(self):
        return self._sub_account_id

    @sub_account_id.setter
    def sub_account_id(self, value):
        self._sub_account_id = value
    @property
    def sub_enterprise_id(self):
        return self._sub_enterprise_id

    @sub_enterprise_id.setter
    def sub_enterprise_id(self, value):
        self._sub_enterprise_id = value
    @property
    def sub_enterprise_name(self):
        return self._sub_enterprise_name

    @sub_enterprise_name.setter
    def sub_enterprise_name(self, value):
        self._sub_enterprise_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcDepartmentUpgradeQueryResponse, self).parse_response_content(response_content)
        if 'department_id' in response:
            self.department_id = response['department_id']
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'process_id' in response:
            self.process_id = response['process_id']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
        if 'status' in response:
            self.status = response['status']
        if 'sub_account_id' in response:
            self.sub_account_id = response['sub_account_id']
        if 'sub_enterprise_id' in response:
            self.sub_enterprise_id = response['sub_enterprise_id']
        if 'sub_enterprise_name' in response:
            self.sub_enterprise_name = response['sub_enterprise_name']
