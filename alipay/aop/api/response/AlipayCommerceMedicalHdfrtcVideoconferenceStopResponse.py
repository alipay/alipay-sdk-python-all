#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfrtcVideoconferenceStopResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfrtcVideoconferenceStopResponse, self).__init__()
        self._video_consult_time = None

    @property
    def video_consult_time(self):
        return self._video_consult_time

    @video_consult_time.setter
    def video_consult_time(self, value):
        self._video_consult_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfrtcVideoconferenceStopResponse, self).parse_response_content(response_content)
        if 'video_consult_time' in response:
            self.video_consult_time = response['video_consult_time']
