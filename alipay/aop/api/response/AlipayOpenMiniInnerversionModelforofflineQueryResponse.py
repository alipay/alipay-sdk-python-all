#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionModelforofflineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionModelforofflineQueryResponse, self).__init__()
        self._model_json = None
        self._sync_id = None

    @property
    def model_json(self):
        return self._model_json

    @model_json.setter
    def model_json(self, value):
        self._model_json = value
    @property
    def sync_id(self):
        return self._sync_id

    @sync_id.setter
    def sync_id(self, value):
        self._sync_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionModelforofflineQueryResponse, self).parse_response_content(response_content)
        if 'model_json' in response:
            self.model_json = response['model_json']
        if 'sync_id' in response:
            self.sync_id = response['sync_id']
