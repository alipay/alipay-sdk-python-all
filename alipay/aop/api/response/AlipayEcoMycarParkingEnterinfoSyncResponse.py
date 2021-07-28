#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingEnterinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingEnterinfoSyncResponse, self).__init__()
        self._agreement_scene = None
        self._agreement_status = None
        self._car_status = None
        self._current_time = None
        self._serial_no = None

    @property
    def agreement_scene(self):
        return self._agreement_scene

    @agreement_scene.setter
    def agreement_scene(self, value):
        self._agreement_scene = value
    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
    @property
    def car_status(self):
        return self._car_status

    @car_status.setter
    def car_status(self, value):
        self._car_status = value
    @property
    def current_time(self):
        return self._current_time

    @current_time.setter
    def current_time(self, value):
        self._current_time = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingEnterinfoSyncResponse, self).parse_response_content(response_content)
        if 'agreement_scene' in response:
            self.agreement_scene = response['agreement_scene']
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
        if 'car_status' in response:
            self.car_status = response['car_status']
        if 'current_time' in response:
            self.current_time = response['current_time']
        if 'serial_no' in response:
            self.serial_no = response['serial_no']
