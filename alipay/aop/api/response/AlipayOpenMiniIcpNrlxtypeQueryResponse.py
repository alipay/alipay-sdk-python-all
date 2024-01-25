#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IcpNrlxTypeList import IcpNrlxTypeList


class AlipayOpenMiniIcpNrlxtypeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIcpNrlxtypeQueryResponse, self).__init__()
        self._nrlx_types = None

    @property
    def nrlx_types(self):
        return self._nrlx_types

    @nrlx_types.setter
    def nrlx_types(self, value):
        if isinstance(value, list):
            self._nrlx_types = list()
            for i in value:
                if isinstance(i, IcpNrlxTypeList):
                    self._nrlx_types.append(i)
                else:
                    self._nrlx_types.append(IcpNrlxTypeList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIcpNrlxtypeQueryResponse, self).parse_response_content(response_content)
        if 'nrlx_types' in response:
            self.nrlx_types = response['nrlx_types']
