#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalUserqueryQuestionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalUserqueryQuestionQueryResponse, self).__init__()
        self._feed_back = None
        self._jump_url = None
        self._query = None
        self._sup_id = None

    @property
    def feed_back(self):
        return self._feed_back

    @feed_back.setter
    def feed_back(self, value):
        self._feed_back = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def sup_id(self):
        return self._sup_id

    @sup_id.setter
    def sup_id(self, value):
        self._sup_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalUserqueryQuestionQueryResponse, self).parse_response_content(response_content)
        if 'feed_back' in response:
            self.feed_back = response['feed_back']
        if 'jump_url' in response:
            self.jump_url = response['jump_url']
        if 'query' in response:
            self.query = response['query']
        if 'sup_id' in response:
            self.sup_id = response['sup_id']
