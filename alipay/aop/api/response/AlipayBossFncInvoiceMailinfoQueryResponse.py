#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncInvoiceMailinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncInvoiceMailinfoQueryResponse, self).__init__()
        self._creator = None
        self._express_company_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._invoice_id = None
        self._last_modifier = None
        self._mail_date = None
        self._mail_id = None
        self._reason = None
        self._recipients_address = None
        self._recipients_name = None
        self._recipients_tel = None
        self._sender_address = None
        self._sender_name = None
        self._sender_tel = None
        self._tnt_inst_id = None
        self._tracking_no = None

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def express_company_name(self):
        return self._express_company_name

    @express_company_name.setter
    def express_company_name(self, value):
        self._express_company_name = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def last_modifier(self):
        return self._last_modifier

    @last_modifier.setter
    def last_modifier(self, value):
        self._last_modifier = value
    @property
    def mail_date(self):
        return self._mail_date

    @mail_date.setter
    def mail_date(self, value):
        self._mail_date = value
    @property
    def mail_id(self):
        return self._mail_id

    @mail_id.setter
    def mail_id(self, value):
        self._mail_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def recipients_address(self):
        return self._recipients_address

    @recipients_address.setter
    def recipients_address(self, value):
        self._recipients_address = value
    @property
    def recipients_name(self):
        return self._recipients_name

    @recipients_name.setter
    def recipients_name(self, value):
        self._recipients_name = value
    @property
    def recipients_tel(self):
        return self._recipients_tel

    @recipients_tel.setter
    def recipients_tel(self, value):
        self._recipients_tel = value
    @property
    def sender_address(self):
        return self._sender_address

    @sender_address.setter
    def sender_address(self, value):
        self._sender_address = value
    @property
    def sender_name(self):
        return self._sender_name

    @sender_name.setter
    def sender_name(self, value):
        self._sender_name = value
    @property
    def sender_tel(self):
        return self._sender_tel

    @sender_tel.setter
    def sender_tel(self, value):
        self._sender_tel = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncInvoiceMailinfoQueryResponse, self).parse_response_content(response_content)
        if 'creator' in response:
            self.creator = response['creator']
        if 'express_company_name' in response:
            self.express_company_name = response['express_company_name']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'invoice_id' in response:
            self.invoice_id = response['invoice_id']
        if 'last_modifier' in response:
            self.last_modifier = response['last_modifier']
        if 'mail_date' in response:
            self.mail_date = response['mail_date']
        if 'mail_id' in response:
            self.mail_id = response['mail_id']
        if 'reason' in response:
            self.reason = response['reason']
        if 'recipients_address' in response:
            self.recipients_address = response['recipients_address']
        if 'recipients_name' in response:
            self.recipients_name = response['recipients_name']
        if 'recipients_tel' in response:
            self.recipients_tel = response['recipients_tel']
        if 'sender_address' in response:
            self.sender_address = response['sender_address']
        if 'sender_name' in response:
            self.sender_name = response['sender_name']
        if 'sender_tel' in response:
            self.sender_tel = response['sender_tel']
        if 'tnt_inst_id' in response:
            self.tnt_inst_id = response['tnt_inst_id']
        if 'tracking_no' in response:
            self.tracking_no = response['tracking_no']
