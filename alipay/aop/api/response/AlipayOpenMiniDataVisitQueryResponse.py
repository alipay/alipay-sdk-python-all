#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AreaDetail import AreaDetail


class AlipayOpenMiniDataVisitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniDataVisitQueryResponse, self).__init__()
        self._app_pv = None
        self._app_uv = None
        self._area_detail_list = None

    @property
    def app_pv(self):
        return self._app_pv

    @app_pv.setter
    def app_pv(self, value):
        self._app_pv = value
    @property
    def app_uv(self):
        return self._app_uv

    @app_uv.setter
    def app_uv(self, value):
        self._app_uv = value
    @property
    def area_detail_list(self):
        return self._area_detail_list

    @area_detail_list.setter
    def area_detail_list(self, value):
        if isinstance(value, list):
            self._area_detail_list = list()
            for i in value:
                if isinstance(i, AreaDetail):
                    self._area_detail_list.append(i)
                else:
                    self._area_detail_list.append(AreaDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniDataVisitQueryResponse, self).parse_response_content(response_content)
        if 'app_pv' in response:
            self.app_pv = response['app_pv']
        if 'app_uv' in response:
            self.app_uv = response['app_uv']
        if 'area_detail_list' in response:
            self.area_detail_list = response['area_detail_list']
