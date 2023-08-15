#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RefererSetting import RefererSetting


class AlipayCloudCloudrunStaticsiteRefererQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunStaticsiteRefererQueryResponse, self).__init__()
        self._referer = None

    @property
    def referer(self):
        return self._referer

    @referer.setter
    def referer(self, value):
        if isinstance(value, RefererSetting):
            self._referer = value
        else:
            self._referer = RefererSetting.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunStaticsiteRefererQueryResponse, self).parse_response_content(response_content)
        if 'referer' in response:
            self.referer = response['referer']
