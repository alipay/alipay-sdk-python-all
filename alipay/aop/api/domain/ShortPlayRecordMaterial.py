#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShortPlayActor import ShortPlayActor


class ShortPlayRecordMaterial(object):

    def __init__(self):
        self._actor_list = None
        self._actor_salary_ratio = None
        self._animation_type = None
        self._audience = None
        self._avg_duration = None
        self._content_declared = None
        self._copyright_holder = None
        self._director = None
        self._first_broadcast = None
        self._main_actor_salary_ratio = None
        self._playlet_production_cost = None
        self._producer = None
        self._program_category = None
        self._screen_writer = None
        self._seqs_count = None
        self._summary = None

    @property
    def actor_list(self):
        return self._actor_list

    @actor_list.setter
    def actor_list(self, value):
        if isinstance(value, list):
            self._actor_list = list()
            for i in value:
                if isinstance(i, ShortPlayActor):
                    self._actor_list.append(i)
                else:
                    self._actor_list.append(ShortPlayActor.from_alipay_dict(i))
    @property
    def actor_salary_ratio(self):
        return self._actor_salary_ratio

    @actor_salary_ratio.setter
    def actor_salary_ratio(self, value):
        self._actor_salary_ratio = value
    @property
    def animation_type(self):
        return self._animation_type

    @animation_type.setter
    def animation_type(self, value):
        self._animation_type = value
    @property
    def audience(self):
        return self._audience

    @audience.setter
    def audience(self, value):
        if isinstance(value, list):
            self._audience = list()
            for i in value:
                self._audience.append(i)
    @property
    def avg_duration(self):
        return self._avg_duration

    @avg_duration.setter
    def avg_duration(self, value):
        self._avg_duration = value
    @property
    def content_declared(self):
        return self._content_declared

    @content_declared.setter
    def content_declared(self, value):
        self._content_declared = value
    @property
    def copyright_holder(self):
        return self._copyright_holder

    @copyright_holder.setter
    def copyright_holder(self, value):
        self._copyright_holder = value
    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        if isinstance(value, list):
            self._director = list()
            for i in value:
                self._director.append(i)
    @property
    def first_broadcast(self):
        return self._first_broadcast

    @first_broadcast.setter
    def first_broadcast(self, value):
        self._first_broadcast = value
    @property
    def main_actor_salary_ratio(self):
        return self._main_actor_salary_ratio

    @main_actor_salary_ratio.setter
    def main_actor_salary_ratio(self, value):
        self._main_actor_salary_ratio = value
    @property
    def playlet_production_cost(self):
        return self._playlet_production_cost

    @playlet_production_cost.setter
    def playlet_production_cost(self, value):
        self._playlet_production_cost = value
    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, value):
        self._producer = value
    @property
    def program_category(self):
        return self._program_category

    @program_category.setter
    def program_category(self, value):
        self._program_category = value
    @property
    def screen_writer(self):
        return self._screen_writer

    @screen_writer.setter
    def screen_writer(self, value):
        if isinstance(value, list):
            self._screen_writer = list()
            for i in value:
                self._screen_writer.append(i)
    @property
    def seqs_count(self):
        return self._seqs_count

    @seqs_count.setter
    def seqs_count(self, value):
        self._seqs_count = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value


    def to_alipay_dict(self):
        params = dict()
        if self.actor_list:
            if isinstance(self.actor_list, list):
                for i in range(0, len(self.actor_list)):
                    element = self.actor_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.actor_list[i] = element.to_alipay_dict()
            if hasattr(self.actor_list, 'to_alipay_dict'):
                params['actor_list'] = self.actor_list.to_alipay_dict()
            else:
                params['actor_list'] = self.actor_list
        if self.actor_salary_ratio:
            if hasattr(self.actor_salary_ratio, 'to_alipay_dict'):
                params['actor_salary_ratio'] = self.actor_salary_ratio.to_alipay_dict()
            else:
                params['actor_salary_ratio'] = self.actor_salary_ratio
        if self.animation_type:
            if hasattr(self.animation_type, 'to_alipay_dict'):
                params['animation_type'] = self.animation_type.to_alipay_dict()
            else:
                params['animation_type'] = self.animation_type
        if self.audience:
            if isinstance(self.audience, list):
                for i in range(0, len(self.audience)):
                    element = self.audience[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.audience[i] = element.to_alipay_dict()
            if hasattr(self.audience, 'to_alipay_dict'):
                params['audience'] = self.audience.to_alipay_dict()
            else:
                params['audience'] = self.audience
        if self.avg_duration:
            if hasattr(self.avg_duration, 'to_alipay_dict'):
                params['avg_duration'] = self.avg_duration.to_alipay_dict()
            else:
                params['avg_duration'] = self.avg_duration
        if self.content_declared:
            if hasattr(self.content_declared, 'to_alipay_dict'):
                params['content_declared'] = self.content_declared.to_alipay_dict()
            else:
                params['content_declared'] = self.content_declared
        if self.copyright_holder:
            if hasattr(self.copyright_holder, 'to_alipay_dict'):
                params['copyright_holder'] = self.copyright_holder.to_alipay_dict()
            else:
                params['copyright_holder'] = self.copyright_holder
        if self.director:
            if isinstance(self.director, list):
                for i in range(0, len(self.director)):
                    element = self.director[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.director[i] = element.to_alipay_dict()
            if hasattr(self.director, 'to_alipay_dict'):
                params['director'] = self.director.to_alipay_dict()
            else:
                params['director'] = self.director
        if self.first_broadcast:
            if hasattr(self.first_broadcast, 'to_alipay_dict'):
                params['first_broadcast'] = self.first_broadcast.to_alipay_dict()
            else:
                params['first_broadcast'] = self.first_broadcast
        if self.main_actor_salary_ratio:
            if hasattr(self.main_actor_salary_ratio, 'to_alipay_dict'):
                params['main_actor_salary_ratio'] = self.main_actor_salary_ratio.to_alipay_dict()
            else:
                params['main_actor_salary_ratio'] = self.main_actor_salary_ratio
        if self.playlet_production_cost:
            if hasattr(self.playlet_production_cost, 'to_alipay_dict'):
                params['playlet_production_cost'] = self.playlet_production_cost.to_alipay_dict()
            else:
                params['playlet_production_cost'] = self.playlet_production_cost
        if self.producer:
            if hasattr(self.producer, 'to_alipay_dict'):
                params['producer'] = self.producer.to_alipay_dict()
            else:
                params['producer'] = self.producer
        if self.program_category:
            if hasattr(self.program_category, 'to_alipay_dict'):
                params['program_category'] = self.program_category.to_alipay_dict()
            else:
                params['program_category'] = self.program_category
        if self.screen_writer:
            if isinstance(self.screen_writer, list):
                for i in range(0, len(self.screen_writer)):
                    element = self.screen_writer[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.screen_writer[i] = element.to_alipay_dict()
            if hasattr(self.screen_writer, 'to_alipay_dict'):
                params['screen_writer'] = self.screen_writer.to_alipay_dict()
            else:
                params['screen_writer'] = self.screen_writer
        if self.seqs_count:
            if hasattr(self.seqs_count, 'to_alipay_dict'):
                params['seqs_count'] = self.seqs_count.to_alipay_dict()
            else:
                params['seqs_count'] = self.seqs_count
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShortPlayRecordMaterial()
        if 'actor_list' in d:
            o.actor_list = d['actor_list']
        if 'actor_salary_ratio' in d:
            o.actor_salary_ratio = d['actor_salary_ratio']
        if 'animation_type' in d:
            o.animation_type = d['animation_type']
        if 'audience' in d:
            o.audience = d['audience']
        if 'avg_duration' in d:
            o.avg_duration = d['avg_duration']
        if 'content_declared' in d:
            o.content_declared = d['content_declared']
        if 'copyright_holder' in d:
            o.copyright_holder = d['copyright_holder']
        if 'director' in d:
            o.director = d['director']
        if 'first_broadcast' in d:
            o.first_broadcast = d['first_broadcast']
        if 'main_actor_salary_ratio' in d:
            o.main_actor_salary_ratio = d['main_actor_salary_ratio']
        if 'playlet_production_cost' in d:
            o.playlet_production_cost = d['playlet_production_cost']
        if 'producer' in d:
            o.producer = d['producer']
        if 'program_category' in d:
            o.program_category = d['program_category']
        if 'screen_writer' in d:
            o.screen_writer = d['screen_writer']
        if 'seqs_count' in d:
            o.seqs_count = d['seqs_count']
        if 'summary' in d:
            o.summary = d['summary']
        return o


