#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsOnlinegameGameSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._desc = None
        self._end_time = None
        self._game_id = None
        self._game_progress_unit = None
        self._game_progress_value = None
        self._name = None
        self._out_game_no = None
        self._poster_url = None
        self._sports_data_limit_count = None
        self._sports_data_source = None
        self._sports_data_type = None
        self._start_time = None
        self._status = None
        self._sub_biz_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, value):
        self._game_id = value
    @property
    def game_progress_unit(self):
        return self._game_progress_unit

    @game_progress_unit.setter
    def game_progress_unit(self, value):
        self._game_progress_unit = value
    @property
    def game_progress_value(self):
        return self._game_progress_value

    @game_progress_value.setter
    def game_progress_value(self, value):
        self._game_progress_value = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_game_no(self):
        return self._out_game_no

    @out_game_no.setter
    def out_game_no(self, value):
        self._out_game_no = value
    @property
    def poster_url(self):
        return self._poster_url

    @poster_url.setter
    def poster_url(self, value):
        self._poster_url = value
    @property
    def sports_data_limit_count(self):
        return self._sports_data_limit_count

    @sports_data_limit_count.setter
    def sports_data_limit_count(self, value):
        self._sports_data_limit_count = value
    @property
    def sports_data_source(self):
        return self._sports_data_source

    @sports_data_source.setter
    def sports_data_source(self, value):
        self._sports_data_source = value
    @property
    def sports_data_type(self):
        return self._sports_data_type

    @sports_data_type.setter
    def sports_data_type(self, value):
        self._sports_data_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.game_id:
            if hasattr(self.game_id, 'to_alipay_dict'):
                params['game_id'] = self.game_id.to_alipay_dict()
            else:
                params['game_id'] = self.game_id
        if self.game_progress_unit:
            if hasattr(self.game_progress_unit, 'to_alipay_dict'):
                params['game_progress_unit'] = self.game_progress_unit.to_alipay_dict()
            else:
                params['game_progress_unit'] = self.game_progress_unit
        if self.game_progress_value:
            if hasattr(self.game_progress_value, 'to_alipay_dict'):
                params['game_progress_value'] = self.game_progress_value.to_alipay_dict()
            else:
                params['game_progress_value'] = self.game_progress_value
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_game_no:
            if hasattr(self.out_game_no, 'to_alipay_dict'):
                params['out_game_no'] = self.out_game_no.to_alipay_dict()
            else:
                params['out_game_no'] = self.out_game_no
        if self.poster_url:
            if hasattr(self.poster_url, 'to_alipay_dict'):
                params['poster_url'] = self.poster_url.to_alipay_dict()
            else:
                params['poster_url'] = self.poster_url
        if self.sports_data_limit_count:
            if hasattr(self.sports_data_limit_count, 'to_alipay_dict'):
                params['sports_data_limit_count'] = self.sports_data_limit_count.to_alipay_dict()
            else:
                params['sports_data_limit_count'] = self.sports_data_limit_count
        if self.sports_data_source:
            if hasattr(self.sports_data_source, 'to_alipay_dict'):
                params['sports_data_source'] = self.sports_data_source.to_alipay_dict()
            else:
                params['sports_data_source'] = self.sports_data_source
        if self.sports_data_type:
            if hasattr(self.sports_data_type, 'to_alipay_dict'):
                params['sports_data_type'] = self.sports_data_type.to_alipay_dict()
            else:
                params['sports_data_type'] = self.sports_data_type
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsOnlinegameGameSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'game_id' in d:
            o.game_id = d['game_id']
        if 'game_progress_unit' in d:
            o.game_progress_unit = d['game_progress_unit']
        if 'game_progress_value' in d:
            o.game_progress_value = d['game_progress_value']
        if 'name' in d:
            o.name = d['name']
        if 'out_game_no' in d:
            o.out_game_no = d['out_game_no']
        if 'poster_url' in d:
            o.poster_url = d['poster_url']
        if 'sports_data_limit_count' in d:
            o.sports_data_limit_count = d['sports_data_limit_count']
        if 'sports_data_source' in d:
            o.sports_data_source = d['sports_data_source']
        if 'sports_data_type' in d:
            o.sports_data_type = d['sports_data_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


