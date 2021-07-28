#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishSimplyInfo import KbdishSimplyInfo


class KoubeiCateringDishQuerydishQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishQuerydishQueryResponse, self).__init__()
        self._dish_info_list = None
        self._retry = None

    @property
    def dish_info_list(self):
        return self._dish_info_list

    @dish_info_list.setter
    def dish_info_list(self, value):
        if isinstance(value, list):
            self._dish_info_list = list()
            for i in value:
                if isinstance(i, KbdishSimplyInfo):
                    self._dish_info_list.append(i)
                else:
                    self._dish_info_list.append(KbdishSimplyInfo.from_alipay_dict(i))
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishQuerydishQueryResponse, self).parse_response_content(response_content)
        if 'dish_info_list' in response:
            self.dish_info_list = response['dish_info_list']
        if 'retry' in response:
            self.retry = response['retry']
