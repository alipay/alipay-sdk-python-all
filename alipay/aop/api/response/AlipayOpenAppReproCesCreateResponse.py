#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Gavinmed import Gavinmed


class AlipayOpenAppReproCesCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppReproCesCreateResponse, self).__init__()
        self._resname = None
        self._result = None

    @property
    def resname(self):
        return self._resname

    @resname.setter
    def resname(self, value):
        if isinstance(value, list):
            self._resname = list()
            for i in value:
                if isinstance(i, Gavinmed):
                    self._resname.append(i)
                else:
                    self._resname.append(Gavinmed.from_alipay_dict(i))
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                self._result.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppReproCesCreateResponse, self).parse_response_content(response_content)
        if 'resname' in response:
            self.resname = response['resname']
        if 'result' in response:
            self.result = response['result']
