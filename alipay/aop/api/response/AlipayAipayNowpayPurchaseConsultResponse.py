#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConsultChargingOption import ConsultChargingOption


class AlipayAipayNowpayPurchaseConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayNowpayPurchaseConsultResponse, self).__init__()
        self._capability_status = None
        self._charging_options = None
        self._decision = None
        self._product_icon_url = None
        self._product_name = None
        self._purchase_qr_code = None
        self._purchase_url = None
        self._reason_code = None
        self._valid_from = None
        self._valid_until = None

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
                if isinstance(i, ConsultChargingOption):
                    self._charging_options.append(i)
                else:
                    self._charging_options.append(ConsultChargingOption.from_alipay_dict(i))
    @property
    def decision(self):
        return self._decision

    @decision.setter
    def decision(self, value):
        self._decision = value
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
    def purchase_qr_code(self):
        return self._purchase_qr_code

    @purchase_qr_code.setter
    def purchase_qr_code(self, value):
        self._purchase_qr_code = value
    @property
    def purchase_url(self):
        return self._purchase_url

    @purchase_url.setter
    def purchase_url(self, value):
        self._purchase_url = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def valid_from(self):
        return self._valid_from

    @valid_from.setter
    def valid_from(self, value):
        self._valid_from = value
    @property
    def valid_until(self):
        return self._valid_until

    @valid_until.setter
    def valid_until(self, value):
        self._valid_until = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayNowpayPurchaseConsultResponse, self).parse_response_content(response_content)
        if 'capability_status' in response:
            self.capability_status = response['capability_status']
        if 'charging_options' in response:
            self.charging_options = response['charging_options']
        if 'decision' in response:
            self.decision = response['decision']
        if 'product_icon_url' in response:
            self.product_icon_url = response['product_icon_url']
        if 'product_name' in response:
            self.product_name = response['product_name']
        if 'purchase_qr_code' in response:
            self.purchase_qr_code = response['purchase_qr_code']
        if 'purchase_url' in response:
            self.purchase_url = response['purchase_url']
        if 'reason_code' in response:
            self.reason_code = response['reason_code']
        if 'valid_from' in response:
            self.valid_from = response['valid_from']
        if 'valid_until' in response:
            self.valid_until = response['valid_until']
