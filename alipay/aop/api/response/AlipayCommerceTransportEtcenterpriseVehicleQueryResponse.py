#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcenterpriseVehicleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseVehicleQueryResponse, self).__init__()
        self._biz_agreement_no = None
        self._biz_code = None
        self._biz_msg = None
        self._deduct_sign_status = None
        self._device_biz_time = None
        self._device_no = None
        self._device_status = None
        self._device_status_detail = None
        self._first_actived_time = None
        self._order_id = None
        self._order_status = None
        self._service_exp = None
        self._vehicle_corp_id = None
        self._vehicle_corp_name = None
        self._vehicle_id = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value
    @property
    def deduct_sign_status(self):
        return self._deduct_sign_status

    @deduct_sign_status.setter
    def deduct_sign_status(self, value):
        self._deduct_sign_status = value
    @property
    def device_biz_time(self):
        return self._device_biz_time

    @device_biz_time.setter
    def device_biz_time(self, value):
        self._device_biz_time = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, value):
        self._device_status = value
    @property
    def device_status_detail(self):
        return self._device_status_detail

    @device_status_detail.setter
    def device_status_detail(self, value):
        self._device_status_detail = value
    @property
    def first_actived_time(self):
        return self._first_actived_time

    @first_actived_time.setter
    def first_actived_time(self, value):
        self._first_actived_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def service_exp(self):
        return self._service_exp

    @service_exp.setter
    def service_exp(self, value):
        self._service_exp = value
    @property
    def vehicle_corp_id(self):
        return self._vehicle_corp_id

    @vehicle_corp_id.setter
    def vehicle_corp_id(self, value):
        self._vehicle_corp_id = value
    @property
    def vehicle_corp_name(self):
        return self._vehicle_corp_name

    @vehicle_corp_name.setter
    def vehicle_corp_name(self, value):
        self._vehicle_corp_name = value
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseVehicleQueryResponse, self).parse_response_content(response_content)
        if 'biz_agreement_no' in response:
            self.biz_agreement_no = response['biz_agreement_no']
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'deduct_sign_status' in response:
            self.deduct_sign_status = response['deduct_sign_status']
        if 'device_biz_time' in response:
            self.device_biz_time = response['device_biz_time']
        if 'device_no' in response:
            self.device_no = response['device_no']
        if 'device_status' in response:
            self.device_status = response['device_status']
        if 'device_status_detail' in response:
            self.device_status_detail = response['device_status_detail']
        if 'first_actived_time' in response:
            self.first_actived_time = response['first_actived_time']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'service_exp' in response:
            self.service_exp = response['service_exp']
        if 'vehicle_corp_id' in response:
            self.vehicle_corp_id = response['vehicle_corp_id']
        if 'vehicle_corp_name' in response:
            self.vehicle_corp_name = response['vehicle_corp_name']
        if 'vehicle_id' in response:
            self.vehicle_id = response['vehicle_id']
