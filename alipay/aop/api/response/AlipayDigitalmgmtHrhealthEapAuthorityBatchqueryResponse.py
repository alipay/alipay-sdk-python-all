#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EapAuthVO import EapAuthVO


class AlipayDigitalmgmtHrhealthEapAuthorityBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtHrhealthEapAuthorityBatchqueryResponse, self).__init__()
        self._eap_auth_vo = None

    @property
    def eap_auth_vo(self):
        return self._eap_auth_vo

    @eap_auth_vo.setter
    def eap_auth_vo(self, value):
        if isinstance(value, list):
            self._eap_auth_vo = list()
            for i in value:
                if isinstance(i, EapAuthVO):
                    self._eap_auth_vo.append(i)
                else:
                    self._eap_auth_vo.append(EapAuthVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtHrhealthEapAuthorityBatchqueryResponse, self).parse_response_content(response_content)
        if 'eap_auth_vo' in response:
            self.eap_auth_vo = response['eap_auth_vo']
