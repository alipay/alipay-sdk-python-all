#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppVisitTrendDataResponse import AppVisitTrendDataResponse


class AlipayOpenMiniDataVisittrendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniDataVisittrendQueryResponse, self).__init__()
        self._app_visit_trend_data_list_response = None

    @property
    def app_visit_trend_data_list_response(self):
        return self._app_visit_trend_data_list_response

    @app_visit_trend_data_list_response.setter
    def app_visit_trend_data_list_response(self, value):
        if isinstance(value, list):
            self._app_visit_trend_data_list_response = list()
            for i in value:
                if isinstance(i, AppVisitTrendDataResponse):
                    self._app_visit_trend_data_list_response.append(i)
                else:
                    self._app_visit_trend_data_list_response.append(AppVisitTrendDataResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniDataVisittrendQueryResponse, self).parse_response_content(response_content)
        if 'app_visit_trend_data_list_response' in response:
            self.app_visit_trend_data_list_response = response['app_visit_trend_data_list_response']
