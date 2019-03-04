#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataIotdataDataTotalQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataIotdataDataTotalQueryResponse, self).__init__()
        self._adult = None
        self._avg_stop_time = None
        self._back_interception_rate = None
        self._elder = None
        self._end_time = None
        self._face_interception_rate = None
        self._female = None
        self._male = None
        self._nonage = None
        self._person_view = None
        self._side_interception_rate = None
        self._start_time = None

    @property
    def adult(self):
        return self._adult

    @adult.setter
    def adult(self, value):
        self._adult = value
    @property
    def avg_stop_time(self):
        return self._avg_stop_time

    @avg_stop_time.setter
    def avg_stop_time(self, value):
        self._avg_stop_time = value
    @property
    def back_interception_rate(self):
        return self._back_interception_rate

    @back_interception_rate.setter
    def back_interception_rate(self, value):
        self._back_interception_rate = value
    @property
    def elder(self):
        return self._elder

    @elder.setter
    def elder(self, value):
        self._elder = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def face_interception_rate(self):
        return self._face_interception_rate

    @face_interception_rate.setter
    def face_interception_rate(self, value):
        self._face_interception_rate = value
    @property
    def female(self):
        return self._female

    @female.setter
    def female(self, value):
        self._female = value
    @property
    def male(self):
        return self._male

    @male.setter
    def male(self, value):
        self._male = value
    @property
    def nonage(self):
        return self._nonage

    @nonage.setter
    def nonage(self, value):
        self._nonage = value
    @property
    def person_view(self):
        return self._person_view

    @person_view.setter
    def person_view(self, value):
        self._person_view = value
    @property
    def side_interception_rate(self):
        return self._side_interception_rate

    @side_interception_rate.setter
    def side_interception_rate(self, value):
        self._side_interception_rate = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataIotdataDataTotalQueryResponse, self).parse_response_content(response_content)
        if 'adult' in response:
            self.adult = response['adult']
        if 'avg_stop_time' in response:
            self.avg_stop_time = response['avg_stop_time']
        if 'back_interception_rate' in response:
            self.back_interception_rate = response['back_interception_rate']
        if 'elder' in response:
            self.elder = response['elder']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'face_interception_rate' in response:
            self.face_interception_rate = response['face_interception_rate']
        if 'female' in response:
            self.female = response['female']
        if 'male' in response:
            self.male = response['male']
        if 'nonage' in response:
            self.nonage = response['nonage']
        if 'person_view' in response:
            self.person_view = response['person_view']
        if 'side_interception_rate' in response:
            self.side_interception_rate = response['side_interception_rate']
        if 'start_time' in response:
            self.start_time = response['start_time']
