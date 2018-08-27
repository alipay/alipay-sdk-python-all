#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingVoucherTemplatedetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherTemplatedetailQueryResponse, self).__init__()
        self._amount = None
        self._floor_amount = None
        self._publish_amount = None
        self._publish_count = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._recycle_amount = None
        self._status = None
        self._template_id = None
        self._total_amount = None
        self._used_amount = None
        self._used_count = None
        self._voucher_description = None
        self._voucher_name = None
        self._voucher_quantity = None
        self._voucher_type = None
        self._voucher_valid_period = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def publish_amount(self):
        return self._publish_amount

    @publish_amount.setter
    def publish_amount(self, value):
        self._publish_amount = value
    @property
    def publish_count(self):
        return self._publish_count

    @publish_count.setter
    def publish_count(self, value):
        self._publish_count = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
    @property
    def recycle_amount(self):
        return self._recycle_amount

    @recycle_amount.setter
    def recycle_amount(self, value):
        self._recycle_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def used_amount(self):
        return self._used_amount

    @used_amount.setter
    def used_amount(self, value):
        self._used_amount = value
    @property
    def used_count(self):
        return self._used_count

    @used_count.setter
    def used_count(self, value):
        self._used_count = value
    @property
    def voucher_description(self):
        return self._voucher_description

    @voucher_description.setter
    def voucher_description(self, value):
        self._voucher_description = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_quantity(self):
        return self._voucher_quantity

    @voucher_quantity.setter
    def voucher_quantity(self, value):
        self._voucher_quantity = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def voucher_valid_period(self):
        return self._voucher_valid_period

    @voucher_valid_period.setter
    def voucher_valid_period(self, value):
        self._voucher_valid_period = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherTemplatedetailQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'floor_amount' in response:
            self.floor_amount = response['floor_amount']
        if 'publish_amount' in response:
            self.publish_amount = response['publish_amount']
        if 'publish_count' in response:
            self.publish_count = response['publish_count']
        if 'publish_end_time' in response:
            self.publish_end_time = response['publish_end_time']
        if 'publish_start_time' in response:
            self.publish_start_time = response['publish_start_time']
        if 'recycle_amount' in response:
            self.recycle_amount = response['recycle_amount']
        if 'status' in response:
            self.status = response['status']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'used_amount' in response:
            self.used_amount = response['used_amount']
        if 'used_count' in response:
            self.used_count = response['used_count']
        if 'voucher_description' in response:
            self.voucher_description = response['voucher_description']
        if 'voucher_name' in response:
            self.voucher_name = response['voucher_name']
        if 'voucher_quantity' in response:
            self.voucher_quantity = response['voucher_quantity']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
        if 'voucher_valid_period' in response:
            self.voucher_valid_period = response['voucher_valid_period']
