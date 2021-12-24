#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GiftUserTemplateInfo import GiftUserTemplateInfo


class AlipayFundCouponTemplateUserCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponTemplateUserCreateResponse, self).__init__()
        self._template_info = None
        self._user_template_id = None

    @property
    def template_info(self):
        return self._template_info

    @template_info.setter
    def template_info(self, value):
        if isinstance(value, GiftUserTemplateInfo):
            self._template_info = value
        else:
            self._template_info = GiftUserTemplateInfo.from_alipay_dict(value)
    @property
    def user_template_id(self):
        return self._user_template_id

    @user_template_id.setter
    def user_template_id(self, value):
        self._user_template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponTemplateUserCreateResponse, self).parse_response_content(response_content)
        if 'template_info' in response:
            self.template_info = response['template_info']
        if 'user_template_id' in response:
            self.user_template_id = response['user_template_id']
