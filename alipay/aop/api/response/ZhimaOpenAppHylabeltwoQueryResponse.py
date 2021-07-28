#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Hylabel import Hylabel


class ZhimaOpenAppHylabeltwoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaOpenAppHylabeltwoQueryResponse, self).__init__()
        self._hylabel_list = None

    @property
    def hylabel_list(self):
        return self._hylabel_list

    @hylabel_list.setter
    def hylabel_list(self, value):
        if isinstance(value, list):
            self._hylabel_list = list()
            for i in value:
                if isinstance(i, Hylabel):
                    self._hylabel_list.append(i)
                else:
                    self._hylabel_list.append(Hylabel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaOpenAppHylabeltwoQueryResponse, self).parse_response_content(response_content)
        if 'hylabel_list' in response:
            self.hylabel_list = response['hylabel_list']
