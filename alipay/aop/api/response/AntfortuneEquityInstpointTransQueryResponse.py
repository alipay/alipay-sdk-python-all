#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PointTransInfo import PointTransInfo


class AntfortuneEquityInstpointTransQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneEquityInstpointTransQueryResponse, self).__init__()
        self._trans_info = None

    @property
    def trans_info(self):
        return self._trans_info

    @trans_info.setter
    def trans_info(self, value):
        if isinstance(value, list):
            self._trans_info = list()
            for i in value:
                if isinstance(i, PointTransInfo):
                    self._trans_info.append(i)
                else:
                    self._trans_info.append(PointTransInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntfortuneEquityInstpointTransQueryResponse, self).parse_response_content(response_content)
        if 'trans_info' in response:
            self.trans_info = response['trans_info']
