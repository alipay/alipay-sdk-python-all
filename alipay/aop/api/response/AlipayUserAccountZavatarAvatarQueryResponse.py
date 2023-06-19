#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AvatarVO import AvatarVO
from alipay.aop.api.domain.AvatarAnimationVO import AvatarAnimationVO
from alipay.aop.api.domain.StageSceneryVO import StageSceneryVO
from alipay.aop.api.domain.AvatarVO import AvatarVO
from alipay.aop.api.domain.AvatarAnimationVO import AvatarAnimationVO
from alipay.aop.api.domain.StageSceneryVO import StageSceneryVO


class AlipayUserAccountZavatarAvatarQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountZavatarAvatarQueryResponse, self).__init__()
        self._cust_avatar_vo = None
        self._default_animation_v_os = None
        self._default_stage_scenery_v_os = None
        self._digital_human_id = None
        self._init_avatar_v_os = None
        self._model_level = None
        self._optional_animation_v_os = None
        self._optional_stage_scenery_v_os = None

    @property
    def cust_avatar_vo(self):
        return self._cust_avatar_vo

    @cust_avatar_vo.setter
    def cust_avatar_vo(self, value):
        if isinstance(value, AvatarVO):
            self._cust_avatar_vo = value
        else:
            self._cust_avatar_vo = AvatarVO.from_alipay_dict(value)
    @property
    def default_animation_v_os(self):
        return self._default_animation_v_os

    @default_animation_v_os.setter
    def default_animation_v_os(self, value):
        if isinstance(value, list):
            self._default_animation_v_os = list()
            for i in value:
                if isinstance(i, AvatarAnimationVO):
                    self._default_animation_v_os.append(i)
                else:
                    self._default_animation_v_os.append(AvatarAnimationVO.from_alipay_dict(i))
    @property
    def default_stage_scenery_v_os(self):
        return self._default_stage_scenery_v_os

    @default_stage_scenery_v_os.setter
    def default_stage_scenery_v_os(self, value):
        if isinstance(value, list):
            self._default_stage_scenery_v_os = list()
            for i in value:
                if isinstance(i, StageSceneryVO):
                    self._default_stage_scenery_v_os.append(i)
                else:
                    self._default_stage_scenery_v_os.append(StageSceneryVO.from_alipay_dict(i))
    @property
    def digital_human_id(self):
        return self._digital_human_id

    @digital_human_id.setter
    def digital_human_id(self, value):
        self._digital_human_id = value
    @property
    def init_avatar_v_os(self):
        return self._init_avatar_v_os

    @init_avatar_v_os.setter
    def init_avatar_v_os(self, value):
        if isinstance(value, list):
            self._init_avatar_v_os = list()
            for i in value:
                if isinstance(i, AvatarVO):
                    self._init_avatar_v_os.append(i)
                else:
                    self._init_avatar_v_os.append(AvatarVO.from_alipay_dict(i))
    @property
    def model_level(self):
        return self._model_level

    @model_level.setter
    def model_level(self, value):
        self._model_level = value
    @property
    def optional_animation_v_os(self):
        return self._optional_animation_v_os

    @optional_animation_v_os.setter
    def optional_animation_v_os(self, value):
        if isinstance(value, list):
            self._optional_animation_v_os = list()
            for i in value:
                if isinstance(i, AvatarAnimationVO):
                    self._optional_animation_v_os.append(i)
                else:
                    self._optional_animation_v_os.append(AvatarAnimationVO.from_alipay_dict(i))
    @property
    def optional_stage_scenery_v_os(self):
        return self._optional_stage_scenery_v_os

    @optional_stage_scenery_v_os.setter
    def optional_stage_scenery_v_os(self, value):
        if isinstance(value, list):
            self._optional_stage_scenery_v_os = list()
            for i in value:
                if isinstance(i, StageSceneryVO):
                    self._optional_stage_scenery_v_os.append(i)
                else:
                    self._optional_stage_scenery_v_os.append(StageSceneryVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountZavatarAvatarQueryResponse, self).parse_response_content(response_content)
        if 'cust_avatar_vo' in response:
            self.cust_avatar_vo = response['cust_avatar_vo']
        if 'default_animation_v_os' in response:
            self.default_animation_v_os = response['default_animation_v_os']
        if 'default_stage_scenery_v_os' in response:
            self.default_stage_scenery_v_os = response['default_stage_scenery_v_os']
        if 'digital_human_id' in response:
            self.digital_human_id = response['digital_human_id']
        if 'init_avatar_v_os' in response:
            self.init_avatar_v_os = response['init_avatar_v_os']
        if 'model_level' in response:
            self.model_level = response['model_level']
        if 'optional_animation_v_os' in response:
            self.optional_animation_v_os = response['optional_animation_v_os']
        if 'optional_stage_scenery_v_os' in response:
            self.optional_stage_scenery_v_os = response['optional_stage_scenery_v_os']
