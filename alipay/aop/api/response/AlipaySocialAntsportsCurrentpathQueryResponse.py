#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntsportsCurrentpathQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntsportsCurrentpathQueryResponse, self).__init__()
        self._exercise_consume_step_count = None
        self._exercise_produce_step_count = None
        self._forward_step_count = None
        self._min_go_steps = None
        self._next_unlock_path_id = None
        self._path_complete_status = None
        self._path_id = None
        self._path_join_status = None
        self._path_name = None
        self._path_record_id = None
        self._path_scene = None
        self._path_station_code = None
        self._path_station_name = None

    @property
    def exercise_consume_step_count(self):
        return self._exercise_consume_step_count

    @exercise_consume_step_count.setter
    def exercise_consume_step_count(self, value):
        self._exercise_consume_step_count = value
    @property
    def exercise_produce_step_count(self):
        return self._exercise_produce_step_count

    @exercise_produce_step_count.setter
    def exercise_produce_step_count(self, value):
        self._exercise_produce_step_count = value
    @property
    def forward_step_count(self):
        return self._forward_step_count

    @forward_step_count.setter
    def forward_step_count(self, value):
        self._forward_step_count = value
    @property
    def min_go_steps(self):
        return self._min_go_steps

    @min_go_steps.setter
    def min_go_steps(self, value):
        self._min_go_steps = value
    @property
    def next_unlock_path_id(self):
        return self._next_unlock_path_id

    @next_unlock_path_id.setter
    def next_unlock_path_id(self, value):
        self._next_unlock_path_id = value
    @property
    def path_complete_status(self):
        return self._path_complete_status

    @path_complete_status.setter
    def path_complete_status(self, value):
        self._path_complete_status = value
    @property
    def path_id(self):
        return self._path_id

    @path_id.setter
    def path_id(self, value):
        self._path_id = value
    @property
    def path_join_status(self):
        return self._path_join_status

    @path_join_status.setter
    def path_join_status(self, value):
        self._path_join_status = value
    @property
    def path_name(self):
        return self._path_name

    @path_name.setter
    def path_name(self, value):
        self._path_name = value
    @property
    def path_record_id(self):
        return self._path_record_id

    @path_record_id.setter
    def path_record_id(self, value):
        self._path_record_id = value
    @property
    def path_scene(self):
        return self._path_scene

    @path_scene.setter
    def path_scene(self, value):
        self._path_scene = value
    @property
    def path_station_code(self):
        return self._path_station_code

    @path_station_code.setter
    def path_station_code(self, value):
        self._path_station_code = value
    @property
    def path_station_name(self):
        return self._path_station_name

    @path_station_name.setter
    def path_station_name(self, value):
        self._path_station_name = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntsportsCurrentpathQueryResponse, self).parse_response_content(response_content)
        if 'exercise_consume_step_count' in response:
            self.exercise_consume_step_count = response['exercise_consume_step_count']
        if 'exercise_produce_step_count' in response:
            self.exercise_produce_step_count = response['exercise_produce_step_count']
        if 'forward_step_count' in response:
            self.forward_step_count = response['forward_step_count']
        if 'min_go_steps' in response:
            self.min_go_steps = response['min_go_steps']
        if 'next_unlock_path_id' in response:
            self.next_unlock_path_id = response['next_unlock_path_id']
        if 'path_complete_status' in response:
            self.path_complete_status = response['path_complete_status']
        if 'path_id' in response:
            self.path_id = response['path_id']
        if 'path_join_status' in response:
            self.path_join_status = response['path_join_status']
        if 'path_name' in response:
            self.path_name = response['path_name']
        if 'path_record_id' in response:
            self.path_record_id = response['path_record_id']
        if 'path_scene' in response:
            self.path_scene = response['path_scene']
        if 'path_station_code' in response:
            self.path_station_code = response['path_station_code']
        if 'path_station_name' in response:
            self.path_station_name = response['path_station_name']
