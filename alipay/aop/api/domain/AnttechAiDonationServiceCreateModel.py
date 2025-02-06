#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiDonationServiceCreateModel(object):

    def __init__(self):
        self._biz_receipt = None
        self._bless_content = None
        self._device_id = None
        self._donation_amount = None
        self._donation_date = None
        self._donation_number = None
        self._donation_type = None
        self._donor_name = None
        self._external_client_id = None
        self._request_id = None
        self._terminal_display = None

    @property
    def biz_receipt(self):
        return self._biz_receipt

    @biz_receipt.setter
    def biz_receipt(self, value):
        self._biz_receipt = value
    @property
    def bless_content(self):
        return self._bless_content

    @bless_content.setter
    def bless_content(self, value):
        self._bless_content = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def donation_amount(self):
        return self._donation_amount

    @donation_amount.setter
    def donation_amount(self, value):
        self._donation_amount = value
    @property
    def donation_date(self):
        return self._donation_date

    @donation_date.setter
    def donation_date(self, value):
        self._donation_date = value
    @property
    def donation_number(self):
        return self._donation_number

    @donation_number.setter
    def donation_number(self, value):
        self._donation_number = value
    @property
    def donation_type(self):
        return self._donation_type

    @donation_type.setter
    def donation_type(self, value):
        self._donation_type = value
    @property
    def donor_name(self):
        return self._donor_name

    @donor_name.setter
    def donor_name(self, value):
        self._donor_name = value
    @property
    def external_client_id(self):
        return self._external_client_id

    @external_client_id.setter
    def external_client_id(self, value):
        self._external_client_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def terminal_display(self):
        return self._terminal_display

    @terminal_display.setter
    def terminal_display(self, value):
        self._terminal_display = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_receipt:
            if hasattr(self.biz_receipt, 'to_alipay_dict'):
                params['biz_receipt'] = self.biz_receipt.to_alipay_dict()
            else:
                params['biz_receipt'] = self.biz_receipt
        if self.bless_content:
            if hasattr(self.bless_content, 'to_alipay_dict'):
                params['bless_content'] = self.bless_content.to_alipay_dict()
            else:
                params['bless_content'] = self.bless_content
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.donation_amount:
            if hasattr(self.donation_amount, 'to_alipay_dict'):
                params['donation_amount'] = self.donation_amount.to_alipay_dict()
            else:
                params['donation_amount'] = self.donation_amount
        if self.donation_date:
            if hasattr(self.donation_date, 'to_alipay_dict'):
                params['donation_date'] = self.donation_date.to_alipay_dict()
            else:
                params['donation_date'] = self.donation_date
        if self.donation_number:
            if hasattr(self.donation_number, 'to_alipay_dict'):
                params['donation_number'] = self.donation_number.to_alipay_dict()
            else:
                params['donation_number'] = self.donation_number
        if self.donation_type:
            if hasattr(self.donation_type, 'to_alipay_dict'):
                params['donation_type'] = self.donation_type.to_alipay_dict()
            else:
                params['donation_type'] = self.donation_type
        if self.donor_name:
            if hasattr(self.donor_name, 'to_alipay_dict'):
                params['donor_name'] = self.donor_name.to_alipay_dict()
            else:
                params['donor_name'] = self.donor_name
        if self.external_client_id:
            if hasattr(self.external_client_id, 'to_alipay_dict'):
                params['external_client_id'] = self.external_client_id.to_alipay_dict()
            else:
                params['external_client_id'] = self.external_client_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.terminal_display:
            if hasattr(self.terminal_display, 'to_alipay_dict'):
                params['terminal_display'] = self.terminal_display.to_alipay_dict()
            else:
                params['terminal_display'] = self.terminal_display
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiDonationServiceCreateModel()
        if 'biz_receipt' in d:
            o.biz_receipt = d['biz_receipt']
        if 'bless_content' in d:
            o.bless_content = d['bless_content']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'donation_amount' in d:
            o.donation_amount = d['donation_amount']
        if 'donation_date' in d:
            o.donation_date = d['donation_date']
        if 'donation_number' in d:
            o.donation_number = d['donation_number']
        if 'donation_type' in d:
            o.donation_type = d['donation_type']
        if 'donor_name' in d:
            o.donor_name = d['donor_name']
        if 'external_client_id' in d:
            o.external_client_id = d['external_client_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'terminal_display' in d:
            o.terminal_display = d['terminal_display']
        return o


