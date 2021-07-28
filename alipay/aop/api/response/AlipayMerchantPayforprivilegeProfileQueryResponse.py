#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PayForPrivilegeCardTemplateConfig import PayForPrivilegeCardTemplateConfig


class AlipayMerchantPayforprivilegeProfileQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantPayforprivilegeProfileQueryResponse, self).__init__()
        self._card_template_config = None

    @property
    def card_template_config(self):
        return self._card_template_config

    @card_template_config.setter
    def card_template_config(self, value):
        if isinstance(value, PayForPrivilegeCardTemplateConfig):
            self._card_template_config = value
        else:
            self._card_template_config = PayForPrivilegeCardTemplateConfig.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantPayforprivilegeProfileQueryResponse, self).parse_response_content(response_content)
        if 'card_template_config' in response:
            self.card_template_config = response['card_template_config']
