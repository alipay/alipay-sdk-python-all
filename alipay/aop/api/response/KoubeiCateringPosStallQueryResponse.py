#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StallModel import StallModel


class KoubeiCateringPosStallQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosStallQueryResponse, self).__init__()
        self._no_set_stall = None
        self._repeat_set_stall = None
        self._stall_model_list = None

    @property
    def no_set_stall(self):
        return self._no_set_stall

    @no_set_stall.setter
    def no_set_stall(self, value):
        self._no_set_stall = value
    @property
    def repeat_set_stall(self):
        return self._repeat_set_stall

    @repeat_set_stall.setter
    def repeat_set_stall(self, value):
        self._repeat_set_stall = value
    @property
    def stall_model_list(self):
        return self._stall_model_list

    @stall_model_list.setter
    def stall_model_list(self, value):
        if isinstance(value, list):
            self._stall_model_list = list()
            for i in value:
                if isinstance(i, StallModel):
                    self._stall_model_list.append(i)
                else:
                    self._stall_model_list.append(StallModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosStallQueryResponse, self).parse_response_content(response_content)
        if 'no_set_stall' in response:
            self.no_set_stall = response['no_set_stall']
        if 'repeat_set_stall' in response:
            self.repeat_set_stall = response['repeat_set_stall']
        if 'stall_model_list' in response:
            self.stall_model_list = response['stall_model_list']
