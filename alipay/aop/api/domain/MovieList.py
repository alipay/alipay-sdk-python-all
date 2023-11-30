#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MovieList(object):

    def __init__(self):
        self._cast = None
        self._copy_types = None
        self._cover = None
        self._director = None
        self._duration = None
        self._film_code = None
        self._film_name = None
        self._id = None
        self._is_booking = None
        self._language = None
        self._plan_count = None
        self._publish_date = None
        self._simple_word = None
        self._type = None

    @property
    def cast(self):
        return self._cast

    @cast.setter
    def cast(self, value):
        self._cast = value
    @property
    def copy_types(self):
        return self._copy_types

    @copy_types.setter
    def copy_types(self, value):
        self._copy_types = value
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        self._director = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def film_code(self):
        return self._film_code

    @film_code.setter
    def film_code(self, value):
        self._film_code = value
    @property
    def film_name(self):
        return self._film_name

    @film_name.setter
    def film_name(self, value):
        self._film_name = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_booking(self):
        return self._is_booking

    @is_booking.setter
    def is_booking(self, value):
        self._is_booking = value
    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
    @property
    def plan_count(self):
        return self._plan_count

    @plan_count.setter
    def plan_count(self, value):
        self._plan_count = value
    @property
    def publish_date(self):
        return self._publish_date

    @publish_date.setter
    def publish_date(self, value):
        self._publish_date = value
    @property
    def simple_word(self):
        return self._simple_word

    @simple_word.setter
    def simple_word(self, value):
        self._simple_word = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cast:
            if hasattr(self.cast, 'to_alipay_dict'):
                params['cast'] = self.cast.to_alipay_dict()
            else:
                params['cast'] = self.cast
        if self.copy_types:
            if hasattr(self.copy_types, 'to_alipay_dict'):
                params['copy_types'] = self.copy_types.to_alipay_dict()
            else:
                params['copy_types'] = self.copy_types
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.director:
            if hasattr(self.director, 'to_alipay_dict'):
                params['director'] = self.director.to_alipay_dict()
            else:
                params['director'] = self.director
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.film_code:
            if hasattr(self.film_code, 'to_alipay_dict'):
                params['film_code'] = self.film_code.to_alipay_dict()
            else:
                params['film_code'] = self.film_code
        if self.film_name:
            if hasattr(self.film_name, 'to_alipay_dict'):
                params['film_name'] = self.film_name.to_alipay_dict()
            else:
                params['film_name'] = self.film_name
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_booking:
            if hasattr(self.is_booking, 'to_alipay_dict'):
                params['is_booking'] = self.is_booking.to_alipay_dict()
            else:
                params['is_booking'] = self.is_booking
        if self.language:
            if hasattr(self.language, 'to_alipay_dict'):
                params['language'] = self.language.to_alipay_dict()
            else:
                params['language'] = self.language
        if self.plan_count:
            if hasattr(self.plan_count, 'to_alipay_dict'):
                params['plan_count'] = self.plan_count.to_alipay_dict()
            else:
                params['plan_count'] = self.plan_count
        if self.publish_date:
            if hasattr(self.publish_date, 'to_alipay_dict'):
                params['publish_date'] = self.publish_date.to_alipay_dict()
            else:
                params['publish_date'] = self.publish_date
        if self.simple_word:
            if hasattr(self.simple_word, 'to_alipay_dict'):
                params['simple_word'] = self.simple_word.to_alipay_dict()
            else:
                params['simple_word'] = self.simple_word
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MovieList()
        if 'cast' in d:
            o.cast = d['cast']
        if 'copy_types' in d:
            o.copy_types = d['copy_types']
        if 'cover' in d:
            o.cover = d['cover']
        if 'director' in d:
            o.director = d['director']
        if 'duration' in d:
            o.duration = d['duration']
        if 'film_code' in d:
            o.film_code = d['film_code']
        if 'film_name' in d:
            o.film_name = d['film_name']
        if 'id' in d:
            o.id = d['id']
        if 'is_booking' in d:
            o.is_booking = d['is_booking']
        if 'language' in d:
            o.language = d['language']
        if 'plan_count' in d:
            o.plan_count = d['plan_count']
        if 'publish_date' in d:
            o.publish_date = d['publish_date']
        if 'simple_word' in d:
            o.simple_word = d['simple_word']
        if 'type' in d:
            o.type = d['type']
        return o


