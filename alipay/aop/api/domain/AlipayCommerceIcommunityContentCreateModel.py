#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IcommunityContentMediaInfo import IcommunityContentMediaInfo
from alipay.aop.api.domain.IcommunityContentLocationInfo import IcommunityContentLocationInfo
from alipay.aop.api.domain.IcommunityContentUrlIndex import IcommunityContentUrlIndex


class AlipayCommerceIcommunityContentCreateModel(object):

    def __init__(self):
        self._content_create_biz_scene = None
        self._content_link_group_ids = None
        self._content_media_info = None
        self._content_publish_ip = None
        self._content_text = None
        self._content_title = None
        self._content_type = None
        self._location_info = None
        self._out_content_id = None
        self._province_name = None
        self._publish_time = None
        self._publisher_id = None
        self._topic_id_list = None
        self._url_info_list = None

    @property
    def content_create_biz_scene(self):
        return self._content_create_biz_scene

    @content_create_biz_scene.setter
    def content_create_biz_scene(self, value):
        self._content_create_biz_scene = value
    @property
    def content_link_group_ids(self):
        return self._content_link_group_ids

    @content_link_group_ids.setter
    def content_link_group_ids(self, value):
        if isinstance(value, list):
            self._content_link_group_ids = list()
            for i in value:
                self._content_link_group_ids.append(i)
    @property
    def content_media_info(self):
        return self._content_media_info

    @content_media_info.setter
    def content_media_info(self, value):
        if isinstance(value, list):
            self._content_media_info = list()
            for i in value:
                if isinstance(i, IcommunityContentMediaInfo):
                    self._content_media_info.append(i)
                else:
                    self._content_media_info.append(IcommunityContentMediaInfo.from_alipay_dict(i))
    @property
    def content_publish_ip(self):
        return self._content_publish_ip

    @content_publish_ip.setter
    def content_publish_ip(self, value):
        self._content_publish_ip = value
    @property
    def content_text(self):
        return self._content_text

    @content_text.setter
    def content_text(self, value):
        self._content_text = value
    @property
    def content_title(self):
        return self._content_title

    @content_title.setter
    def content_title(self, value):
        self._content_title = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def location_info(self):
        return self._location_info

    @location_info.setter
    def location_info(self, value):
        if isinstance(value, IcommunityContentLocationInfo):
            self._location_info = value
        else:
            self._location_info = IcommunityContentLocationInfo.from_alipay_dict(value)
    @property
    def out_content_id(self):
        return self._out_content_id

    @out_content_id.setter
    def out_content_id(self, value):
        self._out_content_id = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def publish_time(self):
        return self._publish_time

    @publish_time.setter
    def publish_time(self, value):
        self._publish_time = value
    @property
    def publisher_id(self):
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, value):
        self._publisher_id = value
    @property
    def topic_id_list(self):
        return self._topic_id_list

    @topic_id_list.setter
    def topic_id_list(self, value):
        if isinstance(value, list):
            self._topic_id_list = list()
            for i in value:
                self._topic_id_list.append(i)
    @property
    def url_info_list(self):
        return self._url_info_list

    @url_info_list.setter
    def url_info_list(self, value):
        if isinstance(value, list):
            self._url_info_list = list()
            for i in value:
                if isinstance(i, IcommunityContentUrlIndex):
                    self._url_info_list.append(i)
                else:
                    self._url_info_list.append(IcommunityContentUrlIndex.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.content_create_biz_scene:
            if hasattr(self.content_create_biz_scene, 'to_alipay_dict'):
                params['content_create_biz_scene'] = self.content_create_biz_scene.to_alipay_dict()
            else:
                params['content_create_biz_scene'] = self.content_create_biz_scene
        if self.content_link_group_ids:
            if isinstance(self.content_link_group_ids, list):
                for i in range(0, len(self.content_link_group_ids)):
                    element = self.content_link_group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_link_group_ids[i] = element.to_alipay_dict()
            if hasattr(self.content_link_group_ids, 'to_alipay_dict'):
                params['content_link_group_ids'] = self.content_link_group_ids.to_alipay_dict()
            else:
                params['content_link_group_ids'] = self.content_link_group_ids
        if self.content_media_info:
            if isinstance(self.content_media_info, list):
                for i in range(0, len(self.content_media_info)):
                    element = self.content_media_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_media_info[i] = element.to_alipay_dict()
            if hasattr(self.content_media_info, 'to_alipay_dict'):
                params['content_media_info'] = self.content_media_info.to_alipay_dict()
            else:
                params['content_media_info'] = self.content_media_info
        if self.content_publish_ip:
            if hasattr(self.content_publish_ip, 'to_alipay_dict'):
                params['content_publish_ip'] = self.content_publish_ip.to_alipay_dict()
            else:
                params['content_publish_ip'] = self.content_publish_ip
        if self.content_text:
            if hasattr(self.content_text, 'to_alipay_dict'):
                params['content_text'] = self.content_text.to_alipay_dict()
            else:
                params['content_text'] = self.content_text
        if self.content_title:
            if hasattr(self.content_title, 'to_alipay_dict'):
                params['content_title'] = self.content_title.to_alipay_dict()
            else:
                params['content_title'] = self.content_title
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.location_info:
            if hasattr(self.location_info, 'to_alipay_dict'):
                params['location_info'] = self.location_info.to_alipay_dict()
            else:
                params['location_info'] = self.location_info
        if self.out_content_id:
            if hasattr(self.out_content_id, 'to_alipay_dict'):
                params['out_content_id'] = self.out_content_id.to_alipay_dict()
            else:
                params['out_content_id'] = self.out_content_id
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.publish_time:
            if hasattr(self.publish_time, 'to_alipay_dict'):
                params['publish_time'] = self.publish_time.to_alipay_dict()
            else:
                params['publish_time'] = self.publish_time
        if self.publisher_id:
            if hasattr(self.publisher_id, 'to_alipay_dict'):
                params['publisher_id'] = self.publisher_id.to_alipay_dict()
            else:
                params['publisher_id'] = self.publisher_id
        if self.topic_id_list:
            if isinstance(self.topic_id_list, list):
                for i in range(0, len(self.topic_id_list)):
                    element = self.topic_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.topic_id_list[i] = element.to_alipay_dict()
            if hasattr(self.topic_id_list, 'to_alipay_dict'):
                params['topic_id_list'] = self.topic_id_list.to_alipay_dict()
            else:
                params['topic_id_list'] = self.topic_id_list
        if self.url_info_list:
            if isinstance(self.url_info_list, list):
                for i in range(0, len(self.url_info_list)):
                    element = self.url_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.url_info_list[i] = element.to_alipay_dict()
            if hasattr(self.url_info_list, 'to_alipay_dict'):
                params['url_info_list'] = self.url_info_list.to_alipay_dict()
            else:
                params['url_info_list'] = self.url_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIcommunityContentCreateModel()
        if 'content_create_biz_scene' in d:
            o.content_create_biz_scene = d['content_create_biz_scene']
        if 'content_link_group_ids' in d:
            o.content_link_group_ids = d['content_link_group_ids']
        if 'content_media_info' in d:
            o.content_media_info = d['content_media_info']
        if 'content_publish_ip' in d:
            o.content_publish_ip = d['content_publish_ip']
        if 'content_text' in d:
            o.content_text = d['content_text']
        if 'content_title' in d:
            o.content_title = d['content_title']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'location_info' in d:
            o.location_info = d['location_info']
        if 'out_content_id' in d:
            o.out_content_id = d['out_content_id']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'publish_time' in d:
            o.publish_time = d['publish_time']
        if 'publisher_id' in d:
            o.publisher_id = d['publisher_id']
        if 'topic_id_list' in d:
            o.topic_id_list = d['topic_id_list']
        if 'url_info_list' in d:
            o.url_info_list = d['url_info_list']
        return o


