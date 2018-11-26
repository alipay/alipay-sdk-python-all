#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NearMallBo import NearMallBo


class KoubeiMarketingDataNearmallQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataNearmallQueryResponse, self).__init__()
        self._near_mall_bos = None

    @property
    def near_mall_bos(self):
        return self._near_mall_bos

    @near_mall_bos.setter
    def near_mall_bos(self, value):
        if isinstance(value, list):
            self._near_mall_bos = list()
            for i in value:
                if isinstance(i, NearMallBo):
                    self._near_mall_bos.append(i)
                else:
                    self._near_mall_bos.append(NearMallBo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataNearmallQueryResponse, self).parse_response_content(response_content)
        if 'near_mall_bos' in response:
            self.near_mall_bos = response['near_mall_bos']
