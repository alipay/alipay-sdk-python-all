#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAntdataassetsUploadjobCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAntdataassetsUploadjobCreateResponse, self).__init__()
        self._uca_dataset_id = None

    @property
    def uca_dataset_id(self):
        return self._uca_dataset_id

    @uca_dataset_id.setter
    def uca_dataset_id(self, value):
        self._uca_dataset_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAntdataassetsUploadjobCreateResponse, self).parse_response_content(response_content)
        if 'uca_dataset_id' in response:
            self.uca_dataset_id = response['uca_dataset_id']
