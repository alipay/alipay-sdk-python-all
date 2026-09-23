#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShortPlayChannelInfo import ShortPlayChannelInfo
from alipay.aop.api.domain.ShortPlayCopyrightMaterial import ShortPlayCopyrightMaterial
from alipay.aop.api.domain.ShortPlayEpisodeInfo import ShortPlayEpisodeInfo
from alipay.aop.api.domain.ShortPlayRecordMaterial import ShortPlayRecordMaterial


class AlipaySocialBaseLifecreationShortplaydetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseLifecreationShortplaydetailQueryResponse, self).__init__()
        self._album_id = None
        self._broadcast_record_number = None
        self._channel_status = None
        self._copyright_material = None
        self._cover = None
        self._create_time = None
        self._episode_info_list = None
        self._record_material = None
        self._tag_list = None
        self._title = None
        self._update_time = None

    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
    @property
    def broadcast_record_number(self):
        return self._broadcast_record_number

    @broadcast_record_number.setter
    def broadcast_record_number(self, value):
        self._broadcast_record_number = value
    @property
    def channel_status(self):
        return self._channel_status

    @channel_status.setter
    def channel_status(self, value):
        if isinstance(value, list):
            self._channel_status = list()
            for i in value:
                if isinstance(i, ShortPlayChannelInfo):
                    self._channel_status.append(i)
                else:
                    self._channel_status.append(ShortPlayChannelInfo.from_alipay_dict(i))
    @property
    def copyright_material(self):
        return self._copyright_material

    @copyright_material.setter
    def copyright_material(self, value):
        if isinstance(value, ShortPlayCopyrightMaterial):
            self._copyright_material = value
        else:
            self._copyright_material = ShortPlayCopyrightMaterial.from_alipay_dict(value)
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def episode_info_list(self):
        return self._episode_info_list

    @episode_info_list.setter
    def episode_info_list(self, value):
        if isinstance(value, list):
            self._episode_info_list = list()
            for i in value:
                if isinstance(i, ShortPlayEpisodeInfo):
                    self._episode_info_list.append(i)
                else:
                    self._episode_info_list.append(ShortPlayEpisodeInfo.from_alipay_dict(i))
    @property
    def record_material(self):
        return self._record_material

    @record_material.setter
    def record_material(self, value):
        if isinstance(value, ShortPlayRecordMaterial):
            self._record_material = value
        else:
            self._record_material = ShortPlayRecordMaterial.from_alipay_dict(value)
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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseLifecreationShortplaydetailQueryResponse, self).parse_response_content(response_content)
        if 'album_id' in response:
            self.album_id = response['album_id']
        if 'broadcast_record_number' in response:
            self.broadcast_record_number = response['broadcast_record_number']
        if 'channel_status' in response:
            self.channel_status = response['channel_status']
        if 'copyright_material' in response:
            self.copyright_material = response['copyright_material']
        if 'cover' in response:
            self.cover = response['cover']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'episode_info_list' in response:
            self.episode_info_list = response['episode_info_list']
        if 'record_material' in response:
            self.record_material = response['record_material']
        if 'tag_list' in response:
            self.tag_list = response['tag_list']
        if 'title' in response:
            self.title = response['title']
        if 'update_time' in response:
            self.update_time = response['update_time']
