#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoRoutePolylineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoRoutePolylineQueryResponse, self).__init__()
        self._audio_text = None
        self._avatar = None
        self._comfort_level = None
        self._historical_curiosities = None
        self._introduction = None
        self._item_id = None
        self._latitude = None
        self._line_type = None
        self._longitude = None
        self._polyline = None
        self._tags = None
        self._title = None
        self._travel_distance = None
        self._travel_duration = None

    @property
    def audio_text(self):
        return self._audio_text

    @audio_text.setter
    def audio_text(self, value):
        self._audio_text = value
    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def comfort_level(self):
        return self._comfort_level

    @comfort_level.setter
    def comfort_level(self, value):
        self._comfort_level = value
    @property
    def historical_curiosities(self):
        return self._historical_curiosities

    @historical_curiosities.setter
    def historical_curiosities(self, value):
        self._historical_curiosities = value
    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def line_type(self):
        return self._line_type

    @line_type.setter
    def line_type(self, value):
        self._line_type = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def polyline(self):
        return self._polyline

    @polyline.setter
    def polyline(self, value):
        if isinstance(value, list):
            self._polyline = list()
            for i in value:
                self._polyline.append(i)
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def travel_distance(self):
        return self._travel_distance

    @travel_distance.setter
    def travel_distance(self, value):
        self._travel_distance = value
    @property
    def travel_duration(self):
        return self._travel_duration

    @travel_duration.setter
    def travel_duration(self, value):
        self._travel_duration = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoRoutePolylineQueryResponse, self).parse_response_content(response_content)
        if 'audio_text' in response:
            self.audio_text = response['audio_text']
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'comfort_level' in response:
            self.comfort_level = response['comfort_level']
        if 'historical_curiosities' in response:
            self.historical_curiosities = response['historical_curiosities']
        if 'introduction' in response:
            self.introduction = response['introduction']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'line_type' in response:
            self.line_type = response['line_type']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'polyline' in response:
            self.polyline = response['polyline']
        if 'tags' in response:
            self.tags = response['tags']
        if 'title' in response:
            self.title = response['title']
        if 'travel_distance' in response:
            self.travel_distance = response['travel_distance']
        if 'travel_duration' in response:
            self.travel_duration = response['travel_duration']
