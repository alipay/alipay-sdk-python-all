#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DentalInquiryArchivesDiseaseInfo import DentalInquiryArchivesDiseaseInfo


class DentalInquiryArchivesInfo(object):

    def __init__(self):
        self._diseases = None
        self._doctor_avatar = None
        self._doctor_name = None
        self._doctor_suggestion = None
        self._doctor_title = None
        self._health_level = None
        self._health_score = None
        self._inquiry_time = None
        self._out_doctor_id = None
        self._out_shop_id = None

    @property
    def diseases(self):
        return self._diseases

    @diseases.setter
    def diseases(self, value):
        if isinstance(value, list):
            self._diseases = list()
            for i in value:
                if isinstance(i, DentalInquiryArchivesDiseaseInfo):
                    self._diseases.append(i)
                else:
                    self._diseases.append(DentalInquiryArchivesDiseaseInfo.from_alipay_dict(i))
    @property
    def doctor_avatar(self):
        return self._doctor_avatar

    @doctor_avatar.setter
    def doctor_avatar(self, value):
        self._doctor_avatar = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def doctor_suggestion(self):
        return self._doctor_suggestion

    @doctor_suggestion.setter
    def doctor_suggestion(self, value):
        self._doctor_suggestion = value
    @property
    def doctor_title(self):
        return self._doctor_title

    @doctor_title.setter
    def doctor_title(self, value):
        self._doctor_title = value
    @property
    def health_level(self):
        return self._health_level

    @health_level.setter
    def health_level(self, value):
        self._health_level = value
    @property
    def health_score(self):
        return self._health_score

    @health_score.setter
    def health_score(self, value):
        self._health_score = value
    @property
    def inquiry_time(self):
        return self._inquiry_time

    @inquiry_time.setter
    def inquiry_time(self, value):
        self._inquiry_time = value
    @property
    def out_doctor_id(self):
        return self._out_doctor_id

    @out_doctor_id.setter
    def out_doctor_id(self, value):
        self._out_doctor_id = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.diseases:
            if isinstance(self.diseases, list):
                for i in range(0, len(self.diseases)):
                    element = self.diseases[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.diseases[i] = element.to_alipay_dict()
            if hasattr(self.diseases, 'to_alipay_dict'):
                params['diseases'] = self.diseases.to_alipay_dict()
            else:
                params['diseases'] = self.diseases
        if self.doctor_avatar:
            if hasattr(self.doctor_avatar, 'to_alipay_dict'):
                params['doctor_avatar'] = self.doctor_avatar.to_alipay_dict()
            else:
                params['doctor_avatar'] = self.doctor_avatar
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.doctor_suggestion:
            if hasattr(self.doctor_suggestion, 'to_alipay_dict'):
                params['doctor_suggestion'] = self.doctor_suggestion.to_alipay_dict()
            else:
                params['doctor_suggestion'] = self.doctor_suggestion
        if self.doctor_title:
            if hasattr(self.doctor_title, 'to_alipay_dict'):
                params['doctor_title'] = self.doctor_title.to_alipay_dict()
            else:
                params['doctor_title'] = self.doctor_title
        if self.health_level:
            if hasattr(self.health_level, 'to_alipay_dict'):
                params['health_level'] = self.health_level.to_alipay_dict()
            else:
                params['health_level'] = self.health_level
        if self.health_score:
            if hasattr(self.health_score, 'to_alipay_dict'):
                params['health_score'] = self.health_score.to_alipay_dict()
            else:
                params['health_score'] = self.health_score
        if self.inquiry_time:
            if hasattr(self.inquiry_time, 'to_alipay_dict'):
                params['inquiry_time'] = self.inquiry_time.to_alipay_dict()
            else:
                params['inquiry_time'] = self.inquiry_time
        if self.out_doctor_id:
            if hasattr(self.out_doctor_id, 'to_alipay_dict'):
                params['out_doctor_id'] = self.out_doctor_id.to_alipay_dict()
            else:
                params['out_doctor_id'] = self.out_doctor_id
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DentalInquiryArchivesInfo()
        if 'diseases' in d:
            o.diseases = d['diseases']
        if 'doctor_avatar' in d:
            o.doctor_avatar = d['doctor_avatar']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'doctor_suggestion' in d:
            o.doctor_suggestion = d['doctor_suggestion']
        if 'doctor_title' in d:
            o.doctor_title = d['doctor_title']
        if 'health_level' in d:
            o.health_level = d['health_level']
        if 'health_score' in d:
            o.health_score = d['health_score']
        if 'inquiry_time' in d:
            o.inquiry_time = d['inquiry_time']
        if 'out_doctor_id' in d:
            o.out_doctor_id = d['out_doctor_id']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        return o


