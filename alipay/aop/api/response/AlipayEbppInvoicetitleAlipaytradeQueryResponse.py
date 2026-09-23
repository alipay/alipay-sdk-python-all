#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoicetitleAlipaytradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoicetitleAlipaytradeQueryResponse, self).__init__()
        self._open_bank_account = None
        self._open_bank_name = None
        self._tax_register_no = None
        self._tele_phone_no = None
        self._title_name = None
        self._title_type = None
        self._user_address = None
        self._user_email = None
        self._user_mobile = None

    @property
    def open_bank_account(self):
        return self._open_bank_account

    @open_bank_account.setter
    def open_bank_account(self, value):
        self._open_bank_account = value
    @property
    def open_bank_name(self):
        return self._open_bank_name

    @open_bank_name.setter
    def open_bank_name(self, value):
        self._open_bank_name = value
    @property
    def tax_register_no(self):
        return self._tax_register_no

    @tax_register_no.setter
    def tax_register_no(self, value):
        self._tax_register_no = value
    @property
    def tele_phone_no(self):
        return self._tele_phone_no

    @tele_phone_no.setter
    def tele_phone_no(self, value):
        self._tele_phone_no = value
    @property
    def title_name(self):
        return self._title_name

    @title_name.setter
    def title_name(self, value):
        self._title_name = value
    @property
    def title_type(self):
        return self._title_type

    @title_type.setter
    def title_type(self, value):
        self._title_type = value
    @property
    def user_address(self):
        return self._user_address

    @user_address.setter
    def user_address(self, value):
        self._user_address = value
    @property
    def user_email(self):
        return self._user_email

    @user_email.setter
    def user_email(self, value):
        self._user_email = value
    @property
    def user_mobile(self):
        return self._user_mobile

    @user_mobile.setter
    def user_mobile(self, value):
        self._user_mobile = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoicetitleAlipaytradeQueryResponse, self).parse_response_content(response_content)
        if 'open_bank_account' in response:
            self.open_bank_account = response['open_bank_account']
        if 'open_bank_name' in response:
            self.open_bank_name = response['open_bank_name']
        if 'tax_register_no' in response:
            self.tax_register_no = response['tax_register_no']
        if 'tele_phone_no' in response:
            self.tele_phone_no = response['tele_phone_no']
        if 'title_name' in response:
            self.title_name = response['title_name']
        if 'title_type' in response:
            self.title_type = response['title_type']
        if 'user_address' in response:
            self.user_address = response['user_address']
        if 'user_email' in response:
            self.user_email = response['user_email']
        if 'user_mobile' in response:
            self.user_mobile = response['user_mobile']
