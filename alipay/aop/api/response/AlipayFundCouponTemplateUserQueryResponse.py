#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GiftUserTemplateBoxInfo import GiftUserTemplateBoxInfo


class AlipayFundCouponTemplateUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponTemplateUserQueryResponse, self).__init__()
        self._has_next = None
        self._templates = None

    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def templates(self):
        return self._templates

    @templates.setter
    def templates(self, value):
        if isinstance(value, list):
            self._templates = list()
            for i in value:
                if isinstance(i, GiftUserTemplateBoxInfo):
                    self._templates.append(i)
                else:
                    self._templates.append(GiftUserTemplateBoxInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponTemplateUserQueryResponse, self).parse_response_content(response_content)
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'templates' in response:
            self.templates = response['templates']
