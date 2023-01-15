#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MultiDataOpenResult import MultiDataOpenResult


class AlipayMerchantQipanBehaviorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanBehaviorQueryResponse, self).__init__()
        self._multi_data_list = None

    @property
    def multi_data_list(self):
        return self._multi_data_list

    @multi_data_list.setter
    def multi_data_list(self, value):
        if isinstance(value, list):
            self._multi_data_list = list()
            for i in value:
                if isinstance(i, MultiDataOpenResult):
                    self._multi_data_list.append(i)
                else:
                    self._multi_data_list.append(MultiDataOpenResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanBehaviorQueryResponse, self).parse_response_content(response_content)
        if 'multi_data_list' in response:
            self.multi_data_list = response['multi_data_list']
