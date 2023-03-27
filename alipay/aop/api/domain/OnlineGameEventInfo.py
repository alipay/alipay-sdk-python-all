#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OnlineGameEventInfo(object):

    def __init__(self):
        self._content = None
        self._game_event_id = None
        self._out_game_event_no = None
        self._progress_unit = None
        self._progress_value = None
        self._status = None
        self._title = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def game_event_id(self):
        return self._game_event_id

    @game_event_id.setter
    def game_event_id(self, value):
        self._game_event_id = value
    @property
    def out_game_event_no(self):
        return self._out_game_event_no

    @out_game_event_no.setter
    def out_game_event_no(self, value):
        self._out_game_event_no = value
    @property
    def progress_unit(self):
        return self._progress_unit

    @progress_unit.setter
    def progress_unit(self, value):
        self._progress_unit = value
    @property
    def progress_value(self):
        return self._progress_value

    @progress_value.setter
    def progress_value(self, value):
        self._progress_value = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.game_event_id:
            if hasattr(self.game_event_id, 'to_alipay_dict'):
                params['game_event_id'] = self.game_event_id.to_alipay_dict()
            else:
                params['game_event_id'] = self.game_event_id
        if self.out_game_event_no:
            if hasattr(self.out_game_event_no, 'to_alipay_dict'):
                params['out_game_event_no'] = self.out_game_event_no.to_alipay_dict()
            else:
                params['out_game_event_no'] = self.out_game_event_no
        if self.progress_unit:
            if hasattr(self.progress_unit, 'to_alipay_dict'):
                params['progress_unit'] = self.progress_unit.to_alipay_dict()
            else:
                params['progress_unit'] = self.progress_unit
        if self.progress_value:
            if hasattr(self.progress_value, 'to_alipay_dict'):
                params['progress_value'] = self.progress_value.to_alipay_dict()
            else:
                params['progress_value'] = self.progress_value
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OnlineGameEventInfo()
        if 'content' in d:
            o.content = d['content']
        if 'game_event_id' in d:
            o.game_event_id = d['game_event_id']
        if 'out_game_event_no' in d:
            o.out_game_event_no = d['out_game_event_no']
        if 'progress_unit' in d:
            o.progress_unit = d['progress_unit']
        if 'progress_value' in d:
            o.progress_value = d['progress_value']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        return o


