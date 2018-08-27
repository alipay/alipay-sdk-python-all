#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZmWatchListDetail import ZmWatchListDetail


class ZhimaCreditWatchlistiiGetResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditWatchlistiiGetResponse, self).__init__()
        self._biz_no = None
        self._details = None
        self._is_matched = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                if isinstance(i, ZmWatchListDetail):
                    self._details.append(i)
                else:
                    self._details.append(ZmWatchListDetail.from_alipay_dict(i))
    @property
    def is_matched(self):
        return self._is_matched

    @is_matched.setter
    def is_matched(self, value):
        self._is_matched = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditWatchlistiiGetResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'details' in response:
            self.details = response['details']
        if 'is_matched' in response:
            self.is_matched = response['is_matched']
