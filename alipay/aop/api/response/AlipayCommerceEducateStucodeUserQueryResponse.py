#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StuStatusArchive import StuStatusArchive


class AlipayCommerceEducateStucodeUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateStucodeUserQueryResponse, self).__init__()
        self._archive = None
        self._stu_certify = None

    @property
    def archive(self):
        return self._archive

    @archive.setter
    def archive(self, value):
        if isinstance(value, StuStatusArchive):
            self._archive = value
        else:
            self._archive = StuStatusArchive.from_alipay_dict(value)
    @property
    def stu_certify(self):
        return self._stu_certify

    @stu_certify.setter
    def stu_certify(self, value):
        self._stu_certify = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateStucodeUserQueryResponse, self).parse_response_content(response_content)
        if 'archive' in response:
            self.archive = response['archive']
        if 'stu_certify' in response:
            self.stu_certify = response['stu_certify']
