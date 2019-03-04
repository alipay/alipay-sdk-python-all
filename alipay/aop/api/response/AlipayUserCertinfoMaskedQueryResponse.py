#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MaskedUserCertView import MaskedUserCertView


class AlipayUserCertinfoMaskedQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertinfoMaskedQueryResponse, self).__init__()
        self._cert_views = None

    @property
    def cert_views(self):
        return self._cert_views

    @cert_views.setter
    def cert_views(self, value):
        if isinstance(value, list):
            self._cert_views = list()
            for i in value:
                if isinstance(i, MaskedUserCertView):
                    self._cert_views.append(i)
                else:
                    self._cert_views.append(MaskedUserCertView.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertinfoMaskedQueryResponse, self).parse_response_content(response_content)
        if 'cert_views' in response:
            self.cert_views = response['cert_views']
