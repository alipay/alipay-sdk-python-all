#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UrlBindingInfo import UrlBindingInfo


class AlipayOpenSpNordermaterialsapplyMaterialsurlbindingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyMaterialsurlbindingQueryResponse, self).__init__()
        self._url_binding_infos = None

    @property
    def url_binding_infos(self):
        return self._url_binding_infos

    @url_binding_infos.setter
    def url_binding_infos(self, value):
        if isinstance(value, list):
            self._url_binding_infos = list()
            for i in value:
                if isinstance(i, UrlBindingInfo):
                    self._url_binding_infos.append(i)
                else:
                    self._url_binding_infos.append(UrlBindingInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyMaterialsurlbindingQueryResponse, self).parse_response_content(response_content)
        if 'url_binding_infos' in response:
            self.url_binding_infos = response['url_binding_infos']
