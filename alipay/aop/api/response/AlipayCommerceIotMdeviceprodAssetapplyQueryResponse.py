#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMdeviceprodAssetapplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMdeviceprodAssetapplyQueryResponse, self).__init__()
        self._apply_isv_name = None
        self._apply_isv_pid = None
        self._apply_merchant_mobile = None
        self._apply_merchant_name = None
        self._apply_merchant_pid = None
        self._apply_person_mobile = None
        self._apply_person_name = None

    @property
    def apply_isv_name(self):
        return self._apply_isv_name

    @apply_isv_name.setter
    def apply_isv_name(self, value):
        self._apply_isv_name = value
    @property
    def apply_isv_pid(self):
        return self._apply_isv_pid

    @apply_isv_pid.setter
    def apply_isv_pid(self, value):
        self._apply_isv_pid = value
    @property
    def apply_merchant_mobile(self):
        return self._apply_merchant_mobile

    @apply_merchant_mobile.setter
    def apply_merchant_mobile(self, value):
        self._apply_merchant_mobile = value
    @property
    def apply_merchant_name(self):
        return self._apply_merchant_name

    @apply_merchant_name.setter
    def apply_merchant_name(self, value):
        self._apply_merchant_name = value
    @property
    def apply_merchant_pid(self):
        return self._apply_merchant_pid

    @apply_merchant_pid.setter
    def apply_merchant_pid(self, value):
        self._apply_merchant_pid = value
    @property
    def apply_person_mobile(self):
        return self._apply_person_mobile

    @apply_person_mobile.setter
    def apply_person_mobile(self, value):
        self._apply_person_mobile = value
    @property
    def apply_person_name(self):
        return self._apply_person_name

    @apply_person_name.setter
    def apply_person_name(self, value):
        self._apply_person_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMdeviceprodAssetapplyQueryResponse, self).parse_response_content(response_content)
        if 'apply_isv_name' in response:
            self.apply_isv_name = response['apply_isv_name']
        if 'apply_isv_pid' in response:
            self.apply_isv_pid = response['apply_isv_pid']
        if 'apply_merchant_mobile' in response:
            self.apply_merchant_mobile = response['apply_merchant_mobile']
        if 'apply_merchant_name' in response:
            self.apply_merchant_name = response['apply_merchant_name']
        if 'apply_merchant_pid' in response:
            self.apply_merchant_pid = response['apply_merchant_pid']
        if 'apply_person_mobile' in response:
            self.apply_person_mobile = response['apply_person_mobile']
        if 'apply_person_name' in response:
            self.apply_person_name = response['apply_person_name']
