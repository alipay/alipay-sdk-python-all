#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRecycleInstshopQrcodeConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleInstshopQrcodeConsultResponse, self).__init__()
        self._alipay_recycle_url = None

    @property
    def alipay_recycle_url(self):
        return self._alipay_recycle_url

    @alipay_recycle_url.setter
    def alipay_recycle_url(self, value):
        self._alipay_recycle_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleInstshopQrcodeConsultResponse, self).parse_response_content(response_content)
        if 'alipay_recycle_url' in response:
            self.alipay_recycle_url = response['alipay_recycle_url']
