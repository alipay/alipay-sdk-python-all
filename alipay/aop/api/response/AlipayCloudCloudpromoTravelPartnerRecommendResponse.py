#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PoiInfoVo import PoiInfoVo
from alipay.aop.api.domain.PoiInfoVo import PoiInfoVo
from alipay.aop.api.domain.PoiInfoVo import PoiInfoVo


class AlipayCloudCloudpromoTravelPartnerRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoTravelPartnerRecommendResponse, self).__init__()
        self._agent_id = None
        self._assist_status = None
        self._comfort_level = None
        self._current_attraction_count = None
        self._current_distance = None
        self._current_duration = None
        self._current_poi_info = None
        self._if_aoi_range = None
        self._item_id = None
        self._nearby_poi_list = None
        self._need_poll = None
        self._next_nearest_poi_list = None
        self._polyline = None
        self._text = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def assist_status(self):
        return self._assist_status

    @assist_status.setter
    def assist_status(self, value):
        self._assist_status = value
    @property
    def comfort_level(self):
        return self._comfort_level

    @comfort_level.setter
    def comfort_level(self, value):
        self._comfort_level = value
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
    def if_aoi_range(self):
        return self._if_aoi_range

    @if_aoi_range.setter
    def if_aoi_range(self, value):
        self._if_aoi_range = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def nearby_poi_list(self):
        return self._nearby_poi_list

    @nearby_poi_list.setter
    def nearby_poi_list(self, value):
        if isinstance(value, list):
            self._nearby_poi_list = list()
            for i in value:
                if isinstance(i, PoiInfoVo):
                    self._nearby_poi_list.append(i)
                else:
                    self._nearby_poi_list.append(PoiInfoVo.from_alipay_dict(i))
    @property
    def need_poll(self):
        return self._need_poll

    @need_poll.setter
    def need_poll(self, value):
        self._need_poll = value
    @property
    def next_nearest_poi_list(self):
        return self._next_nearest_poi_list

    @next_nearest_poi_list.setter
    def next_nearest_poi_list(self, value):
        if isinstance(value, list):
            self._next_nearest_poi_list = list()
            for i in value:
                if isinstance(i, PoiInfoVo):
                    self._next_nearest_poi_list.append(i)
                else:
                    self._next_nearest_poi_list.append(PoiInfoVo.from_alipay_dict(i))
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
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoTravelPartnerRecommendResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'assist_status' in response:
            self.assist_status = response['assist_status']
        if 'comfort_level' in response:
            self.comfort_level = response['comfort_level']
        if 'current_attraction_count' in response:
            self.current_attraction_count = response['current_attraction_count']
        if 'current_distance' in response:
            self.current_distance = response['current_distance']
        if 'current_duration' in response:
            self.current_duration = response['current_duration']
        if 'current_poi_info' in response:
            self.current_poi_info = response['current_poi_info']
        if 'if_aoi_range' in response:
            self.if_aoi_range = response['if_aoi_range']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'nearby_poi_list' in response:
            self.nearby_poi_list = response['nearby_poi_list']
        if 'need_poll' in response:
            self.need_poll = response['need_poll']
        if 'next_nearest_poi_list' in response:
            self.next_nearest_poi_list = response['next_nearest_poi_list']
        if 'polyline' in response:
            self.polyline = response['polyline']
        if 'text' in response:
            self.text = response['text']
