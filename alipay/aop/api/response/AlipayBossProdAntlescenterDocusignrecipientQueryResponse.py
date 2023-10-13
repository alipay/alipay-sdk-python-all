#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlescenterDocusignrecipientQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlescenterDocusignrecipientQueryResponse, self).__init__()
        self._view_url = None

    @property
    def view_url(self):
        return self._view_url

    @view_url.setter
    def view_url(self, value):
        self._view_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlescenterDocusignrecipientQueryResponse, self).parse_response_content(response_content)
        if 'view_url' in response:
            self.view_url = response['view_url']
