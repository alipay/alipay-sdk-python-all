#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TransportInfo import TransportInfo


class AlipaySocialBaseLifecreationTransportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseLifecreationTransportQueryResponse, self).__init__()
        self._transport_infos = None

    @property
    def transport_infos(self):
        return self._transport_infos

    @transport_infos.setter
    def transport_infos(self, value):
        if isinstance(value, list):
            self._transport_infos = list()
            for i in value:
                if isinstance(i, TransportInfo):
                    self._transport_infos.append(i)
                else:
                    self._transport_infos.append(TransportInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseLifecreationTransportQueryResponse, self).parse_response_content(response_content)
        if 'transport_infos' in response:
            self.transport_infos = response['transport_infos']
