#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppMarketingConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppMarketingConsultResponse, self).__init__()
        self._anti_rank = None
        self._assign_discounts = None
        self._biz_tag = None
        self._blind_signature = None
        self._confused_cipher_list = None
        self._image = None
        self._marketing_rank = None
        self._pay_operation_info = None
        self._pre_pay_token = None
        self._text = None

    @property
    def anti_rank(self):
        return self._anti_rank

    @anti_rank.setter
    def anti_rank(self, value):
        self._anti_rank = value
    @property
    def assign_discounts(self):
        return self._assign_discounts

    @assign_discounts.setter
    def assign_discounts(self, value):
        self._assign_discounts = value
    @property
    def biz_tag(self):
        return self._biz_tag

    @biz_tag.setter
    def biz_tag(self, value):
        self._biz_tag = value
    @property
    def blind_signature(self):
        return self._blind_signature

    @blind_signature.setter
    def blind_signature(self, value):
        self._blind_signature = value
    @property
    def confused_cipher_list(self):
        return self._confused_cipher_list

    @confused_cipher_list.setter
    def confused_cipher_list(self, value):
        if isinstance(value, list):
            self._confused_cipher_list = list()
            for i in value:
                self._confused_cipher_list.append(i)
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def marketing_rank(self):
        return self._marketing_rank

    @marketing_rank.setter
    def marketing_rank(self, value):
        self._marketing_rank = value
    @property
    def pay_operation_info(self):
        return self._pay_operation_info

    @pay_operation_info.setter
    def pay_operation_info(self, value):
        self._pay_operation_info = value
    @property
    def pre_pay_token(self):
        return self._pre_pay_token

    @pre_pay_token.setter
    def pre_pay_token(self, value):
        self._pre_pay_token = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppMarketingConsultResponse, self).parse_response_content(response_content)
        if 'anti_rank' in response:
            self.anti_rank = response['anti_rank']
        if 'assign_discounts' in response:
            self.assign_discounts = response['assign_discounts']
        if 'biz_tag' in response:
            self.biz_tag = response['biz_tag']
        if 'blind_signature' in response:
            self.blind_signature = response['blind_signature']
        if 'confused_cipher_list' in response:
            self.confused_cipher_list = response['confused_cipher_list']
        if 'image' in response:
            self.image = response['image']
        if 'marketing_rank' in response:
            self.marketing_rank = response['marketing_rank']
        if 'pay_operation_info' in response:
            self.pay_operation_info = response['pay_operation_info']
        if 'pre_pay_token' in response:
            self.pre_pay_token = response['pre_pay_token']
        if 'text' in response:
            self.text = response['text']
