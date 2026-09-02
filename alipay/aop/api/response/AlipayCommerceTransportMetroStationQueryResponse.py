#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LbsVO import LbsVO
from alipay.aop.api.domain.LineVO import LineVO


class AlipayCommerceTransportMetroStationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportMetroStationQueryResponse, self).__init__()
        self._lbs = None
        self._lines = None
        self._link = None
        self._station_code = None
        self._station_name = None

    @property
    def lbs(self):
        return self._lbs

    @lbs.setter
    def lbs(self, value):
        if isinstance(value, LbsVO):
            self._lbs = value
        else:
            self._lbs = LbsVO.from_alipay_dict(value)
    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        if isinstance(value, list):
            self._lines = list()
            for i in value:
                if isinstance(i, LineVO):
                    self._lines.append(i)
                else:
                    self._lines.append(LineVO.from_alipay_dict(i))
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def station_code(self):
        return self._station_code

    @station_code.setter
    def station_code(self, value):
        self._station_code = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportMetroStationQueryResponse, self).parse_response_content(response_content)
        if 'lbs' in response:
            self.lbs = response['lbs']
        if 'lines' in response:
            self.lines = response['lines']
        if 'link' in response:
            self.link = response['link']
        if 'station_code' in response:
            self.station_code = response['station_code']
        if 'station_name' in response:
            self.station_name = response['station_name']
