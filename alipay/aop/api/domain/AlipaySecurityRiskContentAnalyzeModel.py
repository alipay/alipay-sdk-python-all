#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskContentAnalyzeModel(object):

    def __init__(self):
        self._account_id = None
        self._account_type = None
        self._app_main_scene = None
        self._app_main_scene_id = None
        self._app_name = None
        self._app_scene = None
        self._app_scene_data_id = None
        self._audio_urls = None
        self._link_urls = None
        self._picture_urls = None
        self._publish_date = None
        self._text = None
        self._text_type = None
        self._video_urls = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def app_main_scene(self):
        return self._app_main_scene

    @app_main_scene.setter
    def app_main_scene(self, value):
        self._app_main_scene = value
    @property
    def app_main_scene_id(self):
        return self._app_main_scene_id

    @app_main_scene_id.setter
    def app_main_scene_id(self, value):
        self._app_main_scene_id = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_scene(self):
        return self._app_scene

    @app_scene.setter
    def app_scene(self, value):
        self._app_scene = value
    @property
    def app_scene_data_id(self):
        return self._app_scene_data_id

    @app_scene_data_id.setter
    def app_scene_data_id(self, value):
        self._app_scene_data_id = value
    @property
    def audio_urls(self):
        return self._audio_urls

    @audio_urls.setter
    def audio_urls(self, value):
        if isinstance(value, list):
            self._audio_urls = list()
            for i in value:
                self._audio_urls.append(i)
    @property
    def link_urls(self):
        return self._link_urls

    @link_urls.setter
    def link_urls(self, value):
        if isinstance(value, list):
            self._link_urls = list()
            for i in value:
                self._link_urls.append(i)
    @property
    def picture_urls(self):
        return self._picture_urls

    @picture_urls.setter
    def picture_urls(self, value):
        if isinstance(value, list):
            self._picture_urls = list()
            for i in value:
                self._picture_urls.append(i)
    @property
    def publish_date(self):
        return self._publish_date

    @publish_date.setter
    def publish_date(self, value):
        self._publish_date = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def text_type(self):
        return self._text_type

    @text_type.setter
    def text_type(self, value):
        self._text_type = value
    @property
    def video_urls(self):
        return self._video_urls

    @video_urls.setter
    def video_urls(self, value):
        if isinstance(value, list):
            self._video_urls = list()
            for i in value:
                self._video_urls.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.app_main_scene:
            if hasattr(self.app_main_scene, 'to_alipay_dict'):
                params['app_main_scene'] = self.app_main_scene.to_alipay_dict()
            else:
                params['app_main_scene'] = self.app_main_scene
        if self.app_main_scene_id:
            if hasattr(self.app_main_scene_id, 'to_alipay_dict'):
                params['app_main_scene_id'] = self.app_main_scene_id.to_alipay_dict()
            else:
                params['app_main_scene_id'] = self.app_main_scene_id
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_scene:
            if hasattr(self.app_scene, 'to_alipay_dict'):
                params['app_scene'] = self.app_scene.to_alipay_dict()
            else:
                params['app_scene'] = self.app_scene
        if self.app_scene_data_id:
            if hasattr(self.app_scene_data_id, 'to_alipay_dict'):
                params['app_scene_data_id'] = self.app_scene_data_id.to_alipay_dict()
            else:
                params['app_scene_data_id'] = self.app_scene_data_id
        if self.audio_urls:
            if isinstance(self.audio_urls, list):
                for i in range(0, len(self.audio_urls)):
                    element = self.audio_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.audio_urls[i] = element.to_alipay_dict()
            if hasattr(self.audio_urls, 'to_alipay_dict'):
                params['audio_urls'] = self.audio_urls.to_alipay_dict()
            else:
                params['audio_urls'] = self.audio_urls
        if self.link_urls:
            if isinstance(self.link_urls, list):
                for i in range(0, len(self.link_urls)):
                    element = self.link_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.link_urls[i] = element.to_alipay_dict()
            if hasattr(self.link_urls, 'to_alipay_dict'):
                params['link_urls'] = self.link_urls.to_alipay_dict()
            else:
                params['link_urls'] = self.link_urls
        if self.picture_urls:
            if isinstance(self.picture_urls, list):
                for i in range(0, len(self.picture_urls)):
                    element = self.picture_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.picture_urls[i] = element.to_alipay_dict()
            if hasattr(self.picture_urls, 'to_alipay_dict'):
                params['picture_urls'] = self.picture_urls.to_alipay_dict()
            else:
                params['picture_urls'] = self.picture_urls
        if self.publish_date:
            if hasattr(self.publish_date, 'to_alipay_dict'):
                params['publish_date'] = self.publish_date.to_alipay_dict()
            else:
                params['publish_date'] = self.publish_date
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.text_type:
            if hasattr(self.text_type, 'to_alipay_dict'):
                params['text_type'] = self.text_type.to_alipay_dict()
            else:
                params['text_type'] = self.text_type
        if self.video_urls:
            if isinstance(self.video_urls, list):
                for i in range(0, len(self.video_urls)):
                    element = self.video_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_urls[i] = element.to_alipay_dict()
            if hasattr(self.video_urls, 'to_alipay_dict'):
                params['video_urls'] = self.video_urls.to_alipay_dict()
            else:
                params['video_urls'] = self.video_urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskContentAnalyzeModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'app_main_scene' in d:
            o.app_main_scene = d['app_main_scene']
        if 'app_main_scene_id' in d:
            o.app_main_scene_id = d['app_main_scene_id']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_scene' in d:
            o.app_scene = d['app_scene']
        if 'app_scene_data_id' in d:
            o.app_scene_data_id = d['app_scene_data_id']
        if 'audio_urls' in d:
            o.audio_urls = d['audio_urls']
        if 'link_urls' in d:
            o.link_urls = d['link_urls']
        if 'picture_urls' in d:
            o.picture_urls = d['picture_urls']
        if 'publish_date' in d:
            o.publish_date = d['publish_date']
        if 'text' in d:
            o.text = d['text']
        if 'text_type' in d:
            o.text_type = d['text_type']
        if 'video_urls' in d:
            o.video_urls = d['video_urls']
        return o


