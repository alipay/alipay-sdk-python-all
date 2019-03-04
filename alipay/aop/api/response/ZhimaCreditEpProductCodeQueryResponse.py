#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizResData import BizResData


class ZhimaCreditEpProductCodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpProductCodeQueryResponse, self).__init__()
        self._biz_info = None
        self._total_cnt = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        if isinstance(value, list):
            self._biz_info = list()
            for i in value:
                if isinstance(i, BizResData):
                    self._biz_info.append(i)
                else:
                    self._biz_info.append(BizResData.from_alipay_dict(i))
    @property
    def total_cnt(self):
        return self._total_cnt

    @total_cnt.setter
    def total_cnt(self, value):
        self._total_cnt = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpProductCodeQueryResponse, self).parse_response_content(response_content)
        if 'biz_info' in response:
            self.biz_info = response['biz_info']
        if 'total_cnt' in response:
            self.total_cnt = response['total_cnt']
