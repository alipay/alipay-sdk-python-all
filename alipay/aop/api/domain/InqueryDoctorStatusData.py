#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InquiryChannel import InquiryChannel


class InqueryDoctorStatusData(object):

    def __init__(self):
        self._average_time = None
        self._doctor_platform_status = None
        self._evaluation_score = None
        self._id_no = None
        self._inquiry_channel_list = None
        self._merchant_doctor_id = None
        self._num_of_people_served = None
        self._practicing_doctor_certificate_no = None

    @property
    def average_time(self):
        return self._average_time

    @average_time.setter
    def average_time(self, value):
        self._average_time = value
    @property
    def doctor_platform_status(self):
        return self._doctor_platform_status

    @doctor_platform_status.setter
    def doctor_platform_status(self, value):
        self._doctor_platform_status = value
    @property
    def evaluation_score(self):
        return self._evaluation_score

    @evaluation_score.setter
    def evaluation_score(self, value):
        self._evaluation_score = value
    @property
    def id_no(self):
        return self._id_no

    @id_no.setter
    def id_no(self, value):
        self._id_no = value
    @property
    def inquiry_channel_list(self):
        return self._inquiry_channel_list

    @inquiry_channel_list.setter
    def inquiry_channel_list(self, value):
        if isinstance(value, list):
            self._inquiry_channel_list = list()
            for i in value:
                if isinstance(i, InquiryChannel):
                    self._inquiry_channel_list.append(i)
                else:
                    self._inquiry_channel_list.append(InquiryChannel.from_alipay_dict(i))
    @property
    def merchant_doctor_id(self):
        return self._merchant_doctor_id

    @merchant_doctor_id.setter
    def merchant_doctor_id(self, value):
        self._merchant_doctor_id = value
    @property
    def num_of_people_served(self):
        return self._num_of_people_served

    @num_of_people_served.setter
    def num_of_people_served(self, value):
        self._num_of_people_served = value
    @property
    def practicing_doctor_certificate_no(self):
        return self._practicing_doctor_certificate_no

    @practicing_doctor_certificate_no.setter
    def practicing_doctor_certificate_no(self, value):
        self._practicing_doctor_certificate_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.average_time:
            if hasattr(self.average_time, 'to_alipay_dict'):
                params['average_time'] = self.average_time.to_alipay_dict()
            else:
                params['average_time'] = self.average_time
        if self.doctor_platform_status:
            if hasattr(self.doctor_platform_status, 'to_alipay_dict'):
                params['doctor_platform_status'] = self.doctor_platform_status.to_alipay_dict()
            else:
                params['doctor_platform_status'] = self.doctor_platform_status
        if self.evaluation_score:
            if hasattr(self.evaluation_score, 'to_alipay_dict'):
                params['evaluation_score'] = self.evaluation_score.to_alipay_dict()
            else:
                params['evaluation_score'] = self.evaluation_score
        if self.id_no:
            if hasattr(self.id_no, 'to_alipay_dict'):
                params['id_no'] = self.id_no.to_alipay_dict()
            else:
                params['id_no'] = self.id_no
        if self.inquiry_channel_list:
            if isinstance(self.inquiry_channel_list, list):
                for i in range(0, len(self.inquiry_channel_list)):
                    element = self.inquiry_channel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inquiry_channel_list[i] = element.to_alipay_dict()
            if hasattr(self.inquiry_channel_list, 'to_alipay_dict'):
                params['inquiry_channel_list'] = self.inquiry_channel_list.to_alipay_dict()
            else:
                params['inquiry_channel_list'] = self.inquiry_channel_list
        if self.merchant_doctor_id:
            if hasattr(self.merchant_doctor_id, 'to_alipay_dict'):
                params['merchant_doctor_id'] = self.merchant_doctor_id.to_alipay_dict()
            else:
                params['merchant_doctor_id'] = self.merchant_doctor_id
        if self.num_of_people_served:
            if hasattr(self.num_of_people_served, 'to_alipay_dict'):
                params['num_of_people_served'] = self.num_of_people_served.to_alipay_dict()
            else:
                params['num_of_people_served'] = self.num_of_people_served
        if self.practicing_doctor_certificate_no:
            if hasattr(self.practicing_doctor_certificate_no, 'to_alipay_dict'):
                params['practicing_doctor_certificate_no'] = self.practicing_doctor_certificate_no.to_alipay_dict()
            else:
                params['practicing_doctor_certificate_no'] = self.practicing_doctor_certificate_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InqueryDoctorStatusData()
        if 'average_time' in d:
            o.average_time = d['average_time']
        if 'doctor_platform_status' in d:
            o.doctor_platform_status = d['doctor_platform_status']
        if 'evaluation_score' in d:
            o.evaluation_score = d['evaluation_score']
        if 'id_no' in d:
            o.id_no = d['id_no']
        if 'inquiry_channel_list' in d:
            o.inquiry_channel_list = d['inquiry_channel_list']
        if 'merchant_doctor_id' in d:
            o.merchant_doctor_id = d['merchant_doctor_id']
        if 'num_of_people_served' in d:
            o.num_of_people_served = d['num_of_people_served']
        if 'practicing_doctor_certificate_no' in d:
            o.practicing_doctor_certificate_no = d['practicing_doctor_certificate_no']
        return o


