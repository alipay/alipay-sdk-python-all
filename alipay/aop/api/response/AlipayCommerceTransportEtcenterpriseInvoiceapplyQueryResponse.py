#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EtcCorpInvoiceList import EtcCorpInvoiceList


class AlipayCommerceTransportEtcenterpriseInvoiceapplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseInvoiceapplyQueryResponse, self).__init__()
        self._apply_id = None
        self._change_apply_id = None
        self._fee = None
        self._invoice_list = None
        self._invoice_num = None
        self._waybill_invoice_status = None
        self._waybill_no = None
        self._waybill_oss_url = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def change_apply_id(self):
        return self._change_apply_id

    @change_apply_id.setter
    def change_apply_id(self, value):
        self._change_apply_id = value
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def invoice_list(self):
        return self._invoice_list

    @invoice_list.setter
    def invoice_list(self, value):
        if isinstance(value, EtcCorpInvoiceList):
            self._invoice_list = value
        else:
            self._invoice_list = EtcCorpInvoiceList.from_alipay_dict(value)
    @property
    def invoice_num(self):
        return self._invoice_num

    @invoice_num.setter
    def invoice_num(self, value):
        self._invoice_num = value
    @property
    def waybill_invoice_status(self):
        return self._waybill_invoice_status

    @waybill_invoice_status.setter
    def waybill_invoice_status(self, value):
        self._waybill_invoice_status = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value
    @property
    def waybill_oss_url(self):
        return self._waybill_oss_url

    @waybill_oss_url.setter
    def waybill_oss_url(self, value):
        self._waybill_oss_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseInvoiceapplyQueryResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'change_apply_id' in response:
            self.change_apply_id = response['change_apply_id']
        if 'fee' in response:
            self.fee = response['fee']
        if 'invoice_list' in response:
            self.invoice_list = response['invoice_list']
        if 'invoice_num' in response:
            self.invoice_num = response['invoice_num']
        if 'waybill_invoice_status' in response:
            self.waybill_invoice_status = response['waybill_invoice_status']
        if 'waybill_no' in response:
            self.waybill_no = response['waybill_no']
        if 'waybill_oss_url' in response:
            self.waybill_oss_url = response['waybill_oss_url']
