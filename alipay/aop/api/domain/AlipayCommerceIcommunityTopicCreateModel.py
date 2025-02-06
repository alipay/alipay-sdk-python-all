#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIcommunityTopicCreateModel(object):

    def __init__(self):
        self._out_request_id = None
        self._topic_avatar = None
        self._topic_background_image = None
        self._topic_create_biz_scene = None
        self._topic_creator_id = None
        self._topic_desc = None
        self._topic_link_group_ids = None
        self._topic_name = None

    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value
    @property
    def topic_avatar(self):
        return self._topic_avatar

    @topic_avatar.setter
    def topic_avatar(self, value):
        self._topic_avatar = value
    @property
    def topic_background_image(self):
        return self._topic_background_image

    @topic_background_image.setter
    def topic_background_image(self, value):
        self._topic_background_image = value
    @property
    def topic_create_biz_scene(self):
        return self._topic_create_biz_scene

    @topic_create_biz_scene.setter
    def topic_create_biz_scene(self, value):
        self._topic_create_biz_scene = value
    @property
    def topic_creator_id(self):
        return self._topic_creator_id

    @topic_creator_id.setter
    def topic_creator_id(self, value):
        self._topic_creator_id = value
    @property
    def topic_desc(self):
        return self._topic_desc

    @topic_desc.setter
    def topic_desc(self, value):
        self._topic_desc = value
    @property
    def topic_link_group_ids(self):
        return self._topic_link_group_ids

    @topic_link_group_ids.setter
    def topic_link_group_ids(self, value):
        if isinstance(value, list):
            self._topic_link_group_ids = list()
            for i in value:
                self._topic_link_group_ids.append(i)
    @property
    def topic_name(self):
        return self._topic_name

    @topic_name.setter
    def topic_name(self, value):
        self._topic_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_id:
            if hasattr(self.out_request_id, 'to_alipay_dict'):
                params['out_request_id'] = self.out_request_id.to_alipay_dict()
            else:
                params['out_request_id'] = self.out_request_id
        if self.topic_avatar:
            if hasattr(self.topic_avatar, 'to_alipay_dict'):
                params['topic_avatar'] = self.topic_avatar.to_alipay_dict()
            else:
                params['topic_avatar'] = self.topic_avatar
        if self.topic_background_image:
            if hasattr(self.topic_background_image, 'to_alipay_dict'):
                params['topic_background_image'] = self.topic_background_image.to_alipay_dict()
            else:
                params['topic_background_image'] = self.topic_background_image
        if self.topic_create_biz_scene:
            if hasattr(self.topic_create_biz_scene, 'to_alipay_dict'):
                params['topic_create_biz_scene'] = self.topic_create_biz_scene.to_alipay_dict()
            else:
                params['topic_create_biz_scene'] = self.topic_create_biz_scene
        if self.topic_creator_id:
            if hasattr(self.topic_creator_id, 'to_alipay_dict'):
                params['topic_creator_id'] = self.topic_creator_id.to_alipay_dict()
            else:
                params['topic_creator_id'] = self.topic_creator_id
        if self.topic_desc:
            if hasattr(self.topic_desc, 'to_alipay_dict'):
                params['topic_desc'] = self.topic_desc.to_alipay_dict()
            else:
                params['topic_desc'] = self.topic_desc
        if self.topic_link_group_ids:
            if isinstance(self.topic_link_group_ids, list):
                for i in range(0, len(self.topic_link_group_ids)):
                    element = self.topic_link_group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.topic_link_group_ids[i] = element.to_alipay_dict()
            if hasattr(self.topic_link_group_ids, 'to_alipay_dict'):
                params['topic_link_group_ids'] = self.topic_link_group_ids.to_alipay_dict()
            else:
                params['topic_link_group_ids'] = self.topic_link_group_ids
        if self.topic_name:
            if hasattr(self.topic_name, 'to_alipay_dict'):
                params['topic_name'] = self.topic_name.to_alipay_dict()
            else:
                params['topic_name'] = self.topic_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIcommunityTopicCreateModel()
        if 'out_request_id' in d:
            o.out_request_id = d['out_request_id']
        if 'topic_avatar' in d:
            o.topic_avatar = d['topic_avatar']
        if 'topic_background_image' in d:
            o.topic_background_image = d['topic_background_image']
        if 'topic_create_biz_scene' in d:
            o.topic_create_biz_scene = d['topic_create_biz_scene']
        if 'topic_creator_id' in d:
            o.topic_creator_id = d['topic_creator_id']
        if 'topic_desc' in d:
            o.topic_desc = d['topic_desc']
        if 'topic_link_group_ids' in d:
            o.topic_link_group_ids = d['topic_link_group_ids']
        if 'topic_name' in d:
            o.topic_name = d['topic_name']
        return o


