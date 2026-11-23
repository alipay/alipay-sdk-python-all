#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingPointOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingPointOrderQueryResponse, self).__init__()
        self._award_status = None
        self._benefit_id = None
        self._card_template_id = None
        self._exchange_order_id = None
        self._order_status = None
        self._point_amount = None
        self._voucher_activity_id = None
        self._voucher_template_id = None
        self._voucher_type = None

    @property
    def award_status(self):
        return self._award_status

    @award_status.setter
    def award_status(self, value):
        self._award_status = value
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def exchange_order_id(self):
        return self._exchange_order_id

    @exchange_order_id.setter
    def exchange_order_id(self, value):
        self._exchange_order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def point_amount(self):
        return self._point_amount

    @point_amount.setter
    def point_amount(self, value):
        self._point_amount = value
    @property
    def voucher_activity_id(self):
        return self._voucher_activity_id

    @voucher_activity_id.setter
    def voucher_activity_id(self, value):
        self._voucher_activity_id = value
    @property
    def voucher_template_id(self):
        return self._voucher_template_id

    @voucher_template_id.setter
    def voucher_template_id(self, value):
        self._voucher_template_id = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingPointOrderQueryResponse, self).parse_response_content(response_content)
        if 'award_status' in response:
            self.award_status = response['award_status']
        if 'benefit_id' in response:
            self.benefit_id = response['benefit_id']
        if 'card_template_id' in response:
            self.card_template_id = response['card_template_id']
        if 'exchange_order_id' in response:
            self.exchange_order_id = response['exchange_order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'point_amount' in response:
            self.point_amount = response['point_amount']
        if 'voucher_activity_id' in response:
            self.voucher_activity_id = response['voucher_activity_id']
        if 'voucher_template_id' in response:
            self.voucher_template_id = response['voucher_template_id']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
