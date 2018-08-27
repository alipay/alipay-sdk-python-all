#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiPromoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiPromoQueryResponse, self).__init__()
        self._facescore = None

    @property
    def facescore(self):
        return self._facescore

    @facescore.setter
    def facescore(self, value):
        self._facescore = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiPromoQueryResponse, self).parse_response_content(response_content)
        if 'facescore' in response:
            self.facescore = response['facescore']
