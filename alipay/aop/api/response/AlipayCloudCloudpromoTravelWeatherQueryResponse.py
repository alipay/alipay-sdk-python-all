#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AiWeatherVo import AiWeatherVo


class AlipayCloudCloudpromoTravelWeatherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoTravelWeatherQueryResponse, self).__init__()
        self._ai_weather_vo = None
        self._result_url = None

    @property
    def ai_weather_vo(self):
        return self._ai_weather_vo

    @ai_weather_vo.setter
    def ai_weather_vo(self, value):
        if isinstance(value, AiWeatherVo):
            self._ai_weather_vo = value
        else:
            self._ai_weather_vo = AiWeatherVo.from_alipay_dict(value)
    @property
    def result_url(self):
        return self._result_url

    @result_url.setter
    def result_url(self, value):
        self._result_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoTravelWeatherQueryResponse, self).parse_response_content(response_content)
        if 'ai_weather_vo' in response:
            self.ai_weather_vo = response['ai_weather_vo']
        if 'result_url' in response:
            self.result_url = response['result_url']
