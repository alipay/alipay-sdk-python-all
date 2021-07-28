#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsWaybillIstddetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsWaybillIstddetailQueryResponse, self).__init__()
        self._reach_duration = None
        self._rider_lat = None
        self._rider_lng = None
        self._rider_mobile_no = None
        self._rider_name = None
        self._status = None

    @property
    def reach_duration(self):
        return self._reach_duration

    @reach_duration.setter
    def reach_duration(self, value):
        self._reach_duration = value
    @property
    def rider_lat(self):
        return self._rider_lat

    @rider_lat.setter
    def rider_lat(self, value):
        self._rider_lat = value
    @property
    def rider_lng(self):
        return self._rider_lng

    @rider_lng.setter
    def rider_lng(self, value):
        self._rider_lng = value
    @property
    def rider_mobile_no(self):
        return self._rider_mobile_no

    @rider_mobile_no.setter
    def rider_mobile_no(self, value):
        self._rider_mobile_no = value
    @property
    def rider_name(self):
        return self._rider_name

    @rider_name.setter
    def rider_name(self, value):
        self._rider_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsWaybillIstddetailQueryResponse, self).parse_response_content(response_content)
        if 'reach_duration' in response:
            self.reach_duration = response['reach_duration']
        if 'rider_lat' in response:
            self.rider_lat = response['rider_lat']
        if 'rider_lng' in response:
            self.rider_lng = response['rider_lng']
        if 'rider_mobile_no' in response:
            self.rider_mobile_no = response['rider_mobile_no']
        if 'rider_name' in response:
            self.rider_name = response['rider_name']
        if 'status' in response:
            self.status = response['status']
