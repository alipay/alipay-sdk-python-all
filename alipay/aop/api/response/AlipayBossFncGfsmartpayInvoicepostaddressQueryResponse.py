#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncGfsmartpayInvoicepostaddressQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncGfsmartpayInvoicepostaddressQueryResponse, self).__init__()
        self._address_name = None
        self._address_phone = None
        self._contact_email = None
        self._mainland_invoice_post_email = None
        self._oversea_invoice_post_email = None
        self._post_address = None

    @property
    def address_name(self):
        return self._address_name

    @address_name.setter
    def address_name(self, value):
        self._address_name = value
    @property
    def address_phone(self):
        return self._address_phone

    @address_phone.setter
    def address_phone(self, value):
        self._address_phone = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def mainland_invoice_post_email(self):
        return self._mainland_invoice_post_email

    @mainland_invoice_post_email.setter
    def mainland_invoice_post_email(self, value):
        self._mainland_invoice_post_email = value
    @property
    def oversea_invoice_post_email(self):
        return self._oversea_invoice_post_email

    @oversea_invoice_post_email.setter
    def oversea_invoice_post_email(self, value):
        self._oversea_invoice_post_email = value
    @property
    def post_address(self):
        return self._post_address

    @post_address.setter
    def post_address(self, value):
        self._post_address = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncGfsmartpayInvoicepostaddressQueryResponse, self).parse_response_content(response_content)
        if 'address_name' in response:
            self.address_name = response['address_name']
        if 'address_phone' in response:
            self.address_phone = response['address_phone']
        if 'contact_email' in response:
            self.contact_email = response['contact_email']
        if 'mainland_invoice_post_email' in response:
            self.mainland_invoice_post_email = response['mainland_invoice_post_email']
        if 'oversea_invoice_post_email' in response:
            self.oversea_invoice_post_email = response['oversea_invoice_post_email']
        if 'post_address' in response:
            self.post_address = response['post_address']
