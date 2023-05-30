#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OnlineGameEventInfo import OnlineGameEventInfo


class OnlineGameInfo(object):

    def __init__(self):
        self._biz_type = None
        self._desc = None
        self._detail_url = None
        self._end_time = None
        self._env = None
        self._game_id = None
        self._game_progress_unit = None
        self._game_progress_value = None
        self._medal_image = None
        self._name = None
        self._online_game_event_list = None
        self._out_game_no = None
        self._poster_url = None
        self._sports_data_limit_count = None
        self._sports_data_source = None
        self._sports_data_type = None
        self._sports_type = None
        self._start_time = None
        self._status = None
        self._sub_biz_type = None
        self._tag_list = None
        self._user_join_end_time = None
        self._user_join_start_time = None

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
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
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
    def medal_image(self):
        return self._medal_image

    @medal_image.setter
    def medal_image(self, value):
        self._medal_image = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def online_game_event_list(self):
        return self._online_game_event_list

    @online_game_event_list.setter
    def online_game_event_list(self, value):
        if isinstance(value, list):
            self._online_game_event_list = list()
            for i in value:
                if isinstance(i, OnlineGameEventInfo):
                    self._online_game_event_list.append(i)
                else:
                    self._online_game_event_list.append(OnlineGameEventInfo.from_alipay_dict(i))
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
    def sports_type(self):
        return self._sports_type

    @sports_type.setter
    def sports_type(self, value):
        self._sports_type = value
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
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                self._tag_list.append(i)
    @property
    def user_join_end_time(self):
        return self._user_join_end_time

    @user_join_end_time.setter
    def user_join_end_time(self, value):
        self._user_join_end_time = value
    @property
    def user_join_start_time(self):
        return self._user_join_start_time

    @user_join_start_time.setter
    def user_join_start_time(self, value):
        self._user_join_start_time = value


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
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
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
        if self.medal_image:
            if hasattr(self.medal_image, 'to_alipay_dict'):
                params['medal_image'] = self.medal_image.to_alipay_dict()
            else:
                params['medal_image'] = self.medal_image
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.online_game_event_list:
            if isinstance(self.online_game_event_list, list):
                for i in range(0, len(self.online_game_event_list)):
                    element = self.online_game_event_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.online_game_event_list[i] = element.to_alipay_dict()
            if hasattr(self.online_game_event_list, 'to_alipay_dict'):
                params['online_game_event_list'] = self.online_game_event_list.to_alipay_dict()
            else:
                params['online_game_event_list'] = self.online_game_event_list
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
        if self.sports_type:
            if hasattr(self.sports_type, 'to_alipay_dict'):
                params['sports_type'] = self.sports_type.to_alipay_dict()
            else:
                params['sports_type'] = self.sports_type
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
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
        if self.user_join_end_time:
            if hasattr(self.user_join_end_time, 'to_alipay_dict'):
                params['user_join_end_time'] = self.user_join_end_time.to_alipay_dict()
            else:
                params['user_join_end_time'] = self.user_join_end_time
        if self.user_join_start_time:
            if hasattr(self.user_join_start_time, 'to_alipay_dict'):
                params['user_join_start_time'] = self.user_join_start_time.to_alipay_dict()
            else:
                params['user_join_start_time'] = self.user_join_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OnlineGameInfo()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'env' in d:
            o.env = d['env']
        if 'game_id' in d:
            o.game_id = d['game_id']
        if 'game_progress_unit' in d:
            o.game_progress_unit = d['game_progress_unit']
        if 'game_progress_value' in d:
            o.game_progress_value = d['game_progress_value']
        if 'medal_image' in d:
            o.medal_image = d['medal_image']
        if 'name' in d:
            o.name = d['name']
        if 'online_game_event_list' in d:
            o.online_game_event_list = d['online_game_event_list']
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
        if 'sports_type' in d:
            o.sports_type = d['sports_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        if 'user_join_end_time' in d:
            o.user_join_end_time = d['user_join_end_time']
        if 'user_join_start_time' in d:
            o.user_join_start_time = d['user_join_start_time']
        return o


