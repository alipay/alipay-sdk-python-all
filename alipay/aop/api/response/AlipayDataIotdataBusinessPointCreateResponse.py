#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataIotdataBusinessPointCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataIotdataBusinessPointCreateResponse, self).__init__()
        self._point_desc = None
        self._point_id = None
        self._point_name = None
        self._remark = None
        self._status = None

    @property
    def point_desc(self):
        return self._point_desc

    @point_desc.setter
    def point_desc(self, value):
        self._point_desc = value
    @property
    def point_id(self):
        return self._point_id

    @point_id.setter
    def point_id(self, value):
        self._point_id = value
    @property
    def point_name(self):
        return self._point_name

    @point_name.setter
    def point_name(self, value):
        self._point_name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataIotdataBusinessPointCreateResponse, self).parse_response_content(response_content)
        if 'point_desc' in response:
            self.point_desc = response['point_desc']
        if 'point_id' in response:
            self.point_id = response['point_id']
        if 'point_name' in response:
            self.point_name = response['point_name']
        if 'remark' in response:
            self.remark = response['remark']
        if 'status' in response:
            self.status = response['status']
