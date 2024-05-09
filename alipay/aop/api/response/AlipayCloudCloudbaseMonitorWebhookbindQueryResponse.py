#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WebhookBind import WebhookBind


class AlipayCloudCloudbaseMonitorWebhookbindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseMonitorWebhookbindQueryResponse, self).__init__()
        self._page_index = None
        self._page_size = None
        self._total = None
        self._webhook_binds = None

    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def webhook_binds(self):
        return self._webhook_binds

    @webhook_binds.setter
    def webhook_binds(self, value):
        if isinstance(value, list):
            self._webhook_binds = list()
            for i in value:
                if isinstance(i, WebhookBind):
                    self._webhook_binds.append(i)
                else:
                    self._webhook_binds.append(WebhookBind.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseMonitorWebhookbindQueryResponse, self).parse_response_content(response_content)
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
        if 'webhook_binds' in response:
            self.webhook_binds = response['webhook_binds']
