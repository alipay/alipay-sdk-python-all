#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShortPlayFrameFile(object):

    def __init__(self):
        self._episode_num = None
        self._file_id = None

    @property
    def episode_num(self):
        return self._episode_num

    @episode_num.setter
    def episode_num(self, value):
        self._episode_num = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.episode_num:
            if hasattr(self.episode_num, 'to_alipay_dict'):
                params['episode_num'] = self.episode_num.to_alipay_dict()
            else:
                params['episode_num'] = self.episode_num
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShortPlayFrameFile()
        if 'episode_num' in d:
            o.episode_num = d['episode_num']
        if 'file_id' in d:
            o.file_id = d['file_id']
        return o


