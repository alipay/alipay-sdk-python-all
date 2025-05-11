#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthorizeLifeApp import AuthorizeLifeApp
from alipay.aop.api.domain.CopyrightMaterialFile import CopyrightMaterialFile
from alipay.aop.api.domain.ShortPlayFrameFile import ShortPlayFrameFile


class AlipaySecurityDataIprShortplayCreateModel(object):

    def __init__(self):
        self._actor_role = None
        self._art_video_type = None
        self._authorize_end_date = None
        self._authorize_life_app_list = None
        self._authorize_start_date = None
        self._channel = None
        self._content_summary = None
        self._copyright_material_file_list = None
        self._copyright_owner = None
        self._director = None
        self._episode_count = None
        self._external_short_play_id = None
        self._filing_no = None
        self._frame_file_list = None
        self._poster_file_id = None
        self._release_date = None
        self._release_flag = None
        self._self_made_flag = None
        self._short_play_name = None
        self._total_duration_minute = None
        self._urgent_flag = None

    @property
    def actor_role(self):
        return self._actor_role

    @actor_role.setter
    def actor_role(self, value):
        self._actor_role = value
    @property
    def art_video_type(self):
        return self._art_video_type

    @art_video_type.setter
    def art_video_type(self, value):
        self._art_video_type = value
    @property
    def authorize_end_date(self):
        return self._authorize_end_date

    @authorize_end_date.setter
    def authorize_end_date(self, value):
        self._authorize_end_date = value
    @property
    def authorize_life_app_list(self):
        return self._authorize_life_app_list

    @authorize_life_app_list.setter
    def authorize_life_app_list(self, value):
        if isinstance(value, list):
            self._authorize_life_app_list = list()
            for i in value:
                if isinstance(i, AuthorizeLifeApp):
                    self._authorize_life_app_list.append(i)
                else:
                    self._authorize_life_app_list.append(AuthorizeLifeApp.from_alipay_dict(i))
    @property
    def authorize_start_date(self):
        return self._authorize_start_date

    @authorize_start_date.setter
    def authorize_start_date(self, value):
        self._authorize_start_date = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def content_summary(self):
        return self._content_summary

    @content_summary.setter
    def content_summary(self, value):
        self._content_summary = value
    @property
    def copyright_material_file_list(self):
        return self._copyright_material_file_list

    @copyright_material_file_list.setter
    def copyright_material_file_list(self, value):
        if isinstance(value, list):
            self._copyright_material_file_list = list()
            for i in value:
                if isinstance(i, CopyrightMaterialFile):
                    self._copyright_material_file_list.append(i)
                else:
                    self._copyright_material_file_list.append(CopyrightMaterialFile.from_alipay_dict(i))
    @property
    def copyright_owner(self):
        return self._copyright_owner

    @copyright_owner.setter
    def copyright_owner(self, value):
        self._copyright_owner = value
    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        self._director = value
    @property
    def episode_count(self):
        return self._episode_count

    @episode_count.setter
    def episode_count(self, value):
        self._episode_count = value
    @property
    def external_short_play_id(self):
        return self._external_short_play_id

    @external_short_play_id.setter
    def external_short_play_id(self, value):
        self._external_short_play_id = value
    @property
    def filing_no(self):
        return self._filing_no

    @filing_no.setter
    def filing_no(self, value):
        self._filing_no = value
    @property
    def frame_file_list(self):
        return self._frame_file_list

    @frame_file_list.setter
    def frame_file_list(self, value):
        if isinstance(value, list):
            self._frame_file_list = list()
            for i in value:
                if isinstance(i, ShortPlayFrameFile):
                    self._frame_file_list.append(i)
                else:
                    self._frame_file_list.append(ShortPlayFrameFile.from_alipay_dict(i))
    @property
    def poster_file_id(self):
        return self._poster_file_id

    @poster_file_id.setter
    def poster_file_id(self, value):
        self._poster_file_id = value
    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        self._release_date = value
    @property
    def release_flag(self):
        return self._release_flag

    @release_flag.setter
    def release_flag(self, value):
        self._release_flag = value
    @property
    def self_made_flag(self):
        return self._self_made_flag

    @self_made_flag.setter
    def self_made_flag(self, value):
        self._self_made_flag = value
    @property
    def short_play_name(self):
        return self._short_play_name

    @short_play_name.setter
    def short_play_name(self, value):
        self._short_play_name = value
    @property
    def total_duration_minute(self):
        return self._total_duration_minute

    @total_duration_minute.setter
    def total_duration_minute(self, value):
        self._total_duration_minute = value
    @property
    def urgent_flag(self):
        return self._urgent_flag

    @urgent_flag.setter
    def urgent_flag(self, value):
        self._urgent_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.actor_role:
            if hasattr(self.actor_role, 'to_alipay_dict'):
                params['actor_role'] = self.actor_role.to_alipay_dict()
            else:
                params['actor_role'] = self.actor_role
        if self.art_video_type:
            if hasattr(self.art_video_type, 'to_alipay_dict'):
                params['art_video_type'] = self.art_video_type.to_alipay_dict()
            else:
                params['art_video_type'] = self.art_video_type
        if self.authorize_end_date:
            if hasattr(self.authorize_end_date, 'to_alipay_dict'):
                params['authorize_end_date'] = self.authorize_end_date.to_alipay_dict()
            else:
                params['authorize_end_date'] = self.authorize_end_date
        if self.authorize_life_app_list:
            if isinstance(self.authorize_life_app_list, list):
                for i in range(0, len(self.authorize_life_app_list)):
                    element = self.authorize_life_app_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authorize_life_app_list[i] = element.to_alipay_dict()
            if hasattr(self.authorize_life_app_list, 'to_alipay_dict'):
                params['authorize_life_app_list'] = self.authorize_life_app_list.to_alipay_dict()
            else:
                params['authorize_life_app_list'] = self.authorize_life_app_list
        if self.authorize_start_date:
            if hasattr(self.authorize_start_date, 'to_alipay_dict'):
                params['authorize_start_date'] = self.authorize_start_date.to_alipay_dict()
            else:
                params['authorize_start_date'] = self.authorize_start_date
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.content_summary:
            if hasattr(self.content_summary, 'to_alipay_dict'):
                params['content_summary'] = self.content_summary.to_alipay_dict()
            else:
                params['content_summary'] = self.content_summary
        if self.copyright_material_file_list:
            if isinstance(self.copyright_material_file_list, list):
                for i in range(0, len(self.copyright_material_file_list)):
                    element = self.copyright_material_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.copyright_material_file_list[i] = element.to_alipay_dict()
            if hasattr(self.copyright_material_file_list, 'to_alipay_dict'):
                params['copyright_material_file_list'] = self.copyright_material_file_list.to_alipay_dict()
            else:
                params['copyright_material_file_list'] = self.copyright_material_file_list
        if self.copyright_owner:
            if hasattr(self.copyright_owner, 'to_alipay_dict'):
                params['copyright_owner'] = self.copyright_owner.to_alipay_dict()
            else:
                params['copyright_owner'] = self.copyright_owner
        if self.director:
            if hasattr(self.director, 'to_alipay_dict'):
                params['director'] = self.director.to_alipay_dict()
            else:
                params['director'] = self.director
        if self.episode_count:
            if hasattr(self.episode_count, 'to_alipay_dict'):
                params['episode_count'] = self.episode_count.to_alipay_dict()
            else:
                params['episode_count'] = self.episode_count
        if self.external_short_play_id:
            if hasattr(self.external_short_play_id, 'to_alipay_dict'):
                params['external_short_play_id'] = self.external_short_play_id.to_alipay_dict()
            else:
                params['external_short_play_id'] = self.external_short_play_id
        if self.filing_no:
            if hasattr(self.filing_no, 'to_alipay_dict'):
                params['filing_no'] = self.filing_no.to_alipay_dict()
            else:
                params['filing_no'] = self.filing_no
        if self.frame_file_list:
            if isinstance(self.frame_file_list, list):
                for i in range(0, len(self.frame_file_list)):
                    element = self.frame_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.frame_file_list[i] = element.to_alipay_dict()
            if hasattr(self.frame_file_list, 'to_alipay_dict'):
                params['frame_file_list'] = self.frame_file_list.to_alipay_dict()
            else:
                params['frame_file_list'] = self.frame_file_list
        if self.poster_file_id:
            if hasattr(self.poster_file_id, 'to_alipay_dict'):
                params['poster_file_id'] = self.poster_file_id.to_alipay_dict()
            else:
                params['poster_file_id'] = self.poster_file_id
        if self.release_date:
            if hasattr(self.release_date, 'to_alipay_dict'):
                params['release_date'] = self.release_date.to_alipay_dict()
            else:
                params['release_date'] = self.release_date
        if self.release_flag:
            if hasattr(self.release_flag, 'to_alipay_dict'):
                params['release_flag'] = self.release_flag.to_alipay_dict()
            else:
                params['release_flag'] = self.release_flag
        if self.self_made_flag:
            if hasattr(self.self_made_flag, 'to_alipay_dict'):
                params['self_made_flag'] = self.self_made_flag.to_alipay_dict()
            else:
                params['self_made_flag'] = self.self_made_flag
        if self.short_play_name:
            if hasattr(self.short_play_name, 'to_alipay_dict'):
                params['short_play_name'] = self.short_play_name.to_alipay_dict()
            else:
                params['short_play_name'] = self.short_play_name
        if self.total_duration_minute:
            if hasattr(self.total_duration_minute, 'to_alipay_dict'):
                params['total_duration_minute'] = self.total_duration_minute.to_alipay_dict()
            else:
                params['total_duration_minute'] = self.total_duration_minute
        if self.urgent_flag:
            if hasattr(self.urgent_flag, 'to_alipay_dict'):
                params['urgent_flag'] = self.urgent_flag.to_alipay_dict()
            else:
                params['urgent_flag'] = self.urgent_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataIprShortplayCreateModel()
        if 'actor_role' in d:
            o.actor_role = d['actor_role']
        if 'art_video_type' in d:
            o.art_video_type = d['art_video_type']
        if 'authorize_end_date' in d:
            o.authorize_end_date = d['authorize_end_date']
        if 'authorize_life_app_list' in d:
            o.authorize_life_app_list = d['authorize_life_app_list']
        if 'authorize_start_date' in d:
            o.authorize_start_date = d['authorize_start_date']
        if 'channel' in d:
            o.channel = d['channel']
        if 'content_summary' in d:
            o.content_summary = d['content_summary']
        if 'copyright_material_file_list' in d:
            o.copyright_material_file_list = d['copyright_material_file_list']
        if 'copyright_owner' in d:
            o.copyright_owner = d['copyright_owner']
        if 'director' in d:
            o.director = d['director']
        if 'episode_count' in d:
            o.episode_count = d['episode_count']
        if 'external_short_play_id' in d:
            o.external_short_play_id = d['external_short_play_id']
        if 'filing_no' in d:
            o.filing_no = d['filing_no']
        if 'frame_file_list' in d:
            o.frame_file_list = d['frame_file_list']
        if 'poster_file_id' in d:
            o.poster_file_id = d['poster_file_id']
        if 'release_date' in d:
            o.release_date = d['release_date']
        if 'release_flag' in d:
            o.release_flag = d['release_flag']
        if 'self_made_flag' in d:
            o.self_made_flag = d['self_made_flag']
        if 'short_play_name' in d:
            o.short_play_name = d['short_play_name']
        if 'total_duration_minute' in d:
            o.total_duration_minute = d['total_duration_minute']
        if 'urgent_flag' in d:
            o.urgent_flag = d['urgent_flag']
        return o


