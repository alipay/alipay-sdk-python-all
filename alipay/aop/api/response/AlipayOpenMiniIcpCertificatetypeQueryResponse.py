#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IcpCertificateTypeList import IcpCertificateTypeList


class AlipayOpenMiniIcpCertificatetypeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIcpCertificatetypeQueryResponse, self).__init__()
        self._certificate_types = None

    @property
    def certificate_types(self):
        return self._certificate_types

    @certificate_types.setter
    def certificate_types(self, value):
        if isinstance(value, list):
            self._certificate_types = list()
            for i in value:
                if isinstance(i, IcpCertificateTypeList):
                    self._certificate_types.append(i)
                else:
                    self._certificate_types.append(IcpCertificateTypeList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIcpCertificatetypeQueryResponse, self).parse_response_content(response_content)
        if 'certificate_types' in response:
            self.certificate_types = response['certificate_types']
