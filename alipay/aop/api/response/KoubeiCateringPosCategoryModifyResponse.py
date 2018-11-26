#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringPosCategoryModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosCategoryModifyResponse, self).__init__()
        self._cate_id = None

    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosCategoryModifyResponse, self).parse_response_content(response_content)
        if 'cate_id' in response:
            self.cate_id = response['cate_id']
