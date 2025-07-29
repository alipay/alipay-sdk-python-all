#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CurrentChatAudio import CurrentChatAudio
from alipay.aop.api.domain.CurrentChatAudios import CurrentChatAudios
from alipay.aop.api.domain.CurrentChatFile import CurrentChatFile
from alipay.aop.api.domain.CurrentChatFiles import CurrentChatFiles
from alipay.aop.api.domain.CurrentChatVideo import CurrentChatVideo
from alipay.aop.api.domain.CurrentChatVideos import CurrentChatVideos


class MultiModalInputsRequest(object):

    def __init__(self):
        self._current_chat_audio = None
        self._current_chat_audios = None
        self._current_chat_file = None
        self._current_chat_files = None
        self._current_chat_video = None
        self._current_chat_videos = None
        self._images = None

    @property
    def current_chat_audio(self):
        return self._current_chat_audio

    @current_chat_audio.setter
    def current_chat_audio(self, value):
        if isinstance(value, CurrentChatAudio):
            self._current_chat_audio = value
        else:
            self._current_chat_audio = CurrentChatAudio.from_alipay_dict(value)
    @property
    def current_chat_audios(self):
        return self._current_chat_audios

    @current_chat_audios.setter
    def current_chat_audios(self, value):
        if isinstance(value, CurrentChatAudios):
            self._current_chat_audios = value
        else:
            self._current_chat_audios = CurrentChatAudios.from_alipay_dict(value)
    @property
    def current_chat_file(self):
        return self._current_chat_file

    @current_chat_file.setter
    def current_chat_file(self, value):
        if isinstance(value, CurrentChatFile):
            self._current_chat_file = value
        else:
            self._current_chat_file = CurrentChatFile.from_alipay_dict(value)
    @property
    def current_chat_files(self):
        return self._current_chat_files

    @current_chat_files.setter
    def current_chat_files(self, value):
        if isinstance(value, CurrentChatFiles):
            self._current_chat_files = value
        else:
            self._current_chat_files = CurrentChatFiles.from_alipay_dict(value)
    @property
    def current_chat_video(self):
        return self._current_chat_video

    @current_chat_video.setter
    def current_chat_video(self, value):
        if isinstance(value, CurrentChatVideo):
            self._current_chat_video = value
        else:
            self._current_chat_video = CurrentChatVideo.from_alipay_dict(value)
    @property
    def current_chat_videos(self):
        return self._current_chat_videos

    @current_chat_videos.setter
    def current_chat_videos(self, value):
        if isinstance(value, CurrentChatVideos):
            self._current_chat_videos = value
        else:
            self._current_chat_videos = CurrentChatVideos.from_alipay_dict(value)
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.current_chat_audio:
            if hasattr(self.current_chat_audio, 'to_alipay_dict'):
                params['current_chat_audio'] = self.current_chat_audio.to_alipay_dict()
            else:
                params['current_chat_audio'] = self.current_chat_audio
        if self.current_chat_audios:
            if hasattr(self.current_chat_audios, 'to_alipay_dict'):
                params['current_chat_audios'] = self.current_chat_audios.to_alipay_dict()
            else:
                params['current_chat_audios'] = self.current_chat_audios
        if self.current_chat_file:
            if hasattr(self.current_chat_file, 'to_alipay_dict'):
                params['current_chat_file'] = self.current_chat_file.to_alipay_dict()
            else:
                params['current_chat_file'] = self.current_chat_file
        if self.current_chat_files:
            if hasattr(self.current_chat_files, 'to_alipay_dict'):
                params['current_chat_files'] = self.current_chat_files.to_alipay_dict()
            else:
                params['current_chat_files'] = self.current_chat_files
        if self.current_chat_video:
            if hasattr(self.current_chat_video, 'to_alipay_dict'):
                params['current_chat_video'] = self.current_chat_video.to_alipay_dict()
            else:
                params['current_chat_video'] = self.current_chat_video
        if self.current_chat_videos:
            if hasattr(self.current_chat_videos, 'to_alipay_dict'):
                params['current_chat_videos'] = self.current_chat_videos.to_alipay_dict()
            else:
                params['current_chat_videos'] = self.current_chat_videos
        if self.images:
            if isinstance(self.images, list):
                for i in range(0, len(self.images)):
                    element = self.images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.images[i] = element.to_alipay_dict()
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiModalInputsRequest()
        if 'current_chat_audio' in d:
            o.current_chat_audio = d['current_chat_audio']
        if 'current_chat_audios' in d:
            o.current_chat_audios = d['current_chat_audios']
        if 'current_chat_file' in d:
            o.current_chat_file = d['current_chat_file']
        if 'current_chat_files' in d:
            o.current_chat_files = d['current_chat_files']
        if 'current_chat_video' in d:
            o.current_chat_video = d['current_chat_video']
        if 'current_chat_videos' in d:
            o.current_chat_videos = d['current_chat_videos']
        if 'images' in d:
            o.images = d['images']
        return o


