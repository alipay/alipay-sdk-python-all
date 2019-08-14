#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndirectIsvInfo import IndirectIsvInfo


class AntMerchantExpandIndirectTiansuoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectTiansuoQueryResponse, self).__init__()
        self._indirect_isv_info = None

    @property
    def indirect_isv_info(self):
        return self._indirect_isv_info

    @indirect_isv_info.setter
    def indirect_isv_info(self, value):
        if isinstance(value, list):
            self._indirect_isv_info = list()
            for i in value:
                if isinstance(i, IndirectIsvInfo):
                    self._indirect_isv_info.append(i)
                else:
                    self._indirect_isv_info.append(IndirectIsvInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectTiansuoQueryResponse, self).parse_response_content(response_content)
        if 'indirect_isv_info' in response:
            self.indirect_isv_info = response['indirect_isv_info']
