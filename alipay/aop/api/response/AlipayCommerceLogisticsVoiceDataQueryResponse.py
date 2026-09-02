#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LogisticsVoiceSceneData import LogisticsVoiceSceneData


class AlipayCommerceLogisticsVoiceDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsVoiceDataQueryResponse, self).__init__()
        self._cur_page_max_data_id = None
        self._data_list = None
        self._has_more = None

    @property
    def cur_page_max_data_id(self):
        return self._cur_page_max_data_id

    @cur_page_max_data_id.setter
    def cur_page_max_data_id(self, value):
        self._cur_page_max_data_id = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, LogisticsVoiceSceneData):
                    self._data_list.append(i)
                else:
                    self._data_list.append(LogisticsVoiceSceneData.from_alipay_dict(i))
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsVoiceDataQueryResponse, self).parse_response_content(response_content)
        if 'cur_page_max_data_id' in response:
            self.cur_page_max_data_id = response['cur_page_max_data_id']
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'has_more' in response:
            self.has_more = response['has_more']
