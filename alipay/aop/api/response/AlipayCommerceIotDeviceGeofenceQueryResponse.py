#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FenceEvent import FenceEvent


class AlipayCommerceIotDeviceGeofenceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceGeofenceQueryResponse, self).__init__()
        self._bind_device = None
        self._fence_events = None

    @property
    def bind_device(self):
        return self._bind_device

    @bind_device.setter
    def bind_device(self, value):
        if isinstance(value, list):
            self._bind_device = list()
            for i in value:
                self._bind_device.append(i)
    @property
    def fence_events(self):
        return self._fence_events

    @fence_events.setter
    def fence_events(self, value):
        if isinstance(value, list):
            self._fence_events = list()
            for i in value:
                if isinstance(i, FenceEvent):
                    self._fence_events.append(i)
                else:
                    self._fence_events.append(FenceEvent.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceGeofenceQueryResponse, self).parse_response_content(response_content)
        if 'bind_device' in response:
            self.bind_device = response['bind_device']
        if 'fence_events' in response:
            self.fence_events = response['fence_events']
