#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LandingTypeDto import LandingTypeDto
from alipay.aop.api.domain.VideoInfo import VideoInfo


class AlipayDataDataserviceProductLandinginfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceProductLandinginfoQueryResponse, self).__init__()
        self._item_id = None
        self._landing = None
        self._out_item_id = None
        self._video_info_list = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def landing(self):
        return self._landing

    @landing.setter
    def landing(self, value):
        if isinstance(value, LandingTypeDto):
            self._landing = value
        else:
            self._landing = LandingTypeDto.from_alipay_dict(value)
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def video_info_list(self):
        return self._video_info_list

    @video_info_list.setter
    def video_info_list(self, value):
        if isinstance(value, list):
            self._video_info_list = list()
            for i in value:
                if isinstance(i, VideoInfo):
                    self._video_info_list.append(i)
                else:
                    self._video_info_list.append(VideoInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceProductLandinginfoQueryResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'landing' in response:
            self.landing = response['landing']
        if 'out_item_id' in response:
            self.out_item_id = response['out_item_id']
        if 'video_info_list' in response:
            self.video_info_list = response['video_info_list']
