#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserFamilyShareZmgoInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserFamilyShareZmgoInitializeResponse, self).__init__()
        self._family_sharing_link = None
        self._has_sharing = None
        self._shareable = None

    @property
    def family_sharing_link(self):
        return self._family_sharing_link

    @family_sharing_link.setter
    def family_sharing_link(self, value):
        self._family_sharing_link = value
    @property
    def has_sharing(self):
        return self._has_sharing

    @has_sharing.setter
    def has_sharing(self, value):
        self._has_sharing = value
    @property
    def shareable(self):
        return self._shareable

    @shareable.setter
    def shareable(self, value):
        self._shareable = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserFamilyShareZmgoInitializeResponse, self).parse_response_content(response_content)
        if 'family_sharing_link' in response:
            self.family_sharing_link = response['family_sharing_link']
        if 'has_sharing' in response:
            self.has_sharing = response['has_sharing']
        if 'shareable' in response:
            self.shareable = response['shareable']
