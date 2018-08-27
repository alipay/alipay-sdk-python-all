#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherBillDetail import VoucherBillDetail


class AlipayMarketingVoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherQueryResponse, self).__init__()
        self._available_amount = None
        self._bill_details = None
        self._extend_info = None
        self._gmt_active = None
        self._gmt_create = None
        self._gmt_expired = None
        self._name = None
        self._status = None
        self._template_id = None
        self._total_amount = None
        self._user_id = None
        self._voucher_id = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def bill_details(self):
        return self._bill_details

    @bill_details.setter
    def bill_details(self, value):
        if isinstance(value, list):
            self._bill_details = list()
            for i in value:
                if isinstance(i, VoucherBillDetail):
                    self._bill_details.append(i)
                else:
                    self._bill_details.append(VoucherBillDetail.from_alipay_dict(i))
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherQueryResponse, self).parse_response_content(response_content)
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'bill_details' in response:
            self.bill_details = response['bill_details']
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
        if 'gmt_active' in response:
            self.gmt_active = response['gmt_active']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_expired' in response:
            self.gmt_expired = response['gmt_expired']
        if 'name' in response:
            self.name = response['name']
        if 'status' in response:
            self.status = response['status']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
