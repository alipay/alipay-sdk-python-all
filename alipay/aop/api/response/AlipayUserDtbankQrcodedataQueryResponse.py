#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDtbankQrcodedataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankQrcodedataQueryResponse, self).__init__()
        self._bind_card = None
        self._data_date = None
        self._lead_to_follow = None
        self._qrcode_id = None
        self._qrcode_out_id = None
        self._send_voucher_amt = None
        self._send_voucher_cnt = None
        self._write_off_voucher_amt = None
        self._write_off_voucher_cnt = None

    @property
    def bind_card(self):
        return self._bind_card

    @bind_card.setter
    def bind_card(self, value):
        self._bind_card = value
    @property
    def data_date(self):
        return self._data_date

    @data_date.setter
    def data_date(self, value):
        self._data_date = value
    @property
    def lead_to_follow(self):
        return self._lead_to_follow

    @lead_to_follow.setter
    def lead_to_follow(self, value):
        self._lead_to_follow = value
    @property
    def qrcode_id(self):
        return self._qrcode_id

    @qrcode_id.setter
    def qrcode_id(self, value):
        self._qrcode_id = value
    @property
    def qrcode_out_id(self):
        return self._qrcode_out_id

    @qrcode_out_id.setter
    def qrcode_out_id(self, value):
        self._qrcode_out_id = value
    @property
    def send_voucher_amt(self):
        return self._send_voucher_amt

    @send_voucher_amt.setter
    def send_voucher_amt(self, value):
        self._send_voucher_amt = value
    @property
    def send_voucher_cnt(self):
        return self._send_voucher_cnt

    @send_voucher_cnt.setter
    def send_voucher_cnt(self, value):
        self._send_voucher_cnt = value
    @property
    def write_off_voucher_amt(self):
        return self._write_off_voucher_amt

    @write_off_voucher_amt.setter
    def write_off_voucher_amt(self, value):
        self._write_off_voucher_amt = value
    @property
    def write_off_voucher_cnt(self):
        return self._write_off_voucher_cnt

    @write_off_voucher_cnt.setter
    def write_off_voucher_cnt(self, value):
        self._write_off_voucher_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankQrcodedataQueryResponse, self).parse_response_content(response_content)
        if 'bind_card' in response:
            self.bind_card = response['bind_card']
        if 'data_date' in response:
            self.data_date = response['data_date']
        if 'lead_to_follow' in response:
            self.lead_to_follow = response['lead_to_follow']
        if 'qrcode_id' in response:
            self.qrcode_id = response['qrcode_id']
        if 'qrcode_out_id' in response:
            self.qrcode_out_id = response['qrcode_out_id']
        if 'send_voucher_amt' in response:
            self.send_voucher_amt = response['send_voucher_amt']
        if 'send_voucher_cnt' in response:
            self.send_voucher_cnt = response['send_voucher_cnt']
        if 'write_off_voucher_amt' in response:
            self.write_off_voucher_amt = response['write_off_voucher_amt']
        if 'write_off_voucher_cnt' in response:
            self.write_off_voucher_cnt = response['write_off_voucher_cnt']
