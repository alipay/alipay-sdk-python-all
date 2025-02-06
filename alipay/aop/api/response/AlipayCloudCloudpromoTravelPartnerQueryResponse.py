#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PoiInfoVo import PoiInfoVo
from alipay.aop.api.domain.PoiInfoVo import PoiInfoVo
from alipay.aop.api.domain.PoiInfoVo import PoiInfoVo
from alipay.aop.api.domain.PoiListDayVo import PoiListDayVo
from alipay.aop.api.domain.PoiInfoVo import PoiInfoVo


class AlipayCloudCloudpromoTravelPartnerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoTravelPartnerQueryResponse, self).__init__()
        self._assist_status = None
        self._attractions_count = None
        self._audio_poi_info = None
        self._calorie = None
        self._current_attraction_count = None
        self._current_distance = None
        self._current_duration = None
        self._current_poi_info = None
        self._distance = None
        self._duration = None
        self._finish_view = None
        self._introduction = None
        self._item_id = None
        self._need_poll = None
        self._next_poi_info = None
        self._next_poll_interval = None
        self._off_route = None
        self._poi_day_list = None
        self._poly_line_point = None
        self._polyline = None
        self._route_view_points = None
        self._start_point = None
        self._steps = None
        self._text = None
        self._title = None
        self._view_point = None
        self._view_point_image = None

    @property
    def assist_status(self):
        return self._assist_status

    @assist_status.setter
    def assist_status(self, value):
        self._assist_status = value
    @property
    def attractions_count(self):
        return self._attractions_count

    @attractions_count.setter
    def attractions_count(self, value):
        self._attractions_count = value
    @property
    def audio_poi_info(self):
        return self._audio_poi_info

    @audio_poi_info.setter
    def audio_poi_info(self, value):
        if isinstance(value, PoiInfoVo):
            self._audio_poi_info = value
        else:
            self._audio_poi_info = PoiInfoVo.from_alipay_dict(value)
    @property
    def calorie(self):
        return self._calorie

    @calorie.setter
    def calorie(self, value):
        self._calorie = value
    @property
    def current_attraction_count(self):
        return self._current_attraction_count

    @current_attraction_count.setter
    def current_attraction_count(self, value):
        self._current_attraction_count = value
    @property
    def current_distance(self):
        return self._current_distance

    @current_distance.setter
    def current_distance(self, value):
        self._current_distance = value
    @property
    def current_duration(self):
        return self._current_duration

    @current_duration.setter
    def current_duration(self, value):
        self._current_duration = value
    @property
    def current_poi_info(self):
        return self._current_poi_info

    @current_poi_info.setter
    def current_poi_info(self, value):
        if isinstance(value, PoiInfoVo):
            self._current_poi_info = value
        else:
            self._current_poi_info = PoiInfoVo.from_alipay_dict(value)
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
    def finish_view(self):
        return self._finish_view

    @finish_view.setter
    def finish_view(self, value):
        self._finish_view = value
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
    def need_poll(self):
        return self._need_poll

    @need_poll.setter
    def need_poll(self, value):
        self._need_poll = value
    @property
    def next_poi_info(self):
        return self._next_poi_info

    @next_poi_info.setter
    def next_poi_info(self, value):
        if isinstance(value, PoiInfoVo):
            self._next_poi_info = value
        else:
            self._next_poi_info = PoiInfoVo.from_alipay_dict(value)
    @property
    def next_poll_interval(self):
        return self._next_poll_interval

    @next_poll_interval.setter
    def next_poll_interval(self, value):
        self._next_poll_interval = value
    @property
    def off_route(self):
        return self._off_route

    @off_route.setter
    def off_route(self, value):
        self._off_route = value
    @property
    def poi_day_list(self):
        return self._poi_day_list

    @poi_day_list.setter
    def poi_day_list(self, value):
        if isinstance(value, list):
            self._poi_day_list = list()
            for i in value:
                if isinstance(i, PoiListDayVo):
                    self._poi_day_list.append(i)
                else:
                    self._poi_day_list.append(PoiListDayVo.from_alipay_dict(i))
    @property
    def poly_line_point(self):
        return self._poly_line_point

    @poly_line_point.setter
    def poly_line_point(self, value):
        self._poly_line_point = value
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
    def route_view_points(self):
        return self._route_view_points

    @route_view_points.setter
    def route_view_points(self, value):
        if isinstance(value, list):
            self._route_view_points = list()
            for i in value:
                self._route_view_points.append(i)
    @property
    def start_point(self):
        return self._start_point

    @start_point.setter
    def start_point(self, value):
        if isinstance(value, PoiInfoVo):
            self._start_point = value
        else:
            self._start_point = PoiInfoVo.from_alipay_dict(value)
    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):
        self._steps = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoTravelPartnerQueryResponse, self).parse_response_content(response_content)
        if 'assist_status' in response:
            self.assist_status = response['assist_status']
        if 'attractions_count' in response:
            self.attractions_count = response['attractions_count']
        if 'audio_poi_info' in response:
            self.audio_poi_info = response['audio_poi_info']
        if 'calorie' in response:
            self.calorie = response['calorie']
        if 'current_attraction_count' in response:
            self.current_attraction_count = response['current_attraction_count']
        if 'current_distance' in response:
            self.current_distance = response['current_distance']
        if 'current_duration' in response:
            self.current_duration = response['current_duration']
        if 'current_poi_info' in response:
            self.current_poi_info = response['current_poi_info']
        if 'distance' in response:
            self.distance = response['distance']
        if 'duration' in response:
            self.duration = response['duration']
        if 'finish_view' in response:
            self.finish_view = response['finish_view']
        if 'introduction' in response:
            self.introduction = response['introduction']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'need_poll' in response:
            self.need_poll = response['need_poll']
        if 'next_poi_info' in response:
            self.next_poi_info = response['next_poi_info']
        if 'next_poll_interval' in response:
            self.next_poll_interval = response['next_poll_interval']
        if 'off_route' in response:
            self.off_route = response['off_route']
        if 'poi_day_list' in response:
            self.poi_day_list = response['poi_day_list']
        if 'poly_line_point' in response:
            self.poly_line_point = response['poly_line_point']
        if 'polyline' in response:
            self.polyline = response['polyline']
        if 'route_view_points' in response:
            self.route_view_points = response['route_view_points']
        if 'start_point' in response:
            self.start_point = response['start_point']
        if 'steps' in response:
            self.steps = response['steps']
        if 'text' in response:
            self.text = response['text']
        if 'title' in response:
            self.title = response['title']
        if 'view_point' in response:
            self.view_point = response['view_point']
        if 'view_point_image' in response:
            self.view_point_image = response['view_point_image']
