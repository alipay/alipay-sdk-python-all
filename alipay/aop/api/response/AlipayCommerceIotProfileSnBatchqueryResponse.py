#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProfileSnDetail import ProfileSnDetail


class AlipayCommerceIotProfileSnBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotProfileSnBatchqueryResponse, self).__init__()
        self._sn_list = None

    @property
    def sn_list(self):
        return self._sn_list

    @sn_list.setter
    def sn_list(self, value):
        if isinstance(value, list):
            self._sn_list = list()
            for i in value:
                if isinstance(i, ProfileSnDetail):
                    self._sn_list.append(i)
                else:
                    self._sn_list.append(ProfileSnDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotProfileSnBatchqueryResponse, self).parse_response_content(response_content)
        if 'sn_list' in response:
            self.sn_list = response['sn_list']
