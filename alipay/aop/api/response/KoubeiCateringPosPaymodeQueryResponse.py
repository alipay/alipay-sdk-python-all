#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PayModeModel import PayModeModel


class KoubeiCateringPosPaymodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosPaymodeQueryResponse, self).__init__()
        self._pay_mode_model_list = None

    @property
    def pay_mode_model_list(self):
        return self._pay_mode_model_list

    @pay_mode_model_list.setter
    def pay_mode_model_list(self, value):
        if isinstance(value, list):
            self._pay_mode_model_list = list()
            for i in value:
                if isinstance(i, PayModeModel):
                    self._pay_mode_model_list.append(i)
                else:
                    self._pay_mode_model_list.append(PayModeModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosPaymodeQueryResponse, self).parse_response_content(response_content)
        if 'pay_mode_model_list' in response:
            self.pay_mode_model_list = response['pay_mode_model_list']
