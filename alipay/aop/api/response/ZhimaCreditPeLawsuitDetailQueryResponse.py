#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpInfo import EpInfo


class ZhimaCreditPeLawsuitDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeLawsuitDetailQueryResponse, self).__init__()
        self._biz_no = None
        self._lawsuit_detail = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def lawsuit_detail(self):
        return self._lawsuit_detail

    @lawsuit_detail.setter
    def lawsuit_detail(self, value):
        if isinstance(value, EpInfo):
            self._lawsuit_detail = value
        else:
            self._lawsuit_detail = EpInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeLawsuitDetailQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'lawsuit_detail' in response:
            self.lawsuit_detail = response['lawsuit_detail']
