#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChargingOption import ChargingOption


class AlipayAipayNowpayChargeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayNowpayChargeQueryResponse, self).__init__()
        self._billing_mode = None
        self._capability_status = None
        self._charging_options = None
        self._management_url = None
        self._product_icon_url = None
        self._product_name = None
        self._quota_unit = None
        self._reason_message = None
        self._status_version = None

    @property
    def billing_mode(self):
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, value):
        self._billing_mode = value
    @property
    def capability_status(self):
        return self._capability_status

    @capability_status.setter
    def capability_status(self, value):
        self._capability_status = value
    @property
    def charging_options(self):
        return self._charging_options

    @charging_options.setter
    def charging_options(self, value):
        if isinstance(value, list):
            self._charging_options = list()
            for i in value:
                if isinstance(i, ChargingOption):
                    self._charging_options.append(i)
                else:
                    self._charging_options.append(ChargingOption.from_alipay_dict(i))
    @property
    def management_url(self):
        return self._management_url

    @management_url.setter
    def management_url(self, value):
        self._management_url = value
    @property
    def product_icon_url(self):
        return self._product_icon_url

    @product_icon_url.setter
    def product_icon_url(self, value):
        self._product_icon_url = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def quota_unit(self):
        return self._quota_unit

    @quota_unit.setter
    def quota_unit(self, value):
        self._quota_unit = value
    @property
    def reason_message(self):
        return self._reason_message

    @reason_message.setter
    def reason_message(self, value):
        self._reason_message = value
    @property
    def status_version(self):
        return self._status_version

    @status_version.setter
    def status_version(self, value):
        self._status_version = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayNowpayChargeQueryResponse, self).parse_response_content(response_content)
        if 'billing_mode' in response:
            self.billing_mode = response['billing_mode']
        if 'capability_status' in response:
            self.capability_status = response['capability_status']
        if 'charging_options' in response:
            self.charging_options = response['charging_options']
        if 'management_url' in response:
            self.management_url = response['management_url']
        if 'product_icon_url' in response:
            self.product_icon_url = response['product_icon_url']
        if 'product_name' in response:
            self.product_name = response['product_name']
        if 'quota_unit' in response:
            self.quota_unit = response['quota_unit']
        if 'reason_message' in response:
            self.reason_message = response['reason_message']
        if 'status_version' in response:
            self.status_version = response['status_version']
