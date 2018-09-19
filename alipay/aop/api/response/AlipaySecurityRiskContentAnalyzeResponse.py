#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InfoSecHitDetectItem import InfoSecHitDetectItem


class AlipaySecurityRiskContentAnalyzeResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskContentAnalyzeResponse, self).__init__()
        self._app_scene_data_id = None
        self._event_id = None
        self._hit_detect_items = None
        self._need_query = None
        self._result_action = None

    @property
    def app_scene_data_id(self):
        return self._app_scene_data_id

    @app_scene_data_id.setter
    def app_scene_data_id(self, value):
        self._app_scene_data_id = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def hit_detect_items(self):
        return self._hit_detect_items

    @hit_detect_items.setter
    def hit_detect_items(self, value):
        if isinstance(value, list):
            self._hit_detect_items = list()
            for i in value:
                if isinstance(i, InfoSecHitDetectItem):
                    self._hit_detect_items.append(i)
                else:
                    self._hit_detect_items.append(InfoSecHitDetectItem.from_alipay_dict(i))
    @property
    def need_query(self):
        return self._need_query

    @need_query.setter
    def need_query(self, value):
        self._need_query = value
    @property
    def result_action(self):
        return self._result_action

    @result_action.setter
    def result_action(self, value):
        self._result_action = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskContentAnalyzeResponse, self).parse_response_content(response_content)
        if 'app_scene_data_id' in response:
            self.app_scene_data_id = response['app_scene_data_id']
        if 'event_id' in response:
            self.event_id = response['event_id']
        if 'hit_detect_items' in response:
            self.hit_detect_items = response['hit_detect_items']
        if 'need_query' in response:
            self.need_query = response['need_query']
        if 'result_action' in response:
            self.result_action = response['result_action']
