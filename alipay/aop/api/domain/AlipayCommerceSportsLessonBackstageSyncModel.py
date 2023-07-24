#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsLessonBackstageSyncModel(object):

    def __init__(self):
        self._deliver_end_time = None
        self._deliver_start_time = None
        self._lesson_calorie = None
        self._lesson_charge_type = None
        self._lesson_duration = None
        self._lesson_ext_tag = None
        self._lesson_image = None
        self._lesson_intro = None
        self._lesson_intro_image = None
        self._lesson_limit_free_end_time = None
        self._lesson_limit_free_start_time = None
        self._lesson_name = None
        self._lesson_out_id = None
        self._lesson_source = None
        self._lesson_tag = None
        self._lesson_type = None
        self._lesson_url = None
        self._version_no = None

    @property
    def deliver_end_time(self):
        return self._deliver_end_time

    @deliver_end_time.setter
    def deliver_end_time(self, value):
        self._deliver_end_time = value
    @property
    def deliver_start_time(self):
        return self._deliver_start_time

    @deliver_start_time.setter
    def deliver_start_time(self, value):
        self._deliver_start_time = value
    @property
    def lesson_calorie(self):
        return self._lesson_calorie

    @lesson_calorie.setter
    def lesson_calorie(self, value):
        self._lesson_calorie = value
    @property
    def lesson_charge_type(self):
        return self._lesson_charge_type

    @lesson_charge_type.setter
    def lesson_charge_type(self, value):
        self._lesson_charge_type = value
    @property
    def lesson_duration(self):
        return self._lesson_duration

    @lesson_duration.setter
    def lesson_duration(self, value):
        self._lesson_duration = value
    @property
    def lesson_ext_tag(self):
        return self._lesson_ext_tag

    @lesson_ext_tag.setter
    def lesson_ext_tag(self, value):
        if isinstance(value, list):
            self._lesson_ext_tag = list()
            for i in value:
                self._lesson_ext_tag.append(i)
    @property
    def lesson_image(self):
        return self._lesson_image

    @lesson_image.setter
    def lesson_image(self, value):
        self._lesson_image = value
    @property
    def lesson_intro(self):
        return self._lesson_intro

    @lesson_intro.setter
    def lesson_intro(self, value):
        self._lesson_intro = value
    @property
    def lesson_intro_image(self):
        return self._lesson_intro_image

    @lesson_intro_image.setter
    def lesson_intro_image(self, value):
        self._lesson_intro_image = value
    @property
    def lesson_limit_free_end_time(self):
        return self._lesson_limit_free_end_time

    @lesson_limit_free_end_time.setter
    def lesson_limit_free_end_time(self, value):
        self._lesson_limit_free_end_time = value
    @property
    def lesson_limit_free_start_time(self):
        return self._lesson_limit_free_start_time

    @lesson_limit_free_start_time.setter
    def lesson_limit_free_start_time(self, value):
        self._lesson_limit_free_start_time = value
    @property
    def lesson_name(self):
        return self._lesson_name

    @lesson_name.setter
    def lesson_name(self, value):
        self._lesson_name = value
    @property
    def lesson_out_id(self):
        return self._lesson_out_id

    @lesson_out_id.setter
    def lesson_out_id(self, value):
        self._lesson_out_id = value
    @property
    def lesson_source(self):
        return self._lesson_source

    @lesson_source.setter
    def lesson_source(self, value):
        self._lesson_source = value
    @property
    def lesson_tag(self):
        return self._lesson_tag

    @lesson_tag.setter
    def lesson_tag(self, value):
        if isinstance(value, list):
            self._lesson_tag = list()
            for i in value:
                self._lesson_tag.append(i)
    @property
    def lesson_type(self):
        return self._lesson_type

    @lesson_type.setter
    def lesson_type(self, value):
        self._lesson_type = value
    @property
    def lesson_url(self):
        return self._lesson_url

    @lesson_url.setter
    def lesson_url(self, value):
        self._lesson_url = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.deliver_end_time:
            if hasattr(self.deliver_end_time, 'to_alipay_dict'):
                params['deliver_end_time'] = self.deliver_end_time.to_alipay_dict()
            else:
                params['deliver_end_time'] = self.deliver_end_time
        if self.deliver_start_time:
            if hasattr(self.deliver_start_time, 'to_alipay_dict'):
                params['deliver_start_time'] = self.deliver_start_time.to_alipay_dict()
            else:
                params['deliver_start_time'] = self.deliver_start_time
        if self.lesson_calorie:
            if hasattr(self.lesson_calorie, 'to_alipay_dict'):
                params['lesson_calorie'] = self.lesson_calorie.to_alipay_dict()
            else:
                params['lesson_calorie'] = self.lesson_calorie
        if self.lesson_charge_type:
            if hasattr(self.lesson_charge_type, 'to_alipay_dict'):
                params['lesson_charge_type'] = self.lesson_charge_type.to_alipay_dict()
            else:
                params['lesson_charge_type'] = self.lesson_charge_type
        if self.lesson_duration:
            if hasattr(self.lesson_duration, 'to_alipay_dict'):
                params['lesson_duration'] = self.lesson_duration.to_alipay_dict()
            else:
                params['lesson_duration'] = self.lesson_duration
        if self.lesson_ext_tag:
            if isinstance(self.lesson_ext_tag, list):
                for i in range(0, len(self.lesson_ext_tag)):
                    element = self.lesson_ext_tag[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.lesson_ext_tag[i] = element.to_alipay_dict()
            if hasattr(self.lesson_ext_tag, 'to_alipay_dict'):
                params['lesson_ext_tag'] = self.lesson_ext_tag.to_alipay_dict()
            else:
                params['lesson_ext_tag'] = self.lesson_ext_tag
        if self.lesson_image:
            if hasattr(self.lesson_image, 'to_alipay_dict'):
                params['lesson_image'] = self.lesson_image.to_alipay_dict()
            else:
                params['lesson_image'] = self.lesson_image
        if self.lesson_intro:
            if hasattr(self.lesson_intro, 'to_alipay_dict'):
                params['lesson_intro'] = self.lesson_intro.to_alipay_dict()
            else:
                params['lesson_intro'] = self.lesson_intro
        if self.lesson_intro_image:
            if hasattr(self.lesson_intro_image, 'to_alipay_dict'):
                params['lesson_intro_image'] = self.lesson_intro_image.to_alipay_dict()
            else:
                params['lesson_intro_image'] = self.lesson_intro_image
        if self.lesson_limit_free_end_time:
            if hasattr(self.lesson_limit_free_end_time, 'to_alipay_dict'):
                params['lesson_limit_free_end_time'] = self.lesson_limit_free_end_time.to_alipay_dict()
            else:
                params['lesson_limit_free_end_time'] = self.lesson_limit_free_end_time
        if self.lesson_limit_free_start_time:
            if hasattr(self.lesson_limit_free_start_time, 'to_alipay_dict'):
                params['lesson_limit_free_start_time'] = self.lesson_limit_free_start_time.to_alipay_dict()
            else:
                params['lesson_limit_free_start_time'] = self.lesson_limit_free_start_time
        if self.lesson_name:
            if hasattr(self.lesson_name, 'to_alipay_dict'):
                params['lesson_name'] = self.lesson_name.to_alipay_dict()
            else:
                params['lesson_name'] = self.lesson_name
        if self.lesson_out_id:
            if hasattr(self.lesson_out_id, 'to_alipay_dict'):
                params['lesson_out_id'] = self.lesson_out_id.to_alipay_dict()
            else:
                params['lesson_out_id'] = self.lesson_out_id
        if self.lesson_source:
            if hasattr(self.lesson_source, 'to_alipay_dict'):
                params['lesson_source'] = self.lesson_source.to_alipay_dict()
            else:
                params['lesson_source'] = self.lesson_source
        if self.lesson_tag:
            if isinstance(self.lesson_tag, list):
                for i in range(0, len(self.lesson_tag)):
                    element = self.lesson_tag[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.lesson_tag[i] = element.to_alipay_dict()
            if hasattr(self.lesson_tag, 'to_alipay_dict'):
                params['lesson_tag'] = self.lesson_tag.to_alipay_dict()
            else:
                params['lesson_tag'] = self.lesson_tag
        if self.lesson_type:
            if hasattr(self.lesson_type, 'to_alipay_dict'):
                params['lesson_type'] = self.lesson_type.to_alipay_dict()
            else:
                params['lesson_type'] = self.lesson_type
        if self.lesson_url:
            if hasattr(self.lesson_url, 'to_alipay_dict'):
                params['lesson_url'] = self.lesson_url.to_alipay_dict()
            else:
                params['lesson_url'] = self.lesson_url
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsLessonBackstageSyncModel()
        if 'deliver_end_time' in d:
            o.deliver_end_time = d['deliver_end_time']
        if 'deliver_start_time' in d:
            o.deliver_start_time = d['deliver_start_time']
        if 'lesson_calorie' in d:
            o.lesson_calorie = d['lesson_calorie']
        if 'lesson_charge_type' in d:
            o.lesson_charge_type = d['lesson_charge_type']
        if 'lesson_duration' in d:
            o.lesson_duration = d['lesson_duration']
        if 'lesson_ext_tag' in d:
            o.lesson_ext_tag = d['lesson_ext_tag']
        if 'lesson_image' in d:
            o.lesson_image = d['lesson_image']
        if 'lesson_intro' in d:
            o.lesson_intro = d['lesson_intro']
        if 'lesson_intro_image' in d:
            o.lesson_intro_image = d['lesson_intro_image']
        if 'lesson_limit_free_end_time' in d:
            o.lesson_limit_free_end_time = d['lesson_limit_free_end_time']
        if 'lesson_limit_free_start_time' in d:
            o.lesson_limit_free_start_time = d['lesson_limit_free_start_time']
        if 'lesson_name' in d:
            o.lesson_name = d['lesson_name']
        if 'lesson_out_id' in d:
            o.lesson_out_id = d['lesson_out_id']
        if 'lesson_source' in d:
            o.lesson_source = d['lesson_source']
        if 'lesson_tag' in d:
            o.lesson_tag = d['lesson_tag']
        if 'lesson_type' in d:
            o.lesson_type = d['lesson_type']
        if 'lesson_url' in d:
            o.lesson_url = d['lesson_url']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o


