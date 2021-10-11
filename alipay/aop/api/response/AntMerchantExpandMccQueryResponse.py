#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MccQueryInfo import MccQueryInfo


class AntMerchantExpandMccQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMccQueryResponse, self).__init__()
        self._mcc_info_list = None

    @property
    def mcc_info_list(self):
        return self._mcc_info_list

    @mcc_info_list.setter
    def mcc_info_list(self, value):
        if isinstance(value, list):
            self._mcc_info_list = list()
            for i in value:
                if isinstance(i, MccQueryInfo):
                    self._mcc_info_list.append(i)
                else:
                    self._mcc_info_list.append(MccQueryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMccQueryResponse, self).parse_response_content(response_content)
        if 'mcc_info_list' in response:
            self.mcc_info_list = response['mcc_info_list']
