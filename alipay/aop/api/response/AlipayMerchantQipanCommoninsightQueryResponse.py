#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PortraitsDataTgiVO import PortraitsDataTgiVO


class AlipayMerchantQipanCommoninsightQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanCommoninsightQueryResponse, self).__init__()
        self._portraits_data_tgi = None

    @property
    def portraits_data_tgi(self):
        return self._portraits_data_tgi

    @portraits_data_tgi.setter
    def portraits_data_tgi(self, value):
        if isinstance(value, PortraitsDataTgiVO):
            self._portraits_data_tgi = value
        else:
            self._portraits_data_tgi = PortraitsDataTgiVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanCommoninsightQueryResponse, self).parse_response_content(response_content)
        if 'portraits_data_tgi' in response:
            self.portraits_data_tgi = response['portraits_data_tgi']
