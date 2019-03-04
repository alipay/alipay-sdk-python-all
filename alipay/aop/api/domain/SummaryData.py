#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SummaryData(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.adult:
            if hasattr(self.adult, 'to_alipay_dict'):
                params['adult'] = self.adult.to_alipay_dict()
            else:
                params['adult'] = self.adult
        if self.avg_stop_time:
            if hasattr(self.avg_stop_time, 'to_alipay_dict'):
                params['avg_stop_time'] = self.avg_stop_time.to_alipay_dict()
            else:
                params['avg_stop_time'] = self.avg_stop_time
        if self.back_interception_rate:
            if hasattr(self.back_interception_rate, 'to_alipay_dict'):
                params['back_interception_rate'] = self.back_interception_rate.to_alipay_dict()
            else:
                params['back_interception_rate'] = self.back_interception_rate
        if self.elder:
            if hasattr(self.elder, 'to_alipay_dict'):
                params['elder'] = self.elder.to_alipay_dict()
            else:
                params['elder'] = self.elder
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.face_interception_rate:
            if hasattr(self.face_interception_rate, 'to_alipay_dict'):
                params['face_interception_rate'] = self.face_interception_rate.to_alipay_dict()
            else:
                params['face_interception_rate'] = self.face_interception_rate
        if self.female:
            if hasattr(self.female, 'to_alipay_dict'):
                params['female'] = self.female.to_alipay_dict()
            else:
                params['female'] = self.female
        if self.male:
            if hasattr(self.male, 'to_alipay_dict'):
                params['male'] = self.male.to_alipay_dict()
            else:
                params['male'] = self.male
        if self.nonage:
            if hasattr(self.nonage, 'to_alipay_dict'):
                params['nonage'] = self.nonage.to_alipay_dict()
            else:
                params['nonage'] = self.nonage
        if self.person_view:
            if hasattr(self.person_view, 'to_alipay_dict'):
                params['person_view'] = self.person_view.to_alipay_dict()
            else:
                params['person_view'] = self.person_view
        if self.side_interception_rate:
            if hasattr(self.side_interception_rate, 'to_alipay_dict'):
                params['side_interception_rate'] = self.side_interception_rate.to_alipay_dict()
            else:
                params['side_interception_rate'] = self.side_interception_rate
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SummaryData()
        if 'adult' in d:
            o.adult = d['adult']
        if 'avg_stop_time' in d:
            o.avg_stop_time = d['avg_stop_time']
        if 'back_interception_rate' in d:
            o.back_interception_rate = d['back_interception_rate']
        if 'elder' in d:
            o.elder = d['elder']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'face_interception_rate' in d:
            o.face_interception_rate = d['face_interception_rate']
        if 'female' in d:
            o.female = d['female']
        if 'male' in d:
            o.male = d['male']
        if 'nonage' in d:
            o.nonage = d['nonage']
        if 'person_view' in d:
            o.person_view = d['person_view']
        if 'side_interception_rate' in d:
            o.side_interception_rate = d['side_interception_rate']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


