#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInquiryServiceSyncModel(object):

    def __init__(self):
        self._average_time = None
        self._data_version = None
        self._doctor_id = None
        self._evaluation_score = None
        self._inquiry_mode = None
        self._inquiry_price = None
        self._inquiry_type = None
        self._inquiry_url = None
        self._isv_code = None
        self._num_of_people_served = None
        self._platform_code = None
        self._service_duration = None
        self._service_id = None
        self._status = None

    @property
    def average_time(self):
        return self._average_time

    @average_time.setter
    def average_time(self, value):
        self._average_time = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def evaluation_score(self):
        return self._evaluation_score

    @evaluation_score.setter
    def evaluation_score(self, value):
        self._evaluation_score = value
    @property
    def inquiry_mode(self):
        return self._inquiry_mode

    @inquiry_mode.setter
    def inquiry_mode(self, value):
        self._inquiry_mode = value
    @property
    def inquiry_price(self):
        return self._inquiry_price

    @inquiry_price.setter
    def inquiry_price(self, value):
        self._inquiry_price = value
    @property
    def inquiry_type(self):
        return self._inquiry_type

    @inquiry_type.setter
    def inquiry_type(self, value):
        self._inquiry_type = value
    @property
    def inquiry_url(self):
        return self._inquiry_url

    @inquiry_url.setter
    def inquiry_url(self, value):
        self._inquiry_url = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def num_of_people_served(self):
        return self._num_of_people_served

    @num_of_people_served.setter
    def num_of_people_served(self, value):
        self._num_of_people_served = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def service_duration(self):
        return self._service_duration

    @service_duration.setter
    def service_duration(self, value):
        self._service_duration = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.average_time:
            if hasattr(self.average_time, 'to_alipay_dict'):
                params['average_time'] = self.average_time.to_alipay_dict()
            else:
                params['average_time'] = self.average_time
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.evaluation_score:
            if hasattr(self.evaluation_score, 'to_alipay_dict'):
                params['evaluation_score'] = self.evaluation_score.to_alipay_dict()
            else:
                params['evaluation_score'] = self.evaluation_score
        if self.inquiry_mode:
            if hasattr(self.inquiry_mode, 'to_alipay_dict'):
                params['inquiry_mode'] = self.inquiry_mode.to_alipay_dict()
            else:
                params['inquiry_mode'] = self.inquiry_mode
        if self.inquiry_price:
            if hasattr(self.inquiry_price, 'to_alipay_dict'):
                params['inquiry_price'] = self.inquiry_price.to_alipay_dict()
            else:
                params['inquiry_price'] = self.inquiry_price
        if self.inquiry_type:
            if hasattr(self.inquiry_type, 'to_alipay_dict'):
                params['inquiry_type'] = self.inquiry_type.to_alipay_dict()
            else:
                params['inquiry_type'] = self.inquiry_type
        if self.inquiry_url:
            if hasattr(self.inquiry_url, 'to_alipay_dict'):
                params['inquiry_url'] = self.inquiry_url.to_alipay_dict()
            else:
                params['inquiry_url'] = self.inquiry_url
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.num_of_people_served:
            if hasattr(self.num_of_people_served, 'to_alipay_dict'):
                params['num_of_people_served'] = self.num_of_people_served.to_alipay_dict()
            else:
                params['num_of_people_served'] = self.num_of_people_served
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.service_duration:
            if hasattr(self.service_duration, 'to_alipay_dict'):
                params['service_duration'] = self.service_duration.to_alipay_dict()
            else:
                params['service_duration'] = self.service_duration
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInquiryServiceSyncModel()
        if 'average_time' in d:
            o.average_time = d['average_time']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'evaluation_score' in d:
            o.evaluation_score = d['evaluation_score']
        if 'inquiry_mode' in d:
            o.inquiry_mode = d['inquiry_mode']
        if 'inquiry_price' in d:
            o.inquiry_price = d['inquiry_price']
        if 'inquiry_type' in d:
            o.inquiry_type = d['inquiry_type']
        if 'inquiry_url' in d:
            o.inquiry_url = d['inquiry_url']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'num_of_people_served' in d:
            o.num_of_people_served = d['num_of_people_served']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'service_duration' in d:
            o.service_duration = d['service_duration']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'status' in d:
            o.status = d['status']
        return o


