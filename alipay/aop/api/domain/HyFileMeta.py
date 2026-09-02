#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HyFileMeta(object):

    def __init__(self):
        self._afts_file_url = None
        self._bitrate = None
        self._codec_long_name = None
        self._codec_name = None
        self._create_time = None
        self._duration = None
        self._encrypt = None
        self._file_id = None
        self._file_name = None
        self._file_type = None
        self._format_name = None
        self._height = None
        self._md5 = None
        self._size = None
        self._total_frames = None
        self._total_gif_frames = None
        self._width = None

    @property
    def afts_file_url(self):
        return self._afts_file_url

    @afts_file_url.setter
    def afts_file_url(self, value):
        self._afts_file_url = value
    @property
    def bitrate(self):
        return self._bitrate

    @bitrate.setter
    def bitrate(self, value):
        self._bitrate = value
    @property
    def codec_long_name(self):
        return self._codec_long_name

    @codec_long_name.setter
    def codec_long_name(self, value):
        self._codec_long_name = value
    @property
    def codec_name(self):
        return self._codec_name

    @codec_name.setter
    def codec_name(self, value):
        self._codec_name = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def encrypt(self):
        return self._encrypt

    @encrypt.setter
    def encrypt(self, value):
        self._encrypt = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def format_name(self):
        return self._format_name

    @format_name.setter
    def format_name(self, value):
        self._format_name = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def md5(self):
        return self._md5

    @md5.setter
    def md5(self, value):
        self._md5 = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def total_frames(self):
        return self._total_frames

    @total_frames.setter
    def total_frames(self, value):
        self._total_frames = value
    @property
    def total_gif_frames(self):
        return self._total_gif_frames

    @total_gif_frames.setter
    def total_gif_frames(self, value):
        self._total_gif_frames = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.afts_file_url:
            if hasattr(self.afts_file_url, 'to_alipay_dict'):
                params['afts_file_url'] = self.afts_file_url.to_alipay_dict()
            else:
                params['afts_file_url'] = self.afts_file_url
        if self.bitrate:
            if hasattr(self.bitrate, 'to_alipay_dict'):
                params['bitrate'] = self.bitrate.to_alipay_dict()
            else:
                params['bitrate'] = self.bitrate
        if self.codec_long_name:
            if hasattr(self.codec_long_name, 'to_alipay_dict'):
                params['codec_long_name'] = self.codec_long_name.to_alipay_dict()
            else:
                params['codec_long_name'] = self.codec_long_name
        if self.codec_name:
            if hasattr(self.codec_name, 'to_alipay_dict'):
                params['codec_name'] = self.codec_name.to_alipay_dict()
            else:
                params['codec_name'] = self.codec_name
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.encrypt:
            if hasattr(self.encrypt, 'to_alipay_dict'):
                params['encrypt'] = self.encrypt.to_alipay_dict()
            else:
                params['encrypt'] = self.encrypt
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.format_name:
            if hasattr(self.format_name, 'to_alipay_dict'):
                params['format_name'] = self.format_name.to_alipay_dict()
            else:
                params['format_name'] = self.format_name
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.md5:
            if hasattr(self.md5, 'to_alipay_dict'):
                params['md5'] = self.md5.to_alipay_dict()
            else:
                params['md5'] = self.md5
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.total_frames:
            if hasattr(self.total_frames, 'to_alipay_dict'):
                params['total_frames'] = self.total_frames.to_alipay_dict()
            else:
                params['total_frames'] = self.total_frames
        if self.total_gif_frames:
            if hasattr(self.total_gif_frames, 'to_alipay_dict'):
                params['total_gif_frames'] = self.total_gif_frames.to_alipay_dict()
            else:
                params['total_gif_frames'] = self.total_gif_frames
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HyFileMeta()
        if 'afts_file_url' in d:
            o.afts_file_url = d['afts_file_url']
        if 'bitrate' in d:
            o.bitrate = d['bitrate']
        if 'codec_long_name' in d:
            o.codec_long_name = d['codec_long_name']
        if 'codec_name' in d:
            o.codec_name = d['codec_name']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'duration' in d:
            o.duration = d['duration']
        if 'encrypt' in d:
            o.encrypt = d['encrypt']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'format_name' in d:
            o.format_name = d['format_name']
        if 'height' in d:
            o.height = d['height']
        if 'md5' in d:
            o.md5 = d['md5']
        if 'size' in d:
            o.size = d['size']
        if 'total_frames' in d:
            o.total_frames = d['total_frames']
        if 'total_gif_frames' in d:
            o.total_gif_frames = d['total_gif_frames']
        if 'width' in d:
            o.width = d['width']
        return o


