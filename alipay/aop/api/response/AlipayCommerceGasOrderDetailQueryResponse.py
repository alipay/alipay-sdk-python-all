#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FuelVoucherInfo import FuelVoucherInfo


class AlipayCommerceGasOrderDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceGasOrderDetailQueryResponse, self).__init__()
        self._alipay_voucher = None
        self._discount_amount = None
        self._gas_type = None
        self._merchant_order_id = None
        self._nozzle_number = None
        self._order_amount = None
        self._pay_amount = None
        self._service_amount = None
        self._station_code = None
        self._status = None
        self._user_unique_id = None

    @property
    def alipay_voucher(self):
        return self._alipay_voucher

    @alipay_voucher.setter
    def alipay_voucher(self, value):
        if isinstance(value, FuelVoucherInfo):
            self._alipay_voucher = value
        else:
            self._alipay_voucher = FuelVoucherInfo.from_alipay_dict(value)
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def gas_type(self):
        return self._gas_type

    @gas_type.setter
    def gas_type(self, value):
        self._gas_type = value
    @property
    def merchant_order_id(self):
        return self._merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value):
        self._merchant_order_id = value
    @property
    def nozzle_number(self):
        return self._nozzle_number

    @nozzle_number.setter
    def nozzle_number(self, value):
        self._nozzle_number = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def station_code(self):
        return self._station_code

    @station_code.setter
    def station_code(self, value):
        self._station_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_unique_id(self):
        return self._user_unique_id

    @user_unique_id.setter
    def user_unique_id(self, value):
        self._user_unique_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceGasOrderDetailQueryResponse, self).parse_response_content(response_content)
        if 'alipay_voucher' in response:
            self.alipay_voucher = response['alipay_voucher']
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
        if 'gas_type' in response:
            self.gas_type = response['gas_type']
        if 'merchant_order_id' in response:
            self.merchant_order_id = response['merchant_order_id']
        if 'nozzle_number' in response:
            self.nozzle_number = response['nozzle_number']
        if 'order_amount' in response:
            self.order_amount = response['order_amount']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'service_amount' in response:
            self.service_amount = response['service_amount']
        if 'station_code' in response:
            self.station_code = response['station_code']
        if 'status' in response:
            self.status = response['status']
        if 'user_unique_id' in response:
            self.user_unique_id = response['user_unique_id']
