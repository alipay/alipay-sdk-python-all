#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiQualityTestCloudacptCheckresultSubmitResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiQualityTestCloudacptCheckresultSubmitResponse, self).__init__()
        self._activity_id = None
        self._batch_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiQualityTestCloudacptCheckresultSubmitResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'batch_id' in response:
            self.batch_id = response['batch_id']
