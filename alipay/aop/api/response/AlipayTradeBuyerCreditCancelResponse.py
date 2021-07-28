#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeBuyerCreditCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeBuyerCreditCancelResponse, self).__init__()
        self._buyer_credit_source = None
        self._buyer_user_id = None
        self._credit_scene = None
        self._grant_credit_quota = None
        self._grant_operation_no = None
        self._grant_status = None
        self._merchant_credit_source = None
        self._merchant_user_id = None

    @property
    def buyer_credit_source(self):
        return self._buyer_credit_source

    @buyer_credit_source.setter
    def buyer_credit_source(self, value):
        self._buyer_credit_source = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def credit_scene(self):
        return self._credit_scene

    @credit_scene.setter
    def credit_scene(self, value):
        self._credit_scene = value
    @property
    def grant_credit_quota(self):
        return self._grant_credit_quota

    @grant_credit_quota.setter
    def grant_credit_quota(self, value):
        self._grant_credit_quota = value
    @property
    def grant_operation_no(self):
        return self._grant_operation_no

    @grant_operation_no.setter
    def grant_operation_no(self, value):
        self._grant_operation_no = value
    @property
    def grant_status(self):
        return self._grant_status

    @grant_status.setter
    def grant_status(self, value):
        self._grant_status = value
    @property
    def merchant_credit_source(self):
        return self._merchant_credit_source

    @merchant_credit_source.setter
    def merchant_credit_source(self, value):
        self._merchant_credit_source = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeBuyerCreditCancelResponse, self).parse_response_content(response_content)
        if 'buyer_credit_source' in response:
            self.buyer_credit_source = response['buyer_credit_source']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'credit_scene' in response:
            self.credit_scene = response['credit_scene']
        if 'grant_credit_quota' in response:
            self.grant_credit_quota = response['grant_credit_quota']
        if 'grant_operation_no' in response:
            self.grant_operation_no = response['grant_operation_no']
        if 'grant_status' in response:
            self.grant_status = response['grant_status']
        if 'merchant_credit_source' in response:
            self.merchant_credit_source = response['merchant_credit_source']
        if 'merchant_user_id' in response:
            self.merchant_user_id = response['merchant_user_id']
