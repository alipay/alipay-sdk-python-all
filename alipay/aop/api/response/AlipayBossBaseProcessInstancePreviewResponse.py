#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BPOpenApiInstancePreviewStep import BPOpenApiInstancePreviewStep


class AlipayBossBaseProcessInstancePreviewResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseProcessInstancePreviewResponse, self).__init__()
        self._preview_step = None

    @property
    def preview_step(self):
        return self._preview_step

    @preview_step.setter
    def preview_step(self, value):
        if isinstance(value, BPOpenApiInstancePreviewStep):
            self._preview_step = value
        else:
            self._preview_step = BPOpenApiInstancePreviewStep.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseProcessInstancePreviewResponse, self).parse_response_content(response_content)
        if 'preview_step' in response:
            self.preview_step = response['preview_step']
