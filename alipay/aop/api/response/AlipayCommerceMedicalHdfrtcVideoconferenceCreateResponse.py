#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfrtcVideoconferenceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfrtcVideoconferenceCreateResponse, self).__init__()
        self._video_conference_id = None

    @property
    def video_conference_id(self):
        return self._video_conference_id

    @video_conference_id.setter
    def video_conference_id(self, value):
        self._video_conference_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfrtcVideoconferenceCreateResponse, self).parse_response_content(response_content)
        if 'video_conference_id' in response:
            self.video_conference_id = response['video_conference_id']
