#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneProductAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneProductAgreementQueryResponse, self).__init__()
        self._agreeement_sign_type = None
        self._alipay_user_id = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._item_id = None
        self._product_sign_no = None
        self._sign_user_id = None
        self._sign_user_type = None
        self._status = None

    @property
    def agreeement_sign_type(self):
        return self._agreeement_sign_type

    @agreeement_sign_type.setter
    def agreeement_sign_type(self, value):
        self._agreeement_sign_type = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def product_sign_no(self):
        return self._product_sign_no

    @product_sign_no.setter
    def product_sign_no(self, value):
        self._product_sign_no = value
    @property
    def sign_user_id(self):
        return self._sign_user_id

    @sign_user_id.setter
    def sign_user_id(self, value):
        self._sign_user_id = value
    @property
    def sign_user_type(self):
        return self._sign_user_type

    @sign_user_type.setter
    def sign_user_type(self, value):
        self._sign_user_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneProductAgreementQueryResponse, self).parse_response_content(response_content)
        if 'agreeement_sign_type' in response:
            self.agreeement_sign_type = response['agreeement_sign_type']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'effect_end_time' in response:
            self.effect_end_time = response['effect_end_time']
        if 'effect_start_time' in response:
            self.effect_start_time = response['effect_start_time']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'product_sign_no' in response:
            self.product_sign_no = response['product_sign_no']
        if 'sign_user_id' in response:
            self.sign_user_id = response['sign_user_id']
        if 'sign_user_type' in response:
            self.sign_user_type = response['sign_user_type']
        if 'status' in response:
            self.status = response['status']
