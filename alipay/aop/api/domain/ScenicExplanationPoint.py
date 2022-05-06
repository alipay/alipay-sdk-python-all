#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenicExplanationPoint(object):

    def __init__(self):
        self._duration = None
        self._explainer = None
        self._explainer_points = None
        self._latitude = None
        self._longitude = None
        self._point_id = None
        self._point_name = None
        self._price = None
        self._story = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def explainer(self):
        return self._explainer

    @explainer.setter
    def explainer(self, value):
        self._explainer = value
    @property
    def explainer_points(self):
        return self._explainer_points

    @explainer_points.setter
    def explainer_points(self, value):
        if isinstance(value, list):
            self._explainer_points = list()
            for i in value:
                self._explainer_points.append(i)
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def point_id(self):
        return self._point_id

    @point_id.setter
    def point_id(self, value):
        self._point_id = value
    @property
    def point_name(self):
        return self._point_name

    @point_name.setter
    def point_name(self, value):
        self._point_name = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def story(self):
        return self._story

    @story.setter
    def story(self, value):
        self._story = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.explainer:
            if hasattr(self.explainer, 'to_alipay_dict'):
                params['explainer'] = self.explainer.to_alipay_dict()
            else:
                params['explainer'] = self.explainer
        if self.explainer_points:
            if isinstance(self.explainer_points, list):
                for i in range(0, len(self.explainer_points)):
                    element = self.explainer_points[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.explainer_points[i] = element.to_alipay_dict()
            if hasattr(self.explainer_points, 'to_alipay_dict'):
                params['explainer_points'] = self.explainer_points.to_alipay_dict()
            else:
                params['explainer_points'] = self.explainer_points
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.point_id:
            if hasattr(self.point_id, 'to_alipay_dict'):
                params['point_id'] = self.point_id.to_alipay_dict()
            else:
                params['point_id'] = self.point_id
        if self.point_name:
            if hasattr(self.point_name, 'to_alipay_dict'):
                params['point_name'] = self.point_name.to_alipay_dict()
            else:
                params['point_name'] = self.point_name
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.story:
            if hasattr(self.story, 'to_alipay_dict'):
                params['story'] = self.story.to_alipay_dict()
            else:
                params['story'] = self.story
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenicExplanationPoint()
        if 'duration' in d:
            o.duration = d['duration']
        if 'explainer' in d:
            o.explainer = d['explainer']
        if 'explainer_points' in d:
            o.explainer_points = d['explainer_points']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'point_id' in d:
            o.point_id = d['point_id']
        if 'point_name' in d:
            o.point_name = d['point_name']
        if 'price' in d:
            o.price = d['price']
        if 'story' in d:
            o.story = d['story']
        return o


