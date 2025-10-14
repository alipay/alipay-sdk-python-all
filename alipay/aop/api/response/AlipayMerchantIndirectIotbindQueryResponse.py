#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectIotbindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectIotbindQueryResponse, self).__init__()
        self._bind_status = None
        self._bind_time = None
        self._device_id = None
        self._encode_url = None
        self._merchant_name = None
        self._msg_id = None
        self._screen_pay_qr_link = None
        self._smid = None
        self._speech_content = None
        self._supplier_id = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def bind_time(self):
        return self._bind_time

    @bind_time.setter
    def bind_time(self, value):
        self._bind_time = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def encode_url(self):
        return self._encode_url

    @encode_url.setter
    def encode_url(self, value):
        self._encode_url = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def screen_pay_qr_link(self):
        return self._screen_pay_qr_link

    @screen_pay_qr_link.setter
    def screen_pay_qr_link(self, value):
        self._screen_pay_qr_link = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def speech_content(self):
        return self._speech_content

    @speech_content.setter
    def speech_content(self, value):
        self._speech_content = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectIotbindQueryResponse, self).parse_response_content(response_content)
        if 'bind_status' in response:
            self.bind_status = response['bind_status']
        if 'bind_time' in response:
            self.bind_time = response['bind_time']
        if 'device_id' in response:
            self.device_id = response['device_id']
        if 'encode_url' in response:
            self.encode_url = response['encode_url']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'msg_id' in response:
            self.msg_id = response['msg_id']
        if 'screen_pay_qr_link' in response:
            self.screen_pay_qr_link = response['screen_pay_qr_link']
        if 'smid' in response:
            self.smid = response['smid']
        if 'speech_content' in response:
            self.speech_content = response['speech_content']
        if 'supplier_id' in response:
            self.supplier_id = response['supplier_id']
