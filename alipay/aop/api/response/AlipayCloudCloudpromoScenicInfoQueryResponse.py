#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ScenicAudioCardDTO import ScenicAudioCardDTO
from alipay.aop.api.domain.MarkDTO import MarkDTO
from alipay.aop.api.domain.ScenicAllBaseDTO import ScenicAllBaseDTO
from alipay.aop.api.domain.SuggestScenicVO import SuggestScenicVO


class AlipayCloudCloudpromoScenicInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoScenicInfoQueryResponse, self).__init__()
        self._agent_id = None
        self._audio_card_vo = None
        self._cdn_video_url = None
        self._fun_exploration = None
        self._historical_curiosities = None
        self._mark_vo = None
        self._photo_suggest_image_list = None
        self._scene_id = None
        self._scenic_base_vo = None
        self._suggest_scenic_vos = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def audio_card_vo(self):
        return self._audio_card_vo

    @audio_card_vo.setter
    def audio_card_vo(self, value):
        if isinstance(value, ScenicAudioCardDTO):
            self._audio_card_vo = value
        else:
            self._audio_card_vo = ScenicAudioCardDTO.from_alipay_dict(value)
    @property
    def cdn_video_url(self):
        return self._cdn_video_url

    @cdn_video_url.setter
    def cdn_video_url(self, value):
        if isinstance(value, list):
            self._cdn_video_url = list()
            for i in value:
                self._cdn_video_url.append(i)
    @property
    def fun_exploration(self):
        return self._fun_exploration

    @fun_exploration.setter
    def fun_exploration(self, value):
        if isinstance(value, list):
            self._fun_exploration = list()
            for i in value:
                self._fun_exploration.append(i)
    @property
    def historical_curiosities(self):
        return self._historical_curiosities

    @historical_curiosities.setter
    def historical_curiosities(self, value):
        if isinstance(value, list):
            self._historical_curiosities = list()
            for i in value:
                self._historical_curiosities.append(i)
    @property
    def mark_vo(self):
        return self._mark_vo

    @mark_vo.setter
    def mark_vo(self, value):
        if isinstance(value, MarkDTO):
            self._mark_vo = value
        else:
            self._mark_vo = MarkDTO.from_alipay_dict(value)
    @property
    def photo_suggest_image_list(self):
        return self._photo_suggest_image_list

    @photo_suggest_image_list.setter
    def photo_suggest_image_list(self, value):
        if isinstance(value, list):
            self._photo_suggest_image_list = list()
            for i in value:
                self._photo_suggest_image_list.append(i)
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def scenic_base_vo(self):
        return self._scenic_base_vo

    @scenic_base_vo.setter
    def scenic_base_vo(self, value):
        if isinstance(value, ScenicAllBaseDTO):
            self._scenic_base_vo = value
        else:
            self._scenic_base_vo = ScenicAllBaseDTO.from_alipay_dict(value)
    @property
    def suggest_scenic_vos(self):
        return self._suggest_scenic_vos

    @suggest_scenic_vos.setter
    def suggest_scenic_vos(self, value):
        if isinstance(value, list):
            self._suggest_scenic_vos = list()
            for i in value:
                if isinstance(i, SuggestScenicVO):
                    self._suggest_scenic_vos.append(i)
                else:
                    self._suggest_scenic_vos.append(SuggestScenicVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoScenicInfoQueryResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'audio_card_vo' in response:
            self.audio_card_vo = response['audio_card_vo']
        if 'cdn_video_url' in response:
            self.cdn_video_url = response['cdn_video_url']
        if 'fun_exploration' in response:
            self.fun_exploration = response['fun_exploration']
        if 'historical_curiosities' in response:
            self.historical_curiosities = response['historical_curiosities']
        if 'mark_vo' in response:
            self.mark_vo = response['mark_vo']
        if 'photo_suggest_image_list' in response:
            self.photo_suggest_image_list = response['photo_suggest_image_list']
        if 'scene_id' in response:
            self.scene_id = response['scene_id']
        if 'scenic_base_vo' in response:
            self.scenic_base_vo = response['scenic_base_vo']
        if 'suggest_scenic_vos' in response:
            self.suggest_scenic_vos = response['suggest_scenic_vos']
