#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExternalContact import ExternalContact


class AlipayEbppCommunityPropertyCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityPropertyCreateResponse, self).__init__()
        self._contacts = None
        self._property_short_name = None

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, value):
        if isinstance(value, ExternalContact):
            self._contacts = value
        else:
            self._contacts = ExternalContact.from_alipay_dict(value)
    @property
    def property_short_name(self):
        return self._property_short_name

    @property_short_name.setter
    def property_short_name(self, value):
        self._property_short_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityPropertyCreateResponse, self).parse_response_content(response_content)
        if 'contacts' in response:
            self.contacts = response['contacts']
        if 'property_short_name' in response:
            self.property_short_name = response['property_short_name']
