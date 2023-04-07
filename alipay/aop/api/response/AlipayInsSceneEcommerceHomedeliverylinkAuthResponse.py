#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsOpenLogisticsDigestDTO import InsOpenLogisticsDigestDTO


class AlipayInsSceneEcommerceHomedeliverylinkAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommerceHomedeliverylinkAuthResponse, self).__init__()
        self._action_desc = None
        self._action_sub_desc = None
        self._authed_token = None
        self._authed_url = None
        self._delivery_status = None
        self._expiration = None
        self._logistics_digest = None

    @property
    def action_desc(self):
        return self._action_desc

    @action_desc.setter
    def action_desc(self, value):
        self._action_desc = value
    @property
    def action_sub_desc(self):
        return self._action_sub_desc

    @action_sub_desc.setter
    def action_sub_desc(self, value):
        self._action_sub_desc = value
    @property
    def authed_token(self):
        return self._authed_token

    @authed_token.setter
    def authed_token(self, value):
        self._authed_token = value
    @property
    def authed_url(self):
        return self._authed_url

    @authed_url.setter
    def authed_url(self, value):
        self._authed_url = value
    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, value):
        self._expiration = value
    @property
    def logistics_digest(self):
        return self._logistics_digest

    @logistics_digest.setter
    def logistics_digest(self, value):
        if isinstance(value, InsOpenLogisticsDigestDTO):
            self._logistics_digest = value
        else:
            self._logistics_digest = InsOpenLogisticsDigestDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommerceHomedeliverylinkAuthResponse, self).parse_response_content(response_content)
        if 'action_desc' in response:
            self.action_desc = response['action_desc']
        if 'action_sub_desc' in response:
            self.action_sub_desc = response['action_sub_desc']
        if 'authed_token' in response:
            self.authed_token = response['authed_token']
        if 'authed_url' in response:
            self.authed_url = response['authed_url']
        if 'delivery_status' in response:
            self.delivery_status = response['delivery_status']
        if 'expiration' in response:
            self.expiration = response['expiration']
        if 'logistics_digest' in response:
            self.logistics_digest = response['logistics_digest']
