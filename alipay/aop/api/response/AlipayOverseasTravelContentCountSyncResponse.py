#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTravelContentCountSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelContentCountSyncResponse, self).__init__()
        self._results = None

    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value):
        self._results = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelContentCountSyncResponse, self).parse_response_content(response_content)
        if 'results' in response:
            self.results = response['results']
