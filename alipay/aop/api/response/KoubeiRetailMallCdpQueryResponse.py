#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CdpDisplayContent import CdpDisplayContent


class KoubeiRetailMallCdpQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailMallCdpQueryResponse, self).__init__()
        self._cdp_content_list = None

    @property
    def cdp_content_list(self):
        return self._cdp_content_list

    @cdp_content_list.setter
    def cdp_content_list(self, value):
        if isinstance(value, list):
            self._cdp_content_list = list()
            for i in value:
                if isinstance(i, CdpDisplayContent):
                    self._cdp_content_list.append(i)
                else:
                    self._cdp_content_list.append(CdpDisplayContent.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailMallCdpQueryResponse, self).parse_response_content(response_content)
        if 'cdp_content_list' in response:
            self.cdp_content_list = response['cdp_content_list']
