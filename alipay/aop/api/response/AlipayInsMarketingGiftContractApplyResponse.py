#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsMarketingGiftContractApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingGiftContractApplyResponse, self).__init__()
        self._contract_no = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._gift_prod_code = None
        self._out_biz_no = None
        self._policy_no = None
        self._right_no = None

    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
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
    def gift_prod_code(self):
        return self._gift_prod_code

    @gift_prod_code.setter
    def gift_prod_code(self, value):
        self._gift_prod_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def right_no(self):
        return self._right_no

    @right_no.setter
    def right_no(self, value):
        self._right_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingGiftContractApplyResponse, self).parse_response_content(response_content)
        if 'contract_no' in response:
            self.contract_no = response['contract_no']
        if 'effect_end_time' in response:
            self.effect_end_time = response['effect_end_time']
        if 'effect_start_time' in response:
            self.effect_start_time = response['effect_start_time']
        if 'gift_prod_code' in response:
            self.gift_prod_code = response['gift_prod_code']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'right_no' in response:
            self.right_no = response['right_no']
