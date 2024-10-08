#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RouteInfo(object):

    def __init__(self):
        self._attractions_count = None
        self._distance = None
        self._duration = None
        self._route_id = None
        self._route_type = None
        self._title = None
        self._view_point = None
        self._view_point_image = None

    @property
    def attractions_count(self):
        return self._attractions_count

    @attractions_count.setter
    def attractions_count(self, value):
        self._attractions_count = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def route_id(self):
        return self._route_id

    @route_id.setter
    def route_id(self, value):
        self._route_id = value
    @property
    def route_type(self):
        return self._route_type

    @route_type.setter
    def route_type(self, value):
        self._route_type = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def view_point(self):
        return self._view_point

    @view_point.setter
    def view_point(self, value):
        if isinstance(value, list):
            self._view_point = list()
            for i in value:
                self._view_point.append(i)
    @property
    def view_point_image(self):
        return self._view_point_image

    @view_point_image.setter
    def view_point_image(self, value):
        self._view_point_image = value


    def to_alipay_dict(self):
        params = dict()
        if self.attractions_count:
            if hasattr(self.attractions_count, 'to_alipay_dict'):
                params['attractions_count'] = self.attractions_count.to_alipay_dict()
            else:
                params['attractions_count'] = self.attractions_count
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.route_id:
            if hasattr(self.route_id, 'to_alipay_dict'):
                params['route_id'] = self.route_id.to_alipay_dict()
            else:
                params['route_id'] = self.route_id
        if self.route_type:
            if hasattr(self.route_type, 'to_alipay_dict'):
                params['route_type'] = self.route_type.to_alipay_dict()
            else:
                params['route_type'] = self.route_type
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.view_point:
            if isinstance(self.view_point, list):
                for i in range(0, len(self.view_point)):
                    element = self.view_point[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.view_point[i] = element.to_alipay_dict()
            if hasattr(self.view_point, 'to_alipay_dict'):
                params['view_point'] = self.view_point.to_alipay_dict()
            else:
                params['view_point'] = self.view_point
        if self.view_point_image:
            if hasattr(self.view_point_image, 'to_alipay_dict'):
                params['view_point_image'] = self.view_point_image.to_alipay_dict()
            else:
                params['view_point_image'] = self.view_point_image
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RouteInfo()
        if 'attractions_count' in d:
            o.attractions_count = d['attractions_count']
        if 'distance' in d:
            o.distance = d['distance']
        if 'duration' in d:
            o.duration = d['duration']
        if 'route_id' in d:
            o.route_id = d['route_id']
        if 'route_type' in d:
            o.route_type = d['route_type']
        if 'title' in d:
            o.title = d['title']
        if 'view_point' in d:
            o.view_point = d['view_point']
        if 'view_point_image' in d:
            o.view_point_image = d['view_point_image']
        return o


